import datetime
import urllib.request
import json

from pathlib import Path
from packaging.version import Version
from jinja2 import Template


SOURCE_DIR = Path(__file__).parent
RELEASE_DIR = SOURCE_DIR / "miniconda_releases"

RELEASE_NOTES_TEMPLATE = SOURCE_DIR / "miniconda_release_notes.rst.jinja2"
RELEASE_NOTES_RST = SOURCE_DIR / "miniconda_release_notes.rst"

FILES_URL = "https://repo.anaconda.com/miniconda/.files.json"


def get_supported_python_versions(miniconda_version, files_info):
    """
    Return python versions found in Miniconda installer
    file names for a particular Miniconda version.
    """
    py_versions = []
    for filename in files_info:
        if not f"_{miniconda_version}-" in filename or "py" not in filename:
            continue
        py_intermediate = filename.split("py")[1]
        py_version = py_intermediate.split("_")[0]
        py_version = f"{py_version[0]}.{py_version[1:]}"
        if py_version not in py_versions:
            py_versions.append(py_version)
    return sorted(py_versions, key=Version, reverse=True)


def get_package_list(dists: list[str]) -> list[dict[str, str]]:
    #  The `dist` strings are of the format "<name>-<version>-<hash>_<build_num>.conda"
    packages = []
    for dist in dists:
        if dist.startswith("_"):
            continue
        pkg_name, pkg_version, pkg_split = dist[:-6].rsplit("-", 2)
        pkg_hash, pkg_build_num = pkg_split.split("_")
        package = {
            "name": pkg_name,
            "version": pkg_version,
            "hash": pkg_hash,
            "build_num": pkg_build_num
        }
        packages.append(package)
    return packages


def get_installer_info(release: Path, files_info: dict) -> dict:
    """
    Process _info.json files output by constructor to get installer information,
    including the list of delivered packages
    """

    NOTES_FILE = release / "changes.rst"
    notes_text = NOTES_FILE.read_text(encoding="utf-8")

    miniconda_version = release.name
    installer_info = {
        "version": miniconda_version,
        "python_versions": get_supported_python_versions(miniconda_version, files_info),
        "package_lists": {},
        "release_date": "",
        "notes": notes_text, # user-facing changes, bug fixes, known issues
    }

    # Get list of packages
    for info_json in release.iterdir():
        if not info_json.name.endswith("_info.json"):
            continue
        info_dict = json.loads(info_json.read_text())
        platform = info_dict["_platform"]
        if platform in installer_info:
            continue
        installer_info["package_lists"][platform] = get_package_list(info_dict["_dists"])

    # Get release date
    for filename, data in files_info.items():
        if f"_{miniconda_version}-" in filename:
            mtime = data["mtime"]
            date = datetime.datetime.fromtimestamp(mtime)
            installer_info["release_date"] = date.strftime("%B %-d, %Y")
            break

    return installer_info


def main():
    with urllib.request.urlopen(url=FILES_URL) as f:
        files_info = json.loads(f.read().decode("utf-8"))

    release_info = []
    releases = sorted([release.name for release in RELEASE_DIR.iterdir()], reverse=True, key=Version)
    for release in releases:
        release_info.append(get_installer_info(RELEASE_DIR / release, files_info))
    
    with open(RELEASE_NOTES_TEMPLATE) as f:
        template_text = f.read()
    
    template = Template(template_text)
    rst_text = template.render(release_info=release_info)

    with open(RELEASE_NOTES_RST, "w") as f:
        f.write(rst_text)
    

if __name__ == "__main__":
     main()

