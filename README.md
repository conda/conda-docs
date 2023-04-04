# Conda documentation

This repository includes documentation that is common for `conda` and `conda-build`, as well as landing pages for those projects (located at https://docs.conda.io/).

The conda documentation is built using [ReadTheDocs](https://readthedocs.com/). The `conda-docs` repo is the primary project, while `conda` and `conda-build` are created as subprojects. This enables each project's respective documentation to remain in its repo, but for all of the documentation to exist together on the same domain. The landing pages built from the `conda-docs` repo link to the documentation built from the `conda` and `conda-build` repos.

The documentation for each of those individual repositories can be found in their respective repos:

- https://github.com/conda/conda
- https://github.com/conda/conda-build

Please file issues, comments, and pull requests at the appropriate repo.

## Contribution guidelines

### Conda capitalization

You can find information on how to capitalize and talk about conda in the [conda contributing guide](https://github.com/conda/conda/blob/main/CONTRIBUTING.md#conda-capitalization-standards).

### Creating new pages

If you create any new documentation files in this repo, please update the table of contents with the name of your new file. Otherwise, your page will not appear in the table of contents tree on the left-hand side of the documentation. The `toctree` directive for the `conda-docs` repo exists in the `index.rst` file. If you are in the `conda` or `conda-build` repos, there are many `toctree` directives on many `index` files, so make sure you edit the correct one.

## Local builds

You can build this docs repo on your local machine to preview changes in your browser.

NOTE: These steps have only been tested on MacOS.

### Set up and activate a doc build environment

1. Create a conda environment using the supplied requirements file in the `conda-docs` repo.
    ```
    conda create -n conda-docs pip -y
    conda activate conda-docs
    pip install -r requirements.txt
    ```

### Run a local build

1. Go to the `docs` directory.
    ```
    cd docs
    ```

1. Build the HTML docs using the `make` command. The commands used for this are defined in the `docs/Makefile` file.
    ```
    make html
    ```

1. Open the `conda-docs/_build/html` directory in your file manager, locate the desired `.html` file you want to preview, and double-click it to open it in your browser. (You can also drag and drop the file into an open browser.)
