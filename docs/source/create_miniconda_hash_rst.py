""" create rst file with size, date and sha256 for miniconda installers """

import urllib.request
import json
import datetime
import math
import os
import time
from packaging.version import Version

# Column lengths
FILENAME_LEN = 42
SIZE_LEN = 9
TIMEMOD_LEN = 19
HASH_LEN = 68

OUT_FILENAME = "miniconda_hashes.rst"


def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi"]:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, "Yi", suffix)


def main():
    FILES_URL = "https://repo.anaconda.com/miniconda/.files.json"
    with urllib.request.urlopen(urllib.request.Request(url=FILES_URL)) as f:
        data = json.loads(f.read().decode("utf-8"))
    # remove index.json and 'latest' entries
    data.pop("index.json")
    data = {k: v for k, v in data.items() if "latest" not in k}

    # write file with hashes for all files
    f = open(OUT_FILENAME, "w")
    f.write(":orphan:\n\n")
    title = "Miniconda hash information"
    f.write("=" * len(title) + "\n" + title + "\n" + "=" * len(title) + "\n\n")
    f.write(
        "=" * FILENAME_LEN
        + "   "
        + "=" * SIZE_LEN
        + "   "
        + "=" * TIMEMOD_LEN
        + "  "
        + "=" * HASH_LEN
        + "\n"
    )
    f.write(
        "Name".ljust(FILENAME_LEN)
        + "   "
        + "Size".ljust(SIZE_LEN)
        + "   "
        + "Time modified".ljust(TIMEMOD_LEN)
        + "  "
        + "SHA256 hash".ljust(HASH_LEN)
        + "\n"
    )
    f.write(
        "=" * FILENAME_LEN
        + "   "
        + "=" * SIZE_LEN
        + "   "
        + "=" * TIMEMOD_LEN
        + "  "
        + "=" * HASH_LEN
        + "\n"
    )
    def sorting_key(filename):
        # typically the filename is Miniconda{2,3}-version-platform.ext
        version_str = filename.split("-")[1]
        # cases where the filename is Miniconda3-py3X_version-platform.ext
        if "_" in version_str:
            version_str = version_str.split("_")[1]
        return Version(version_str)
    # =================================================================
    # the main hosting server is central time, so pretend we are too
    # in order for anyone to be able to run this on Unix platforms.
    os.environ['TZ'] = 'US/Central'
    time.tzset()
    # =================================================================
    for filename in sorted(data, reverse=True, key=sorting_key):
        last_modified = datetime.datetime.fromtimestamp(
            math.floor(data[filename]["mtime"])
        )
        last_mod_str = (
            last_modified.date().isoformat() + " " + last_modified.time().isoformat()
        )
        if "sha256" not in data[filename]:
            print("WARNING: no sha256 information for:", filename)
            continue
        f.write(
            filename.ljust(FILENAME_LEN)
            + "   "
            + sizeof_fmt(data[filename]["size"]).rjust(SIZE_LEN)
            + "   "
            + last_mod_str.ljust(TIMEMOD_LEN)
            + "  "
            + "``"
            + str(data[filename]["sha256"])
            + "``\n"
        )
    f.write(
        "=" * FILENAME_LEN
        + "   "
        + "=" * SIZE_LEN
        + "   "
        + "=" * TIMEMOD_LEN
        + "  "
        + "=" * HASH_LEN
        + "\n"
    )


if __name__ == "__main__":
    main()
