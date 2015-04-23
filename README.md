# Conda documentation


This repository includes documentation for all of conda, including
conda-build.

The website is at http://conda.pydata.org/ and the docs are at http://conda.pydata.org/docs/.

Feel free to make pull requests against this repo for suggested changes. All
changes are welcome, from typo fixes to new documents to refactoring.

## Website

You will need to

    conda create -n conda-website -c asmeurer sphinxjp.themes.basicstrap cloud_sptheme

Use

    source activate conda-website
    cd web
    make html

to build the site.  The result will be in web/build/html.

To check that the links are correct, use

    make linkcheck

## Docs

The docs have several dependencies. You can install them all with

    conda create -n conda-docs -c asmeurer conda-docs-deps python=3

Furthermore you will need to have conda-build installed to generate the help
pages for the conda-build commands.

    conda install -n root conda-build

Unfortunately the conda-docs-deps package is not available for Windows because
we do not have a conda package for perl on Windows yet.

Then run

    source activate conda-docs
    cd docs
    make html

The result will be in docs/build/html.

To skip the generation of command docs (much faster), run

    make just-html

## Deploying

The website and docs are deployed automatically to GitHub pages (the
`gh-pages` branch on this repo) with Travis CI when commits are pushed to
master. Travis will build docs on pull requests to make sure there are no
build warnings or errors, but it only deploys it on master.

The site http://conda.pydata.org points to the GitHub pages of this repo.
