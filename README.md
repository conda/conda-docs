# Conda documentation

This repository includes documentation for all of conda, including
conda-build and conda-docs.

The website is at http://conda.pydata.org/ and the documentation is at http://conda.pydata.org/docs/.

Feel free to make pull requests against this repo for suggested changes. All
changes are welcome, from typo fixes to new documents to refactoring.

## Website

You will need to:

    conda create -n conda-website -c asmeurer sphinxjp.themes.basicstrap cloud_sptheme

To build the site, use:

    source activate conda-website
    cd web
    make html

The result will be in web/build/html.

To check that the links are correct, use:

    make linkcheck

## Docs

The documentation has several dependencies. Linux or Macintosh is recommended
-- the conda-docs-deps package is not available for Windows because
we do not have a conda package for perl on Windows.

Install conda. See instructions on docs website.

Then install documentation and dependencies:

    conda create -n conda-docs -c asmeurer conda-docs-deps python=3
    
After editing files, test in browser by inserting this URL
in front of the Github URL: http://rawgit.com/

To check that the links are correct, use:

    make linkcheck
    
Before you generate documentation for the first time, install conda-build:

    conda install -n root conda-build pycrypto

To generate documentation but skip the generation of command docs (much faster), run:

    make just-html

To generate the documentation and all the help pages for the conda-build commands, run:

    source activate conda-docs
    cd docs
    make html

The result will be in docs/build/html.

## Deploying

The website and docs are deployed automatically to GitHub pages (the
`gh-pages` branch on this repo) with Travis CI when commits are pushed to
master. Travis will build docs on pull requests to make sure there are no
build warnings or errors, but it only deploys it on master.

The site http://conda.pydata.org points to the GitHub pages of this repo.
