import json
from pathlib import Path

SOURCE_DIR = Path(__file__).parent
info_json_file_path = SOURCE_DIR / "_tmp/" / "info.json"

# To get all data needed for the release notes of one release,
# we need to call `get_installer_information` for every _info.json
# inside the release directory

def get_installer_info(info_json_file_path: Path) -> dict:
    """
    Process _info.json file output by constructor to get installer information,
    including the list of delivered packages
    """
    info_dict = json.loads(info_json_file_path.read_text())    
    info_dict["packages"] = [dist_str_to_dict(x) for x in info_dict["_dists"]]

    return info_dict


def dist_str_to_dict(dist: str) -> dict:
        #  The `dist` strings are of the format "<name>-<version>-<hash>_<build_num>.conda"

        pkg_name, pkg_version, pkg_split = dist[:-6].rsplit("-", 2)
        pkg_hash = pkg_split.split("_")[0]
        pkg_build_num = pkg_split.split("_")[1]

        return {
            "name": pkg_name,
            "version": pkg_version,
            "hash": pkg_hash,
            "build_num": pkg_build_num
        }

def main():
    print(get_installer_info(info_json_file_path))

if __name__ == "__main__":
     main()