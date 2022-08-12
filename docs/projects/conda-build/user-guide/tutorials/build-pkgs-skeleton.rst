===========================================
Building conda packages with conda skeleton
===========================================

Overview
========

This tutorial describes how to quickly build a conda package for
a Python module that is already available on PyPI.

In the first procedure, building a simple package, you build a
package that can be installed in any conda environment of the
same Python version as your root environment. The remaining
optional procedures describe how to build packages for other
Python versions and other architectures, as well as how to upload
packages to your Anaconda.org account.

.. note::
   You may consider using `Docker <https://www.docker.com/>`_ to run the tutorial.


Who is this for?
================

This tutorial is for Windows, macOS, and Linux users who wish to
build a conda package from a PyPI package. No prior knowledge of
conda-build or conda recipes is required.


.. _before-you-start1:

Before you start
================

Before you start, check the :ref:`prereqs`.


.. _conda-build-skeleton:

Building a simple package with conda skeleton pypi
==================================================

The ``conda skeleton`` command picks up the PyPI package metadata
and prepares the conda-build recipe. The final step is to
build the package itself and install it into your conda environment.

It is easy to build a skeleton recipe for any Python package that
is hosted on PyPI, the official third-party software repository
for the Python programming language.

In this section you are going to use conda skeleton to generate a
conda recipe, which informs conda-build about where the source
files are located and how to build and install the package.

You'll be working with a package named Click_ that is hosted on PyPI.
Click is a tool for exposing Python functions to create command line
interfaces.

.. _Click: https://github.com/pallets/click

First, in your user home directory, run the ``conda skeleton``
command:

.. code-block:: bash

    conda skeleton pypi click

The two arguments to ``conda skeleton`` are the hosting location,
in this case ``pypi``, and the name of the package.

This creates a directory named ``click`` and creates one
skeleton file in that directory: ``meta.yaml``. Many other files can be added
there as necessary, such as ``build.sh`` and ``bld.bat``, test scripts, or
anything else you need to build your software. For simple, pure-Python recipes,
these extra files are unnecessary and the build/script section in the ``meta.yaml``
is sufficient. Use the ``ls`` command on macOS or Linux or the ``dir`` command on
Windows to verify that this file has been created. The ``meta.yaml`` file has been
populated with information from the PyPI metadata and in many cases will not
need to be edited.

Files in the folder with ``meta.yaml`` are collectively referred to as the "conda-build recipe":

* ``meta.yaml``---Contains all the metadata in the recipe. Only
  the package name and package version sections are
  required---everything else is optional.

* ``bld.bat``---Windows commands to build the package.

* ``build.sh``---macOS and Linux commands to build the package.

Now that you have the conda-build recipe ready, you can use conda-build to create the package:

.. code-block:: bash

    conda-build click

When conda-build is finished, it displays the exact path and
filename of the conda package. See :ref:`troubleshooting` if the
``conda-build`` command fails.

Windows example file path:

.. code-block:: text

    C:\Users\jsmith\miniconda\conda-bld\win-64\click-7.0-py37_0.tar.bz2

macOS example file path:

.. code-block:: text

    /Users/jsmith/miniconda/conda-bld/osx-64/click-7.0-py37_0.tar.bz2


Linux example file path:

.. code-block:: text

    /home/jsmith/miniconda/conda-bld/linux-64/click-7.0-py37_0.tar.bz2


.. note::
   Your path and filename will vary depending on your
   installation and operating system. Save the path and filename
   information for the next step.

Now you can install your newly built package in your conda
environment by using the use-local flag:

.. code-block:: bash

    conda install --use-local click

Notice that Click is coming from the local conda-build channel.

.. code-block:: bash

   (click) 0561:~ jsmith$ conda list
   # packages in environment at /Users/Jsmith/miniconda/envs/click:
   # Name                    Version                   Build  Channel
   ca-certificates           2019.1.23                     0
   certifi                   2019.3.9                 py37_0
   click                     7.0                      py37_0    local

Now verify that Click installed successfully:

.. code-block:: bash

    conda list

Scroll through the list until you find Click.

At this point you now have a conda package for Click that
can be installed in any conda environment of the same Python
version as your root environment. The remaining optional sections
show you how to make packages for other Python versions and other
architectures and how to upload them to your Anaconda.org account.


.. _`python-versions`:

Optional---Building for a different Python version
==================================================
By default, conda-build creates packages for the version of
Python installed in the root environment. To build packages for
other versions of Python, you use the ``--python`` flag followed
by a version. For example, to explicitly build a version of the
Click package for Python 2.7, use:

.. code-block:: bash

    conda-build --python 2.7 click

Notice that the file printed at the end of the ``conda-build``
output has changed to reflect the requested version of Python.
``conda install`` will look in the package directory for the file
that matches your current Python version.

Windows example file path:

.. code-block:: text

    C:\Users\jsmith\Miniconda\conda-bld\win-64\click-7.0-py27_0.tar.bz2

macOS example file path:

.. code-block:: text

    /Users/jsmith/miniconda/conda-bld/osx-64/click-7.0-py27_0.tar.bz2


Linux example file path:

