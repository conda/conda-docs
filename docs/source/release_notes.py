import os
import json
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

ROOT_DIR = os.getcwd()
SOURCE_DIR = os.path.join(ROOT_DIR, "docs/source/")
OUT_FILEPATH = os.path.join(SOURCE_DIR, "release_notes.rst.jinja2")
info_json_file_path = os.path.join(SOURCE_DIR, "_tmp/", "info.json")

repo_url = 'https://repo.anaconda.com/miniconda/'
response = requests.get(repo_url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

info_json_dict = {}
pkg_list = []


# This loads all the data from the info.json
with open(info_json_file_path) as f:
    info_json_raw = json.load(f)
    info_json_dict["name"] = info_json_raw["name"]
    info_json_dict["version"] = info_json_raw["version"]
    info_json_dict["installer_type"] = info_json_raw["installer_type"]
    info_json_dict["platform"] = info_json_raw["_platform"]


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


# This section creates the title and headings in rst format

def create_heading(name, version, release_date):
    title = "Release Notes"

    name = info_json_dict["name"]
    version = info_json_dict["version"]

    date = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    release_date = date.strftime("(%B %d, %Y)")

    print(rst_equals(title))
    heading = print(name.uppercase(), version, release_date)

    print(rst_dashes = "-"*(len(var) + 1))









#     timestamp = pd.to_datetime(time)
#     # try:
#     datestamp = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
#     # except ValueError as ve1:
#     #     print('ValueError 1:', ve1)
#     global date
#     date = datestamp.strftime("(%B %d, %Y)")
#     # return date
#     #     for row in rows:
#     #         filename = row.find('td')[0].text
#     #         print(filename)
#     #     return rows
#         # for data in cell.find_all('td'):
#         #     cell_text = data.get_text()
#         #     print(cell_text)

#     heading = print(name, version, date)


for pkg in pkg_list:
    print("* " + pkg)


def main():
    """The purpose of this is to generate the release notes for miniconda in rst.jinja2 format.
    The JSON files used to extract the package list info will live in the <miniconda> directory.
    The output will include the installer's name, version, user-facing changes, bug fixes, and a list of all the existing packages."""
    create_title("Release Notes")


if __name__ == '__main__':
    main()
