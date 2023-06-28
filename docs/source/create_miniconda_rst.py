#! /usr/bin/env python
""" 
Create miniconda.rst file with size and sha256 for latest installers.
See the miniconda.rst.jinja2 for the template that is ultimately rendered.

NOTE: Please make sure to update the global variables below:
- MINICONDA_VERSION
- PYTHON_VERSION

NOTE: Also confirm the PLATFORM_MAP is up-to-date.

NOTE: If a new Python variant has been built out, please update the tuple
below for 'py_version'.
"""

import datetime
import urllib.request
import json

from jinja2 import Template

OUT_FILENAME = "miniconda.rst"
TEMPLATE_FILENAME = "miniconda.rst.jinja2"
FILES_URL = "https://repo.anaconda.com/miniconda/.files.json"

# Update these!
MINICONDA_VERSION = "23.3.1-0"
PYTHON_VERSION = "3.10.10"  # This is the version of Python that's bundled into the Miniconda installers.

# Confirm these are up-to-date.
PLATFORM_MAP = {
    "win64": "Windows-x86_64.exe",
    "win32": "Windows-x86.exe",
    "osx64_sh": "MacOSX-x86_64.sh",
    "osx64_pkg": "MacOSX-x86_64.pkg",
    "osx_arm64_sh": "MacOSX-arm64.sh",
    "osx_arm64_pkg": "MacOSX-arm64.pkg",
    "linux64": "Linux-x86_64.sh",
    "linux_aarch64": "Linux-aarch64.sh",
    "linux_ppc64le": "Linux-ppc64le.sh",
    "linux_s390x": "Linux-s390x.sh",
}


def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi"]:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, "Yi", suffix)


def get_latest_miniconda_sizes_and_hashes():
    """
    Returns a dict with sizes and SHA256 hashes for each
    installer built for the latest CONDA_VERSION.
    """
    with urllib.request.urlopen(urllib.request.Request(url=FILES_URL)) as f:
        data = json.loads(f.read().decode("utf-8"))

    info = {
        "miniconda_version": MINICONDA_VERSION,
        "conda_version": MINICONDA_VERSION.split("-")[0],
        "python_version": PYTHON_VERSION,
    }

    for platform_id, installer_suffix in PLATFORM_MAP.items():
        latest_installer = f"Miniconda3-latest-{installer_suffix}"
        if "release_date" not in info:
            mtime = data[latest_installer]["mtime"]
            mdate = datetime.date.fromtimestamp(mtime)
            info["release_date"] = mdate.strftime("%B %-d, %Y")
        info[f"{platform_id}_py3_latest_size"] = sizeof_fmt(data[latest_installer]["size"])
        info[f"{platform_id}_py3_latest_hash"] = data[latest_installer]["sha256"]
        for py_version in ("38", "39", "310"):
            full_installer = f"Miniconda3-py{py_version}_{MINICONDA_VERSION}-{installer_suffix}"

            # win-32 is and will remain at "frozen" at v4.12.0 
            # (we no longer make new builds for this subdir)
            if platform_id == "win32":
                full_installer = f"Miniconda3-py{py_version}_4.12.0-{installer_suffix}"

            if full_installer not in data:
                continue
            info[f"{platform_id}_py{py_version}_size"] = sizeof_fmt(data[full_installer]["size"])
            info[f"{platform_id}_py{py_version}_hash"] = data[full_installer]["sha256"]

    return info


def main():
    rst_vars = get_latest_miniconda_sizes_and_hashes()

    with open(TEMPLATE_FILENAME) as f:
        template_text = f.read()

    template = Template(template_text)
    rst_text = template.render(**rst_vars)
    with open(OUT_FILENAME, 'w') as f:
        f.write(rst_text)


if __name__ == "__main__":
    main()
