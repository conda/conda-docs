********************************
Channels and generating an index
********************************

Channel layout
--------------

.. code-block:: bash

  .
  ├── channeldata.json
  ├── linux-32
  |   ├── repodata.json
  │   └── package-0.0.0.tar.bz2
  ├── linux-64
  |   ├── repodata.json
  │   └── package-0.0.0.tar.bz2
  ├── win-64
  |   ├── repodata.json
  │   └── package-0.0.0.tar.bz2
  ├── win-32
  |   ├── repodata.json
  │   └── package-0.0.0.tar.bz2
  ├── osx-64
  |   ├── repodata.json
  │   └── package-0.0.0.tar.bz2
  ...

Parts of a channel
------------------

* Channeldata.json contains metadata about the channel, including:

    - What subdirs the channel contains.
    - What packages exist in the channel and what subdirs they are in.

* Subdirs are associated with platforms. For example, the linux-64 subdir contains
  packages for linux-64 systems.

* Repodata.json contains an index of the packages in a subdir. Each subdir will
  have it's own repodata.

* Channels have packages as tarballs under corresponding subdirs.

channeldata.json
----------------

.. code-block:: bash

  {
    "channeldata_version": 1,
    "packages": {
      "super-fun-package": {
        "activate.d": false,
        "binary_prefix": false,
        "deactivate.d": false,
        "home": "https://github.com/Home/super-fun-package",
        "license": "BSD",
        "post_link": false,
        "pre_link": false,
        "pre_unlink": false,
        "reference_package": "win-64/super-fun-package-0.1.0-py37_0.tar.bz2",
        "run_exports": {},
        "subdirs": [
          "win-64"
        ],
        "summary": "A fun package! Open me up for rainbows",
        "text_prefix": false,
        "version": "0.1.0"
      },
      "subdirs": [
        "win-64",
        ...
      ]
  }

repodata.json
-------------

.. code-block:: bash

  {
    "packages": {
      "super-fun-package-0.1.0-py37_0.tar.bz2": {
        "build": "py37_0",
        "build_number": 0,
        "depends": [
          "some-depends"
        ],
        "license": "BSD",
        "md5": "a75683f8d9f5b58c19a8ec5d0b7f796e",
        "name": "super-fun-package",
        "sha256": "1fe3c3f4250e51886838e8e0287e39029d601b9f493ea05c37a2630a9fe5810f",
        "size": 3832,
        "subdir": "win-64",
        "timestamp": 1530731681870,
        "version": "0.1.0"
      },
      ...
    }

How an index is generated
-------------------------

For each subdir:

* Look at all the packages that exist in the subdir.

* Generate a list of packages to add/update/remove.

* Remove all packages that need to be removed.

For all packages that need to be added/updated:

  * Extract the package to access metadata including full package name,
    mtime, size, and index.json.

  * Aggregate package metadata to repodata collection.

* Apply repodata hotfixes (patches).

* Compute and save the reduced `current_index.json` index.

Example: Building a channel
---------------------------

To build a local channel and put a package in it, follow the directions below.

#. Make the channel structure.

    .. code-block:: bash

      $ mkdir local-channel
      $ cd local-channel
      $ mkdir linux-64 osx-64

#. Put your favorite package in the channel.

    .. code-block:: bash

      $ wget https://anaconda.org/anaconda/scipy/1.1.0/download/linux-64/scipy-1.1.0-py37hfa4b5c9_1.tar.bz2 -P linux-64
      $ wget https://anaconda.org/anaconda/scipy/1.1.0/download/osx-64/scipy-1.1.0-py37hf5b7bf4_0.tar.bz2 -P osx-64

#. Run a conda index. This will generate both channeldata.json for the channel and
   repodata.json for the linux-64 and osx-64 subdirs, along with some other files.

    .. code-block:: bash

      $ conda index .

#. Check your work by searching the channel.

    .. code-block:: bash

      $ conda search -c file:/<path to>/local-channel scipy | grep local-channel


More details behind the scenes
------------------------------

Caching package metadata
~~~~~~~~~~~~~~~~~~~~~~~~

Caching utilizes the existing repodata.json file if it exists. Indexing checks
which files to update based on which files are new, removed, or changed since
the last repodata.json was created. When a package is new or changed, its
metadata is extracted and cached in the subdir to which the package belongs. The
subfolder is the `.cache` folder. This folder has one file of interest:
`stat.json`, which contains results from the `stat` command for each file. This
is used for understanding when a file has changed and needs to be updated. In
each of the other subfolders, the extracted metadata file for each package is
saved as the original package name, plus a `.json` extension. Having these
already extracted can save a lot of time in fully re-creating the index, should
that be necessary.

An aside: one design goal of the `.conda` package format was to make indexing as
fast as possible. To achieve this, the .conda format separates metadata from the
actual package contents. Where the old `.tar.bz2` container required extracting
the entire package to obtain the metadata, the new package format allows
extraction of metadata without touching the package contents. This allows
indexing speed to be independent of the package size. Large `.tar.bz2` packages
can take a very long time to extract and index.

It is generally never necessary to manually alter the cache. To force an
update/rescan of all cached packages, you can delete the .cache folder, or you
can delete just the `.cache/stat.json` file. Ideally, you could remove only one
package of interest from the cache, but that functionality does not currently
exist.

Repodata patching
~~~~~~~~~~~~~~~~~

Package repodata is bootstrapped from the index.json file within packages.
Unfortunately, that metadata is not always correct. Sometimes a version bound
needs to be added retroactively. The process of altering repodata from the
values derived from package index.json files is called "hotfixing." Hotfixing is
tricky, as it has the potential to break environments that have worked, but it
is also sometimes necessary to fix environments that are known not to work.

Repodata patches generated from a python script
===============================================

On your own server, you're probably fine to run arbitrary python code that you
have written to apply your patches. The advantage here is that the patches are
generated on the fly every time the index is generated. That means that any new
packages that have been added since the patch python file was last committed
will be picked up and will have hotfixes applied to them where appropriate.

Anaconda applies hotfixes by providing a python file to `conda index` that has
logic on how to alter metadata. Anaconda's repository of hotfixes is at
https://github.com/AnacondaRecipes/repodata-hotfixes

Repodata patches applied from a JSON file
=========================================

Unfortunately, you can't always run your python code directly - other people who
host your patches may not allow you to run code. What you can do instead is
package the patches as .json files. These will clobber the entries in the
repodata.json when they are applied.

This is the approach that conda-forge has to take, for example. Their patch
creation code is here:
https://github.com/conda-forge/conda-forge-repodata-patches-feedstock/tree/main/recipe

What that code does is to download the current repodata.json, then runs their
python logic to generate the patch JSON file. Those patches are placed into a
location where Anaconda's mirroring tools will find them and apply them to
conda-forge's repodata.json at mirroring time.

The downside here is that this JSON file is only as new as the last time that
the repodata-patches feedstock last generated a package. Any new packages that
have been added to the index in the meantime will not have any hotfixes applied
to them, because the hotfix JSON file does not know about those files.


Trimming to "current" repodata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The number of packages available is always growing. That means conda is always
having to do more and more work. To slow down this growth, in conda 4.7, we
added the ability to have alternate repodata.json files that may represent a
subset of the normal repodata.json. One in particular is
`current_repodata.json`, which represents:

1. the latest version of each package
2. any earlier versions of dependencies needed to make the latest versions satisfiable

current_repodata.json also keeps only one file type: `.conda` where it is
available, and `.tar.bz2` where only `.tar.bz2` is available.

For Anaconda's defaults "main" channel, the current_repodata.json file is
approximately 1/7 the size of repodata.json. This makes downloading the repodata
faster, and it also makes loading the repodata into its python representation
faster.

For those interested in how this is achieved, please refer to the code at
https://github.com/conda/conda-build/blob/90a6de55d8b9e36fc4a8c471b566d356e07436c7/conda_build/index.py#L695-L737
