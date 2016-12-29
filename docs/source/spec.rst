Conda package specification
===========================

.. contents::

A conda package is a bzipped tar archive (``.tar.bz2``) which contains
metadata under the ``info/`` directory, and a collection of files which are
installed directly into an install prefix.  The format is identical across
platforms and operating systems.  It is important to note that during the
install process, all files are basically just extracted into the install
prefix, with the exception of the ones in ``info/``.  Installing a conda
package into an environment may be roughly thought of as executing the
following command::

   $ cd <environment prefix>
   $ tar xjf some-package-1.0-0.tar.bz2

However, it should be noted that only files (including symbolic
links) are part of a conda package, and not directories.  Directories
are created and removed as needed, but you cannot create an empty directory
from the tar archive directly.

In the following, we describe the precise layout of the metadata contained in
the ``info/`` directory and how it relates to the repository index
(``repodata.json.bz``).

.. _package_metadata:

Package metadata
----------------

All metadata about a package is contained under ``info/``.  Files within this location are not installed under the install prefix. Though a package creator is free to add any file, conda will only inspect the content of the following files:

``info/index.json``: This file contains basic information about the package,
such as name, version, build string, and dependencies.  The content of this
file is what gets stored in the repository index file ``repodata.json`` (hence
the name ``index.json``).  The json object is a dictionary containing the
following keys:

   ``name``: string
      The (lowercase) name of the package.  Note that this string
      may contain the ``-`` character.

   ``version``: string
      The package version, which may not contain ``-``.
      Conda acknowledges `PEP 440 <https://www.python.org/dev/peps/pep-0440/>`_.

   ``build``: string
      The build string, which also may not contain ``-``.
      The filename of the conda package is composed from these
      three values, that is ``<name>-<version>-<build>.tar.bz2``.

   ``build_number``: integer
      A (non-negative) integer representing the build
      number of the package.

   ``depends``: list of strings
      List of dependency specifications, where each element is a string
      as outlined in :ref:`build-version-spec`.

   ``arch``: string (optional)
      The architecture the package is built for, e.g. ``x86_64``.
      Conda currently does not do anything with this key.

   ``platform``: string (optional)
      The platform (OS) the package is built for, e.g. ``osx``.
      Conda currently does not do anything with this key.  Packages for a
      specific architecture and platform are usually distinguished by the
      repository sub-directory they are contained in (see below).

The build string is used to differentiate builds of packages with otherwise
the same name and version, e.g. a build with other dependencies (like Python
3.4 instead of Python 2.7), a bug fix in the build process, or some different
optional dependencies (MKL vs. ATLAS linkage), etc.  Nothing in conda actually
inspects the build string---strings such as ``np18py34_1`` are only
designed for human readability, but are never parsed by conda.

Unlike the build string, the build number is inspected by conda.
It is used to sort packages (with otherwise same name and version) to
determine the latest one.
This is important, because new builds (bug fixes to the way a package is
build) may be added to a repository.

``info/files``: This file lists all files which are part of the package
itself (one per line), i.e. all files which need to get linked into the
environment.  Any files in the package not listed in this file will not be
linked when the package is installed.  The directory delimiter for the files
in ``info/files`` should always be ``/``, even on Windows.  This matches the
directory delimiter used in the tarball.

``info/has_prefix``: This optional file lists all files that contain a
hard-coded build prefix or placeholder prefix, which needs to be replaced by
the install prefix at installation time. Note that due to the way the binary
replacement works, the placeholder prefix must be longer than the install
prefix.

Each line of this file should either be a path, in which case it is considered
a text file with the default placeholder, ``/opt/anaconda1anaconda2anaconda3``,
or a space-separated list of ``placeholder``, ``mode``, ``path``, where
``placeholder`` is the build or placeholder prefix, ``mode`` is either ``text``
or ``binary``, and ``path`` is the relative path of the file to be updated. For
instance, on Linux or OS X

::

   bin/script.sh
   /Users/username/anaconda/envs/_build binary bin/binary
   /Users/username/anaconda/envs/_build text share/text

or on Windows

::

  "Scripts/script1.py"
  "C:\Users\username\anaconda\envs\_build" text "Scripts/script2.bat"
  "C:/Users/username/anaconda/envs/_build" binary "Scripts/binary"

Note the directory delimiter for the relative ``path`` must always be ``/``,
even on Windows. The placeholder may contain either ``\`` or ``/`` on Windows;
the replacement prefix will match the delimiter used in the placeholder. (The
default placeholder ``/opt/anaconda1anaconda2anaconda3`` is an exception, being
replaced with the install prefix using the native path delimiter.) On Windows,
the ``placeholder`` and ``path`` always appear in "quotes" to support paths
with spaces.

``info/license.txt``: This optional file is the software license for the package.

``info/no_link``: This optional file lists all files which cannot be linked
(either soft or hard) into environments, and are copied instead.

``info/about.json``: This optional file contains the entries in the :ref:`about` section
of :doc:`./building/meta-yaml` file. The following keys will be added to ``info/about.json``
if present in the build recipe

::

  home
  dev_url
  doc_url
  license_url
  license
  summary
  description
  license_family

``info/recipe``: This directory will contain the full contents of the build recipe.

    ``meta.yaml.rendered``: This is the fully rendered build recipe. See :doc:`../commands/build/conda-render`.

    This directory is only present when the the ``include_recipe`` flag is true in the :ref:`meta-build`.

