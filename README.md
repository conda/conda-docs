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

    conda create -n conda-docs -c asmeurer conda-docs-deps python=3

Furthermore you will need to have conda-build installed to generate the help
pages for the conda-build commands.

    conda install -n root conda-build pycrypto

Unfortunately the conda-docs-deps package is not available for Windows because
we do not have a conda package for perl on Windows yet.

(2016 Aug 24 note from Will Warner: Dave Mertz discovered and I confirmed that creating a new conda-docs environment according to the instructions installs six=1.3.0 from channel asmeurer and 'make html' fails with a UserString error. 'conda install -n conda-docs six=1.10' installs 1.10.0 from default channels and then 'make html' works. I need to update the package conda-docs-deps so it works out of the box and then update this README to remove this work around. Tracked in https://github.com/ContinuumIO/docs/issues/399 .

Also TravisCI was failing on a line of code 'default=config.prefix_length', with the error 'AttributeError: 'Config' object has no attribute 'prefix_length''. Michael Sarahan explained that it was a conda-build bug and should be worked around by editing .travis.yml to use 'conda-build=1.21.11' instead of 'conda-build', which I did, and when a new release of conda-build is made without the bug, I need to change it back to 'conda-build'. Michael S says conda-build 2.0 will likely be released sometime soon after Monday, 2016 Aug 29.)

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
