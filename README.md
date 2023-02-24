# Conda documentation

This repository includes documentation that is common for `conda` and `conda-build` (primarily landing pages at https://conda.io/).

The documentation for each of those individual repositories can be found in their respective repos:

- https://github.com/conda/conda
- https://github.com/conda/conda-build

Please file issues, comments, and PRs at the appropriate repo.

## Local builds

You can build this docs repo on your local machine to preview changes in your browser.

NOTE: These steps have only been tested on MacOS

### Set up and activate a `sphinx` environment

1. If you haven't already, create a conda environment with `sphinx` installed.
    ```
    conda create -n sphinx sphinx
    ```

1. Activate the environment.
    ```
    conda activate sphinx
    ```

### Run a local build

1. Go to the `docs` directory.
    ```
    cd docs
    ```

1. Create a `_build` directory.
    ```
    mkdir _build
    ```

1. Run this command.
    ```
    sphinx-build -b html -d _build/doctrees source _build/html
    ```

1. Open the `_build/html` directory in Finder, locate the desired `.html` file you want to preview, and open it in your browser (you can just drag and drop it into your browser, if it's open).