``info/paths.json``: This file contains basic information about each file contained in the package.
It appeared in conda 4.3 and is intended to replace ``info/files``, ``info/has_prefix``, and
``info/no_link``.
The json object is a dictionary with two keys, ``paths_version``,
which holds the file format version (currently 1)
and ``paths``, which contains a list with one dictionary per file.
The per-file dictionary contains the following keys:

   ``_path``: string
      The path to the file.

   ``sha256``: string
      The SHA-256 checksum of the file.

   ``size_in_bytes``: int
      The size of the files in number of bytes.

   ``path_type``: string
      The type of link. Could be ``hardlink``, ``softlink``, or ``directory``.

   ``no_link``: boolean
      Is set to ``True`` for files that cannot be linked (either soft or hard)
      into environments, and are copied instead.

   ``prefix_placeholder``: string (optional)
      Hard coded prefix placeholder in the file. The default prefix placeholder is
      ``/opt/anaconda1anaconda2anaconda3``, but others may be used.

   ``file_mode``: string (optional)
      Whether the file is a binary file or text file. Could be ``text`` or ``binary`` (default).
      Primarily used in conjunction with ``prefix_placeholder``, in order to determine
      how that prefix placeholder is to be replaced.

   ``inode_paths``: list of strings (optional)
      List of other files which share the same inode (i.e. they are hard links).




Link and unlink scripts
------------------------

A couple of scripts may optionally be executed before and after the link
and unlink step.  These scripts are executed in a subprocess by conda,
using ``/bin/bash <script>`` on Unix and ``%COMSPEC% /c <script>`` on
Windows.  For this to work, there needs to be a convention for the path and
filenames of these scripts.  On Unix we have ``bin/.<name>-<action>.sh``,
and on Windows ``Scripts/.<name>-<action>.bat``, where ``<name>`` is the
package name, and ``<action>`` is one of the following:

``pre-link``: executed prior to linking, an error causes conda to stop.

``post-link``: executed after linking, when the post-link step fails,
we don't write any package metadata and return here.  This way the package
is not considered installed.

``pre-unlink``: executed prior to unlinking, errors are ignored.

For example, when there is a script named ``/bin/.foo-post-link.sh`` in the
package ``foo-1.0-0.tar.bz2``, it is executed after the linking is completed.
Moreover, the following environment variables are set while the script is
being executed: ``PREFIX``, ``PKG_NAME``, ``PKG_VERSION``


Repository structure and index
------------------------------

A conda repository (or channel) is a directory tree, usually served over
HTTPS, which has platform sub-directories, each of which contain conda
packages and a repository index.  The index file ``repodata.json`` lists all
conda packages in the platform sub-directory.  The command ``conda index`` can
be used to create such an index from the conda packages within a directory.
It is simple mapping of the full conda package filename to the dictionary
object in ``info/index.json`` described in the previous section.

In the following example, a repository provides the conda package
``misc-1.0-np17py27_0.tar.bz2`` on 64-bit Linux and 32-bit Windows::

   <some path>/linux-64/repodata.json
                        repodata.json.bz2
                        misc-1.0-np17py27_0.tar.bz2
              /win-32/repodata.json
                      repodata.json.bz2
                      misc-1.0-np17py27_0.tar.bz2

Note that both conda packages have identical filenames, and are only
distinguished by the repository sub-directory they are contained in.

.. _build-version-spec:

Package match specifications
----------------------------

Note that this is not the same as the syntax used at the command line with
conda install (like ``conda install python=3.4``). Internally, conda
translates the command line syntax to the spec defined below (for example,
``python=3.4`` is translated to ``python 3.4*``).

Package dependencies are specified using a match specification.  A match
specification a space separated string of 1, 2 or 3 parts:

* The first part is always the (exact) name of the package.
* The second part refers to the version, and may contain special
  characters.

  ``|`` means "or", e.g. ``1.0|1.2`` matches either version 1.0 or 1.2

  ``*`` matches zero or more characters in the version string. In terms of
  regular expressions, it is the same as ``r'.*'``.

  For example, ``1.0|1.4*``  matches 1.0, 1.4, 1.4.1b2, but not 1.2

  ``<``, ``>``, ``<=``, ``>=``, ``==`` and ``!=`` are relational operators on
  versions, which are compared using [PEP
  440](https://www.python.org/dev/peps/pep-0440/).  For example, ``<=1.0``
  matches ``0.9``, ``0.9.1``, and ``1.0``, but not ``1.0.1``. ``==`` and
  ``!=`` are exact equality,

  ``,`` means "and", e.g., ``>=2,<3`` matches all packages in the "2" series,
  e.g., ``2.0``, ``2.1``, and ``2.9`` all match, but ``3.0`` and ``1.0`` do
  not.

  ``,`` has higher precedence than ``|``, i.e., ``>=1,<2|>3`` means "(greater
  than or equal to 1 and less than 2) or (greater than 3)," which matches
  ``1``, ``1.3``, and ``3.0``, but not ``2.2``.

  Conda parses the version by splitting it into parts separated by ``|``. If
  the part begins with ``<``, ``>``, ``=``, or ``!``, it is parsed as a
  relational operator. Otherwise, it is parsed as a version, possibly
  containing the ``*`` operator.

* The third part is always the (exact) build string.  When there are 3
  parts, the second part has to be the exact version.

Remember that the version specification cannot contain spaces, as spaces are
used to delimit the package, version, and build string in the whole match
specification. ``python >= 2.7`` is an invalid match
specification. Furthermore, ``python>=2.7`` will be matched as any version of
a package named "python>=2.7".

Examples
~~~~~~~~

The following are all valid match specifications for numpy-1.8.1-py27_0:

- ``numpy``
- ``numpy 1.8*``
- ``numpy 1.8.1``
- ``numpy >=1.8``
- ``numpy ==1.8.1``
- ``numpy 1.8|1.8*``
- ``numpy >=1.8,<2``
- ``numpy >=1.8,<2|1.9``
- ``numpy 1.8.1 py27_0``
- ``numpy=1.8.1=py27_0``
