import json
from pathlib import Path

SOURCE_DIR = Path(__file__).parent
RELEASE_DIR = SOURCE_DIR / "miniconda_releases"


def get_installer_info(release: Path) -> dict:
    """
    Process _info.json files output by constructor to get installer information,
    including the list of delivered packages
    """
    def get_package_list(dists: list[str]) -> list:
        #  The `dist` strings are of the format "<name>-<version>-<hash>_<build_num>.conda"
        packages = []
        for dist in dists:
            pkg_name, pkg_version, pkg_split = dist[:-6].rsplit("-", 2)
            pkg_hash = pkg_split.split("_")[0]
            pkg_build_num = pkg_split.split("_")[1]
    
            package = {
                "name": pkg_name,
                "version": pkg_version,
                "hash": pkg_hash,
                "build_num": pkg_build_num
            }
            packages.append(package)
        return packages

    installer_info = {}
    for info_json in release.iterdir():
        if not info_json.name.endswith("_info.json"):
            continue
        info_dict = json.loads(info_json.read_text())
        info_dict["packages"] = get_package_list(info_dict["_dists"])
        platform = info_dict["_platform"]
        py_version = info_dict["version"].split("_")[0]
        installer_type = info_dict["installer_type"]
        installer_info[platform,py_version,installer_type] = info_dict

    return installer_info


def main():
    release_info = {}
    for release in RELEASE_DIR.iterdir():
        release_info[release.name] = get_installer_info(release)
    print(release_info)

if __name__ == "__main__":
     main()