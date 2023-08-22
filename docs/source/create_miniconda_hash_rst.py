#! /usr/bin/env python
"""
Create rst file with size, date and sha256 for miniconda installers.

"""

import datetime
import json
import math
import os
import time
import urllib.request
from pathlib import Path

from packaging.version import Version

# Column lengths
FILENAME_LEN = 47
SIZE_LEN = 9
TIMEMOD_LEN = 19
HASH_LEN = 68

HERE = Path(__file__).parent
OUT_FILENAME = HERE / "miniconda-hashes.rst"


def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}{suffix}"
        num /= 1024.0
    return "{:.1f} {}{}".format(num, "Yi", suffix)


def main():
    # =================================================================
    # The main hosting server is central time, so pretend we are too
    # in order for anyone to be able to run this on Unix platforms.
    os.environ["TZ"] = "US/Central"
    time.tzset()
    # =================================================================

    FILES_URL = "https://repo.anaconda.com/miniconda/.files.json"
    with urllib.request.urlopen(urllib.request.Request(url=FILES_URL)) as f:
        data = json.loads(f.read().decode("utf-8"))
    # remove index.json and 'latest' entries
    data.pop("index.json")
    data = {
        k: v for k, v in data.items() if "latest" not in k and "uninstaller" not in k
    }

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
        """
        Sort by:
          conda_version_platform_ext (e.g. "23.1.0-1-Linux-x86_64.sh")
          miniconda_prefix (e.g. "Miniconda3")
          py_version (e.g. the "310" from "py310")
        """
        # 1. conda_version_platform_ext
        version_str = filename.split("-")[1]
        # Starting with v4.8.2 in 2020, we release Miniconda variants for each
        # python version we support: Miniconda3-py3XX_<version>-<platform>.<ext>
        # So we need to split that off.
        if "_" in version_str:
            version_str = version_str.split("_")[1]
        conda_version_platform_ext = version_str

        # 2. miniconda_prefix
        miniconda_prefix = filename.split("-")[0]

        # 3. py_version
        if "py" in filename:
            py_intermediate = filename.split("py")[1]
            py_version = int(py_intermediate.split("_")[0])
        else:
            py_version = ""

        return (Version(conda_version_platform_ext), miniconda_prefix, py_version)

    # We sort the 'data' dict by our special sorting_key() function,
    # which accounts for all the ways our Miniconda installers have
    # changed their naming format over the years.
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
