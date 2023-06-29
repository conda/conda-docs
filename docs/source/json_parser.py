import os
import json

ROOT_DIR = os.getcwd()
SOURCE_DIR = os.path.join(ROOT_DIR, "docs/source/")
OUT_FILEPATH = os.path.join(SOURCE_DIR, "release_notes.rst.jinja2")

# def get_info_json():
info_json_file_path = os.path.join(SOURCE_DIR, "_tmp/", "info.json")
info_json_dict = {}
pkg_list = []
pkg_dict = {}
with open(info_json_file_path) as f:
    info_json_raw = json.load(f)
    info_json_dict["name"] = info_json_raw["name"]
    info_json_dict["version"] = info_json_raw["version"]
    info_json_dict["installer_type"] = info_json_raw["installer_type"]
    info_json_dict["platform"] = info_json_raw["_platform"]
    # info_json_dict[pkg_list]["pkgs"] = info_json_raw["_dists"]

for dist in info_json_raw["_dists"]:
    separator = '-'
    pkg = dist.rsplit(separator, 1)[0]
    # pkg_split = pkg.rsplit(separator, 1)
    # pkg_list.append(pkg)

    # pkg_name_list = []
    # pkg_version_list = []

    pkg_name = pkg.rsplit(separator, 1)[0]
    pkg_version = pkg.rsplit(separator, 1)[1]

    # pkg_name_list.append(pkg_name)
    # pkg_version_list.append(pkg_version)

    pkg_list.append(pkg_name + " " + pkg_version)

for pkg in pkg_list:
    print("* " + pkg)



# get_info_json()
# print(new_pkg_list)
print(pkg_name_list)
print(pkg_version_list)
breakpoint()