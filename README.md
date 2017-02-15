# Conda documentation


This repository includes documentation for all of conda, including
conda-build.

The website is at https://conda.io/ and the docs are at https://conda.io/docs/.

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

    conda create -n conda-docs python=3 sphinx sphinx_rtd_theme numpydoc
    source activate conda-docs
    conda install -c asmeurer help2man man2html

Furthermore you will need to have conda-build installed to generate the help
pages for the conda-build commands.

    conda install -n root conda-build pycrypto

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

The site https://conda.io points to the GitHub pages of this repo.
