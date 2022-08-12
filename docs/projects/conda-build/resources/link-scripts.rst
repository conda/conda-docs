==================================================
Adding pre-link, post-link, and pre-unlink scripts
==================================================

You can add scripts to a recipe. They must be located in the same directory
as the meta.yaml file. The following scripts can be added:

* ``pre-link``---Executed before the package is installed. An error is
  indicated by a nonzero exit and causes conda to stop and causes the
  installation to fail.
* ``post-link``---Executed after the package is installed. An error is
  indicated by a nonzero exist and causes installation to fail. If there is an
  error, conda does not write any package metadata.
* ``pre-unlink``---Executed before the package is removed. An error is
  indicated by a nonzero exist and causes the removal to fail.

In addition to being co-located with the meta.yaml file, they must be named simply ``post-link.sh`` or ``post-link.bat``. Conda-build will rename them to .<name>-<action>.sh (or .bat) where ``<name>`` is the package name and ``<action>`` is one of the preceeding actions.

These scripts are executed in a subprocess by
conda, using ``%COMSPEC% /c <script>`` on Windows and
``/bin/bash <script>`` on macOS and Linux.


The convention for the path and filenames of these scripts on Windows is::

  Scripts/.<name>-<action>.bat

On Linux and macOS the convention is::

  bin/.<name>-<action>.sh

The scripts set the following environment variables:

.. list-table::
   :widths: 20 40

   * - PREFIX
     - The install prefix.
   * - PKG_NAME
     - The name of the package.
   * - PKG_VERSION
     - The version of the package.
   * - PKG_BUILDNUM
     - The build number of the package.

The scripts are:

* Windows:

  * ``pre-link.bat``
  * ``post-link.bat``
  * ``pre-unlink.bat``

* macOS and Linux:

  * ``pre-link.sh``
  * ``post-link.sh``
  * ``pre-unlink.sh``

Post-link and pre-unlink scripts should:

* Be avoided whenever possible.
* Not touch anything other than the files being installed.
* Not write anything to stdout or stderr, unless an error occurs.
* Not depend on any installed or to-be-installed conda packages.
* Depend only on simple system tools such as ``rm``, ``cp``, ``mv``, and ``ln``.

The scripts should not write to stdout or stderr unless an error occurs, but
they may write to ``$PREFIX/.messages.txt``, which is shown after conda
completes all actions.
