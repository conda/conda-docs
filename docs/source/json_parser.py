import json
from pathlib import Path
from jinja2 import Template

SOURCE_DIR = Path(__file__).parent
RELEASE_DIR = SOURCE_DIR / "miniconda_releases"
RELEASE_NOTES_TEMPLATE = SOURCE_DIR / "miniconda_release_notes.rst.jinja2"
RELEASE_NOTES_RST = SOURCE_DIR / "miniconda_release_notes.rst"

def get_installer_info(release: Path) -> dict:
    """
    Process _info.json files output by constructor to get installer information,
    including the list of delivered packages
    """
    def get_package_list(dists: list[str]) -> list:
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

    installer_info = {}
    for info_json in release.iterdir():
        if not info_json.name.endswith("_info.json"):
            continue
        info_dict = json.loads(info_json.read_text())
        info_dict["packages"] = get_package_list(info_dict["_dists"])
        platform = info_dict["_platform"]
        installer_type = info_dict["installer_type"]
        installer_info[platform,installer_type] = info_dict

    return installer_info


def main():
    release_info = {}
    for release in RELEASE_DIR.iterdir():
        release_info[release.name] = get_installer_info(release)

    with open(RELEASE_NOTES_TEMPLATE) as f:
        template_text = f.read()
    
    template = Template(template_text)
    rst_text = template.render(**release_info)
    with open(RELEASE_NOTES_RST, "w") as f:
        f.write(rst_text)

if __name__ == "__main__":
     main()