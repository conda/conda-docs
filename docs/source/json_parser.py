import os
import json

ROOT_DIR = os.getcwd()
SOURCE_DIR = os.path.join(ROOT_DIR, "docs/source/")
OUT_FILEPATH = os.path.join(SOURCE_DIR, "parsed_info.json")
info_json_file_path = os.path.join(SOURCE_DIR, "_tmp/", "info.json")

with open(info_json_file_path) as f:
    info_json_raw = json.load(f)

def dist_str_to_dict(dist: str) -> dict:
        pkg = dist.rsplit('-', 2)
        pkg_split = pkg[2].split('_')

        pkg_name = pkg[0]
        pkg_version = pkg[1]
        pkg_hash = pkg_split[0]
        pkg_build_num = pkg_split[1].split('.')[0]
        pkg_ext = pkg_split[1].split('.')[1]
    
        return {"name": pkg_name, "version": pkg_version, "hash": pkg_hash, "build_num": pkg_build_num, "ext": pkg_ext}

def dict_to_list_of_dicts(dists: list) -> list:
    pkg_list_infos = [dist_str_to_dict(x) for x in dists]
    return pkg_list_infos

def main():
     with open(OUT_FILEPATH, 'w') as f:
        f.write(str(dict_to_list_of_dicts(info_json_raw["_dists"])))

if __name__ == '__main__':
     main()