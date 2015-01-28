============
Introduction
============

Conda is a cross-platform, Python-agnostic binary package manager. Conda can:

- `Search <commands/conda-search.html>`_ for packages in a repository/package
  index/channel or a current installation.
- `Create <commands/conda-create.html>`_ conda environments.
- `Install <commands/conda-install>`_ and `update <conda-update.html>`_
  packages into new and existing environments.


.. _package:
.. index::
    pair: terminology; package


Packages
--------

A conda `package` is a binary archive (tarball) containing system-level
libraries, Python modules, executable programs, or other components. Conda
keeps track of dependencies between packages and platform specifics, making it
simple to install sets of packages.

A typical package file name could be something like:

    ``gevent-websocket-0.3.6-py27_0.tar.bz2``

    <package-name>-<version>-<build_string>.tar.bz2

.. seealso::

   - `Installing a package <commands/conda-install>`_
   - `Updating packages <conda-update.html>`_
   - :doc:`package-name`
   - :doc:`spec`


.. _meta_package:

Metapackages
------------

conda also provides the notion of `metapackages`.  A metapackage is a conda
package that only has dependencies, no files. An easy way to make a
metapackage is with the ``conda metapackage`` command.


.. _environment:
.. index::
    pair: terminology; environment

Environments
------------

A `conda environment` is a filesystem directory that contains a specific
collection of conda packages.  As a concrete example, you might want to have one
environment that provides NumPy 1.7, and another environment that provides NumPy
1.6 for legacy testing.  conda makes this kind of mixing and matching easy. To
begin using an environment, simply set your ``PATH`` variable to point to its
`bin` directory. This can also be done using the ``source activate`` (Linux,
OS X) or ``activate`` (Windows) command.

Since conda environments are simply directories, they may be created anywhere.
However, conda has a notion of `locations` which are also simply directories
that are known to conda, and contain environments within. Conda environments
created in such locations are said to be "known", and can be displayed for
easy reference. Conda has a default system location, but additional locations
may be specified.

.. seealso::

   - `Creating environments <commands/conda-create>`_
   - :doc:`config`


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
--------

Conda packages can be installed from local or remote ``channels`` within
repositories. A channel is a simple URL to a folder containing conda packages.

Conda comes with a default set of channels to search and install packages
from. However, these can be changed easily, additional default channels can
be configured or a specific channel can be specified *ad hoc* when installing a
package (see :doc:`config` for details).

Channels can be private, public, based on a single machine or local network or
hosted online.

Continuum provides the following standard channels:

 * ``http://repo.continuum.io/pkgs/dev`` - Experimental or developmental
   versions of packages
 * ``http://repo.continuum.io/pkgs/gpl`` - GPL licensed packages
 * ``http://repo.continuum.io/pkgs/free`` - non GPL open source packages

To view all available packages, you can use ``conda search``.  See the
:ref:`search command examples <search_example>` for more information.

.. _location:
.. index::
    pair: terminology; location

.. _known:
.. index::
    pair: terminology; known

Once a conda package has been downloaded, it is said to be "locally available".
A locally available package that has been linked into an conda environment
is said to be "linked". Conversely, unlinking a package from an environment
causes it to be "unlinked".


.. _directory_structure:

Conda system
------------

The conda system has the following directory structure:

**ROOT_DIR**
    The directory that Miniconda was installed into; for example,
    */opt/miniconda* or *C:\\Program Files\\Miniconda*

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
    |       These subdirectories comprise the default/root conda environment.

Other conda environments usually contain the same subdirectories as the
default/root environment.

.. This section should be moved elsewhere, it's too much of a tutorial for
   the introduction section.

Creating Python 3.4 or Python 2.6 environments
----------------------------------------------

Conda supports Python 2.6, 2.7, 3.3, and 3.4.  The default is Python 2.7 or
3.4, depending on which installer you used.

To get started, you need to create an environment using the :ref:`conda create <create_example>`
command.

.. code-block:: bash

    $ conda create -n py34 python=3.4 anaconda

Here, 'py34' is the name of the environment to create, and 'anaconda' is the
metapackage that includes all of the actual Python packages comprising
the Anaconda distribution.  When creating a new environment and installing
the Anaconda metapackage, the NumPy and Python versions can be specified,
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
