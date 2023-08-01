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
import json
import urllib.request
from pathlib import Path

from jinja2 import Template
from packaging.version import Version

HERE = Path(__file__).parent
OUT_FILENAME = HERE / "miniconda.rst"
TEMPLATE_FILENAME = HERE / "miniconda.rst.jinja2"
FILES_URL = "https://repo.anaconda.com/miniconda/.files.json"

# Update these!
MINICONDA_VERSION = "23.5.2-0"
PYTHON_VERSION = (
    "3.11.3"  # the version of Python that's bundled into the Miniconda installers.
)
PY_VERSIONS = ("3.11", "3.10", "3.9", "3.8")

# Must be sorted in the order in which they appear on the Miniconda page
OPERATING_SYSTEMS = ("Windows", "macOS", "Linux")

# Confirm these are up-to-date.
PLATFORM_MAP = {
    "win64": {
        "operating_system": "Windows",
        "suffix": "Windows-x86_64.exe",
        "description": "Windows 64-bit",
    },
    "win32": {
        "operating_system": "Windows",
        "suffix": "Windows-x86.exe",
        "description": "Windows 32-bit",
    },
    "osx64_sh": {
        "operating_system": "macOS",
        "suffix": "MacOSX-x86_64.sh",
        "description": "macOS Intel x86 64-bit bash",
    },
    "osx64_pkg": {
        "operating_system": "macOS",
        "suffix": "MacOSX-x86_64.pkg",
        "description": "macOS Intel x86 64-bit pkg",
    },
    "osx_arm64_sh": {
        "operating_system": "macOS",
        "suffix": "MacOSX-arm64.sh",
        "description": "macOS Apple M1 64-bit bash",
    },
    "osx_arm64_pkg": {
        "operating_system": "macOS",
        "suffix": "MacOSX-arm64.pkg",
        "description": "macOS Apple M1 64-bit pkg",
    },
    "linux64": {
        "operating_system": "Linux",
        "suffix": "Linux-x86_64.sh",
        "description": "Linux 64-bit",
    },
    "linux_aarch64": {
        "operating_system": "Linux",
        "suffix": "Linux-aarch64.sh",
        "description": "Linux-aarch64 64-bit",
    },
    "linux_ppc64le": {
        "operating_system": "Linux",
        "suffix": "Linux-ppc64le.sh",
        "description": "Linux-ppc64le 64-bit",
    },
    "linux_s390x": {
        "operating_system": "Linux",
        "suffix": "Linux-s390x.sh",
        "description": "Linux-s390x 64-bit",
    },
}


def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}{suffix}"
        num /= 1024.0
    return "{:.1f} {}{}".format(num, "Yi", suffix)


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
        "operating_systems": OPERATING_SYSTEMS,
        "py_versions": sorted(PY_VERSIONS, reverse=True, key=Version),
    }
    info["platforms"] = {(os, "latest"): [] for os in info["operating_systems"]}

    for platform_id, installer_data in PLATFORM_MAP.items():
        latest_installer = f"Miniconda3-latest-{installer_data['suffix']}"
        if "release_date" not in info:
            mtime = data[latest_installer]["mtime"]
            mdate = datetime.date.fromtimestamp(mtime)
            info["release_date"] = mdate.strftime("%B %-d, %Y")
        os = installer_data["operating_system"]
        info["platforms"][os, "latest"].append(installer_data.copy())
        info["platforms"][os, "latest"][-1]["hash"] = data[latest_installer]["sha256"]
        for py_version in info["py_versions"]:
            py = py_version.replace(".", "")
            full_installer = (
                f"Miniconda3-py{py}_{MINICONDA_VERSION}-{installer_data['suffix']}"
            )

            # win-32 is and will remain at "frozen" at v4.12.0
            # (we no longer make new builds for this subdir)
            if platform_id == "win32":
                full_installer = f"Miniconda3-py{py}_4.12.0-{installer_data['suffix']}"

            if full_installer not in data:
                continue
            if (os, py_version) not in info["platforms"]:
                info["platforms"][os, py_version] = [installer_data.copy()]
            else:
                info["platforms"][os, py_version].append(installer_data.copy())
            installer = info["platforms"][os, py_version][-1]
            installer["size"] = sizeof_fmt(data[full_installer]["size"])
            installer["hash"] = data[full_installer]["sha256"]
            # full_installer item is needed until win-32 is removed
            installer["full_installer"] = full_installer

    return info


def main():
    rst_vars = get_latest_miniconda_sizes_and_hashes()

    with open(TEMPLATE_FILENAME) as f:
        template_text = f.read()

    template = Template(template_text)
    rst_text = template.render(**rst_vars)
    with open(OUT_FILENAME, "w") as f:
        f.write(rst_text)


if __name__ == "__main__":
    main()
