============
Introduction
============

Conda is a cross-platform, Python-agnostic binary package manager. Conda can:

- `Search <commands/conda-search.html>`_ for packages in a repository/package
  index/channel or a current installation.
- `Create <commands/conda-create.html>`_ conda environments.
- `Install <commands/conda-install>`_ and `update <conda-update.html>`_
  packages into new and existing environments.


Conda Overview
--------------

.. _package:
.. index::
    pair: terminology; package

.. _environment:
.. index::
    pair: terminology; environment


Packages
~~~~~~~~

A conda `package` is a binary archive (tarball) containing system-level
libraries, Python modules, executable programs, or other components. Conda
keeps track of dependencies between packages and platform specifics, making it
simple to install sets of packages.


Environments
~~~~~~~~~~~~

A `conda environment` is a filesystem directory that contains a specific
collection of conda packages.  As a concrete example, you might want to
have one environment that provides NumPy 1.7, and another environment that
provides NumPy 1.6 for legacy testing.  conda makes this kind of mixing
and matching easy.  To begin using an environment, simply set
your **PATH** variable to point to its `bin` directory.

Since conda environments are simply directories, they may be created anywhere.
However, conda has a notion of `locations` which are also simply directories
that are known to conda, and contain environments within. Conda environments
created in such locations are said to be "known", and can be displayed for
easy reference. Conda has a default system location, but additional locations
may be specified (see `Directory Structure`_ and :ref:`config`, respectively,
for more details).


.. _channel:
.. index::
    pair: terminology; channel

.. _locally_available:
.. index::
    pair: terminology; locally available

.. _activated:
.. index::
    pair: terminology; activated

.. _deactivated:
.. index::
    pair: terminology; deactivated


Channels
~~~~~~~~

Conda packages can be installed from local or remote ``channels`` within
repositories. A channel is a simple URL to a folder containing conda packages.

Conda comes with a default set of channels to search and install packages
from. However, these can be changed easily, additional default channels can
be configured or a specific channel can be specified *ad hoc* when installing a
package (see :ref:`config` for details).

Channels can be private, public, based on a single machine or local network or
hosted online.

Continuum provides the following standard channels:

 * ``http://repo.continuum.io/pkgs/dev`` - Experimental or developmental
   versions of packages
 * ``http://repo.continuum.io/pkgs/gpl`` - GPL licensed packages
 * ``http://repo.continuum.io/pkgs/free`` - non GPL open source packages

To view all available packages, you can use ``conda search``.  See the
:ref:`search command examples <search_example>` for more information.

Once a conda package has been downloaded, it is said to be "locally available".
A locally available package that has been linked into an conda environment
is said to be "linked". Conversely, unlinking a package from an environment
causes it to be "unlinked".


.. _location:
.. index::
    pair: terminology; location

.. _known:
.. index::
    pair: terminology; known


Package Naming Conventions
--------------------------

Names and versions of software packages do not follow any prescribed rules.
However, in order to facilitate communication and documentation,
conda employs the following naming conventions with respect to packages:

.. _package_name:
.. index::
    pair: terminology; package name
    seealso: name; package name

**package name**
    The name of a package, without any reference to a particular version.
    Conda package names are normalized, and may contain only lowercase alpha
    characters, numeric digits, underscores, or hyphens.  In usage
    documentation, these will be referred to by `package_name`.

.. _package_version:
.. index::
    pair: terminology; package version
    seealso: name; package version

**package version**
    A version number or string, often similar to *X.Y* or *X.Y.Z*, but may
    take other forms as well.

.. _build_string:
.. index::
    pair: terminology; build string
    seealso: name; build string

**build string**
    An arbitrary string that identifies a particular build of a package for
    conda.  It may contain suggestive mnemonics but these are subject to
    change and should not be relied upon or attempted to be parsed for any
    specific information.

.. _canonical_name:
.. index::
    pair: terminology; canonical name
    seealso: name; canonical name

**canonical name**
    The canonical name consists of the package name, version, and build
    string joined together by hyphens: *name*-*version*-*buildstring*.
    In usage documentation, these will be referred to by `canonical_name`.

.. _filename:
.. index::
    pair: terminology; filename

**file name**
    conda package filenames are canonical names, plus the suffix *.tar.bz2*.


These components are illustrated in the following figure:

.. figure::  images/conda_names.png
   :align:   center

   Different parts of conda package names.

.. _package_spec:
.. index::
    pair: terminology; package specification
    seealso: package spec; package specification

Additionally, a `package specification` is a package name, together with a package version (which may be partial or absent), joined by "=". Here are some examples:

* *python=2.7.3*
* *python=2.7*
* *python*

In usage documentation, these will be referred to by `package_spec`.

.. _meta_package:


Meta-Packages
-------------

conda also provides the notion of `meta-packages`.  A meta-package is a conda
package that only has dependencies, no files. An easy way to make a
meta-package is with the ``conda metapackage`` command.

.. _directory_structure:


Directory Structure
-------------------

The conda system has the following directory structure:

**ROOT_DIR**
    The directory that Anaconda (or Miniconda) was installed
    into; for example, */opt/Anaconda* or *C:\\Anaconda*

    */pkgs*
        Also referred to as *PKGS_DIR*. This directory contains exploded
        packages, ready to be linked in conda environments.
        Each package resides in a subdirectory corresponding to its
        canonical name.

    */envs*
        The system location for additional conda environments to be created.

    |   */bin*
    |   */include*
    |   */lib*
    |   */share*
    |       These subdirectories comprise the default Anaconda environment.

Other conda environments usually contain the same subdirectories as the
default environment.


Creating Python 3.4 or Python 2.6 environments
----------------------------------------------

Anaconda supports Python 2.6, 2.7, 3.3, and 3.4.  The default is Python 2.7 or
3.4, depending on which installer you used.

To get started, you need to create an environment using the :ref:`conda create <create_example>`
command.

.. code-block:: bash

    $ conda create -n py34 python=3.4 anaconda

Here, 'py34' is the name of the environment to create, and 'anaconda' is the
meta-package that includes all of the actual Python packages comprising
the Anaconda distribution.  When creating a new environment and installing
the Anaconda meta-package, the NumPy and Python versions can be specified,
e.g. `numpy=1.7` or `python=3.4`.

.. code-block:: bash

    $ conda create -n py26 python=2.6 anaconda

After the environment creation process completes, adjust your **PATH** variable
to point to this directory.  On Linux/MacOSX systems, this can be easily
done using:

.. code-block:: bash

    $ source activate <env name>

    # This command assumes ~/anaconda/bin/activate is the first 'activate' on your current PATH

This will modify your Bash PS1 to include the name of the environment.

.. code-block:: bash

   $ source activate myenv
   (myenv)$

You can disable this with ``conda config --set changeps1 no``. The environment
variable ``CONDA_DEFAULT_ENV`` is set to the currently activated environment.

On Windows systems, use ``activate`` instead of ``source activate``.

Now you're ready to begin using the Python located in your created
environment.

If you would like to deactivate this environment and revert your **PATH** to
its previous state, use:

.. code-block:: bash

    $ source deactivate

On Windows, this is just ``deactivate``.



.. _YAML syntax: http://en.wikipedia.org/wiki/YAML
