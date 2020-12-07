#! /usr/bin/env python
""" create miniconda.rst file with size and sha256 for latest installers """

import urllib.request
import json

from jinja2 import Template

OUT_FILENAME = "miniconda.rst"
TEMPLATE_FILENAME = "miniconda.rst.jinja2"
FILES_URL = "https://repo.anaconda.com/miniconda/.files.json"


def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi"]:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, "Yi", suffix)


def get_latest_miniconda_sizes_and_hashes():
    with urllib.request.urlopen(urllib.request.Request(url=FILES_URL)) as f:
        data = json.loads(f.read().decode("utf-8"))

    win32_py2 = data['Miniconda2-latest-Windows-x86.exe']
    win32_py3 = data['Miniconda3-latest-Windows-x86.exe']

    win64_py2 = data['Miniconda2-latest-Windows-x86_64.exe']
    win64_py3 = data['Miniconda3-latest-Windows-x86_64.exe']

    osx64_sh_py2 = data['Miniconda2-latest-MacOSX-x86_64.sh']
    osx64_sh_py3 = data['Miniconda3-latest-MacOSX-x86_64.sh']

    osx64_pkg_py2 = data['Miniconda2-latest-MacOSX-x86_64.pkg']
    osx64_pkg_py3 = data['Miniconda3-latest-MacOSX-x86_64.pkg']

    linux32_py2 = data['Miniconda2-latest-Linux-x86.sh']
    linux32_py3 = data['Miniconda3-latest-Linux-x86.sh']

    linux64_py2 = data['Miniconda2-latest-Linux-x86_64.sh']
    linux64_py3 = data['Miniconda3-latest-Linux-x86_64.sh']

    info = {
        'win32_py2_size': sizeof_fmt(win32_py2['size']),
        'win32_py2_hash': win32_py2['sha256'],
        'win32_py3_size': sizeof_fmt(win32_py3['size']),
        'win32_py3_hash': win32_py3['sha256'],

        'win64_py2_size': sizeof_fmt(win64_py2['size']),
        'win64_py2_hash': win64_py2['sha256'],
        'win64_py3_size': sizeof_fmt(win64_py3['size']),
        'win64_py3_hash': win64_py3['sha256'],

        'osx64_sh_py2_size': sizeof_fmt(osx64_sh_py2['size']),
        'osx64_sh_py2_hash': osx64_sh_py2['sha256'],
        'osx64_sh_py3_size': sizeof_fmt(osx64_sh_py3['size']),
        'osx64_sh_py3_hash': osx64_sh_py3['sha256'],

        'osx64_pkg_py2_size': sizeof_fmt(osx64_pkg_py2['size']),
        'osx64_pkg_py2_hash': osx64_pkg_py2['sha256'],
        'osx64_pkg_py3_size': sizeof_fmt(osx64_pkg_py3['size']),
        'osx64_pkg_py3_hash': osx64_pkg_py3['sha256'],

        'linux32_py2_size': sizeof_fmt(linux32_py2['size']),
        'linux32_py2_hash': linux32_py2['sha256'],
        'linux32_py3_size': sizeof_fmt(linux32_py3['size']),
        'linux32_py3_hash': linux32_py3['sha256'],

        'linux64_py2_size': sizeof_fmt(linux64_py2['size']),
        'linux64_py2_hash': linux64_py2['sha256'],
        'linux64_py3_size': sizeof_fmt(linux64_py3['size']),
        'linux64_py3_hash': linux64_py3['sha256'],
    }
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