.. code-block:: text

    /home/jsmith/miniconda/conda-bld/linux-64/click-7.0-py27_0.tar.bz2


.. note::
   Your path and filename will vary depending on your
   installation and operating system. Save the
   path and filename information for the next task.

.. _convert-conda-package:

Optional---Converting conda package for other platforms
========================================================

Now that you have built a package for your current platform with
conda-build, you can convert it for use on other platforms with
the ``conda convert`` command. This works only for pure Python
packages where there is no compiled code. Conda convert does
nothing to change compiled code, it only adapts file paths to
take advantage of the fact that Python scripts are mostly
platform independent. Conda convert accepts a platform specifier
from this and a platform specifier from this list:

* osx-64.
* linux-32.
* linux-64.
* win-32.
* win-64.
* all.

In the output directory, 1 folder will be created for each of the
1 or more platforms you chose and each folder will contain a
.tar.bz2 package file for that platform.

Windows:

.. code-block:: text

    conda convert -f --platform all C:\Users\jsmith\miniconda\conda-bld\win-64\click-7.0-py37_0.tar.bz2
    -o outputdir\

macOS and Linux:

.. code-block:: text

    conda convert --platform all /home/jsmith/miniconda/conda-bld/linux-64/click-7.0-py37_0.tar.bz2
    -o outputdir/


.. note::
   Change your path and filename to the exact path and
   filename you saved in :ref:`python-versions`.

To use these packages, you need to transfer them to other
computers and place them in the correct ``conda-bld/$ARCH``
directory for the platform, where ``$ARCH`` can be ``osx-64``,
``linux-32``, ``linux-64``, ``win-32``, or ``win-64``.

A simpler way is to upload all of the bz2 files to Anaconda.org
as described in the next task.

If you find yourself needing to use ``conda convert``, you might
instead prefer to change your recipe to make your package a "noarch" package.
Noarch packages run anywhere and do not require conda convert.
Some of the ecosystem tools don't yet support noarch packages but,
for the most part, noarch packages are a better way to go.

.. _`upload-to-anaconda-org`:

Optional---Uploading packages to Anaconda.org
=============================================

Anaconda.org is a repository for
public or private packages. Uploading to Anaconda.org allows you
to easily install your package in any environment with just the
``conda install`` command, rather than manually copying or moving the
tarball file from one location to another. You can choose to make
your files public or private. For more information about
Anaconda.org, see the `Anaconda.org documentation
<http://docs.anaconda.org/>`_.

#. Create a free Anaconda.org account and record your new
   Anaconda.org username and password.

#. Run ``conda install anaconda-client`` and enter your
   Anaconda.org username and password.

#. Log into your Anaconda.org account from your terminal with
   the command ``anaconda login``.

Now you can upload the new local packages to Anaconda.org.

Windows:

.. code-block:: text

    anaconda upload C:\Users\jsmith\miniconda\conda-bld\win-64\click-7.0-py37_0.tar.bz2


macOS and Linux:

.. code-block:: text

    anaconda upload /home/jsmith/miniconda/conda-bld/linux-64/click-7.0-py37_0.tar.bz2


.. note::
   Change your path and filename to the exact path and
   filename you saved in :ref:`python-versions`. Your path and
   filename will vary depending on your installation and operating
   system.

If you created packages for multiple versions of Python or used
``conda convert`` to make packages for each supported architecture,
you must use the ``anaconda upload`` command to upload each one.
It is considered best practice to create packages for Python
versions 2.7, 3.4, and 3.5 along with all of the architectures.

.. tip::
   If you want to always automatically upload a successful
   build to Anaconda.org, run:
   ``conda config --set anaconda_upload yes``

You can log out of your Anaconda.org account with the command:

.. code-block:: bash

    anaconda logout


.. _`troubleshooting`:

Troubleshooting a sample issue
===============================

Conda-build may produce the error message "Build Package missing."

To explore this error:

#. Create a conda skeleton package for skyfield. The
   ``conda skeleton`` command is:

   .. code-block:: bash

       conda skeleton pypi skyfield

   This command creates the skyfield conda-build recipe.

#. Run ``conda-build skyfield`` and observe that it fails with
   the following output:

   .. code-block:: text

       Removing old build environment
       Removing old work directory
       BUILD START: skyfield-0.8-py35_0
       Using Anaconda Cloud api site https://api.anaconda.org
       Fetching package metadata: ......
       Solving package specifications: .
       Error:  Package missing in current osx-64 channels:
         - sgp4 >=1.4

In this example, the conda recipe requires ``sgp4`` for the
skyfield package. The skyfield recipe was created by
``conda skeleton``. This error means that conda could not find
the sgp4 package and install it.

Since many PyPI packages depend on other PyPI packages to build
or run, the solution is sometimes as simple as using
``conda skeleton`` to create a conda recipe for the missing
package and then building it:

.. code-block:: bash

    conda skeleton sgp4
    conda build sgp4

You may also try using the ``--recursive`` flag with
``conda skeleton``, but this makes conda recipes for all required
packages, even those that are already available to conda install.


.. _`help1`:

More information
================

For more options, see the full :doc:`conda skeleton command documentation <../../resources/commands/conda-skeleton>`.
