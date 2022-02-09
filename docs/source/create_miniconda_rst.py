#! /usr/bin/env python
""" create miniconda.rst file with size and sha256 for latest installers """

import urllib.request
import json

from jinja2 import Template

OUT_FILENAME = "miniconda.rst"
TEMPLATE_FILENAME = "miniconda.rst.jinja2"
FILES_URL = "https://repo.anaconda.com/miniconda/.files.json"

CONDA_VERSION = "4.10.3"
PLATFORM_MAP = {
    "win32": "Windows-x86.exe",
    "win64": "Windows-x86_64.exe",
    "osx64_sh": "MacOSX-x86_64.sh",
    "osx64_pkg": "MacOSX-x86_64.pkg",
    "osx_arm64_sh": "MacOSX-arm64.sh",
    "linux32": "Linux-x86.sh",
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
    with urllib.request.urlopen(urllib.request.Request(url=FILES_URL)) as f:
        data = json.loads(f.read().decode("utf-8"))

    info = {
        "conda_version": CONDA_VERSION
    }
    for platform_id, installer_suffix in PLATFORM_MAP.items():
        latest_installer = 'Miniconda3-latest-{}'.format(installer_suffix)
        info["{}_py3_latest_size".format(platform_id)] = sizeof_fmt(data[latest_installer]['size'])
        info["{}_py3_latest_hash".format(platform_id)] = data[latest_installer]['sha256']
        for py_version in ("37", "38", "39"):
            full_installer = 'Miniconda3-py{}_{}-{}'.format(py_version, CONDA_VERSION, installer_suffix)
            if full_installer not in data:
                continue
            info["{}_py{}_size".format(platform_id, py_version)] = sizeof_fmt(data[full_installer]['size'])
            info["{}_py{}_hash".format(platform_id, py_version)] = data[full_installer]['sha256']

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
