import os
import json
from bs4 import BeautifulSoup
import requests
from datetime import datetime

ROOT_DIR = os.getcwd()
SOURCE_DIR = os.path.join(ROOT_DIR, "docs/source/")
OUT_FILEPATH = os.path.join(SOURCE_DIR, "release_notes.rst")
info_json_file_path = os.path.join(SOURCE_DIR, "_tmp/", "info.json")

repo_url = 'https://repo.anaconda.com/miniconda/'
response = requests.get(repo_url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

pkg_list = []
pkg_dict = {}


# This loads all the data from the info.json
with open(info_json_file_path) as f:
    info_json_raw = json.load(f)

# This creates a list of all the pkgs
for dist in info_json_raw["_dists"]:
    separator = '-'
    pkg = dist.rsplit(separator, 1)[0]

    pkg_name = pkg.rsplit(separator, 1)[0]
    pkg_version = pkg.rsplit(separator, 1)[1]

    pkg_list.append(pkg_name + " " + pkg_version)


# This loads the info(table) from repo.anaconda.com/miniconda
table = soup.find('table')
row_three = table.find_all('tr')[2]
for cell in row_three:
    filename = row_three.find_all('td')[0].text
    size = row_three.find_all('td')[1].text
    time = row_three.find_all('td')[2].text
    sha256 = row_three.find_all('td')[3].text


# This is a section for rst symbols
def rst_equals(var):
    rst_equals = "="*(len(var))
    print(rst_equals + "\n" + var + "\n" + rst_equals + "\n\n")

def rst_dashes(var):
    rst_dashes = "-"*(len(var) + 1)
    print(var + "\n" + rst_dashes + "\n\n")

def rst_carets(var):
    rst_carets = "^"*(len(var) + 2)
    print(var + "\n" + rst_carets + "\n\n")

# lineBreak = print("\n\n")

# This section creates the title and headings in rst format

def create_heading(name, version, release_date):
    title = "Release Notes"

    name = info_json_raw["name"]
    version = info_json_raw["version"]

    date = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    release_date = date.strftime("(%B %d, %Y)")

    heading = f'{info_json_raw["name"]} {info_json_raw["version"]} {release_date}'

    return rst_equals(title), rst_dashes(heading)

# This is a placeholder for the ufc, bf, and pv lists/info
ufc_list = ["change 1", "change 2", "change 3"]
bf_list = ["bug 1", "bug 2", "bug 3"]
pv_list = ["3.8", "3.9", "3.10", "3.11"]

# This section is for the subheadings
def user_facing_changes(list):
    title = "User-facing Changes"
    print(rst_carets(title))
    for i in list:
        print("* " + i)
    print("\n")

def bug_fixes(bf_list: list):
    title = "Bugs Fixed"
    print(rst_carets(title))
    for i in bf_list:
        item = print("* " + i)
    print("\n")

def python_versions(list):
    # Space holder for how to retrieve python variants
    print("**Available Python Versions: **")
    print(*list, sep = ", ")
    print("\n")

def format_pkg_list(pkg_list: list):
    print("**Packages:**\n")
    for pkg in pkg_list:
        print("* " + pkg)
    print("\n")

def main():
    """The purpose of this is to generate the release notes for miniconda in rst.jinja2 format.
    The JSON files used to extract the package list info will live in the <miniconda> directory.
    The output will include the installer's name, version, user-facing changes, bug fixes, and a list of all the existing packages."""
    heading = str(create_heading(info_json_raw['name'], info_json_raw['version'], time))
    ufc = str(user_facing_changes(ufc_list))
    bf = str(bug_fixes(bf_list))
    pv = str(python_versions(pv_list))
    fpl = str(format_pkg_list(pkg_list))
    with open(OUT_FILEPATH, 'w') as f:
        f.write(heading)
        f.write(ufc)
        f.write(bf)
        f.write(pv)
        f.write(fpl)

if __name__ == '__main__':
    main()
