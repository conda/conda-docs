===================
Conda documentation
===================

This repository includes documentation for all of conda, including
conda-build.

The website is at http://conda.pydata.org/ and the docs are at http://conda.pydata.org/docs/.

Feel free to make pull requests against this repo for suggested changes. All
changes are welcome, from typo fixes to new documents to refactoring.

Website
=======

You will need to

    conda install -c asmeurer sphinxjp.themes.basicstrap cloud_sptheme

Use

    make html

to build the site.  The result will be in web/build/html.

To check that the links are correct, use

    make linkcheck

Docs
====

The docs have several dependencies. You can install them all with

    conda install -c asmeurer conda-docs-deps

Then run

    make html

The result will be in docs/build/html.

Deploying
=========

The website and docs are deployed automatically to GitHub pages (the
`gh-pages` branch on this repo) with Travis CI when commits are pushed to
master. Travis will build docs on pull requests to make sure there are no
build warnings or errors, but it only deploys it on master.

The site http://conda.pydata.org points to the GitHub pages of this repo.
