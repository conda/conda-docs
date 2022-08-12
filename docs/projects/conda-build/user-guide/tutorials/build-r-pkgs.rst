======================================
Building R packages with skeleton CRAN
======================================

Overview
========

This tutorial describes how to quickly build
an R-language package on macOS for an R module
that is already available on CRAN.

You will build a simple package that can be
installed in any conda environment of the same
R version as your root environment. The tutorial
will also tell you how to build the dependencies
that may arise while building the package.

Who is this for?
================
This tutorial is for macOS users who wish to
build an R-language package from CRAN.
No prior knowledge of conda-build or conda recipes
is required.


.. _before-you-start3:

Before you start
================

Before you start, check the :doc:`prerequisites <index>`.

.. _conda-build-cran:

Building a simple package with conda skeleton CRAN
==================================================

The conda skeleton command picks up the CRAN package
metadata and prepares the conda-build recipe. The final
step is to build the package itself and install it into
your conda environment.

It is easy to build a skeleton recipe for any R package that is hosted on CRAN.
In this section you are going to use conda skeleton to generate a conda recipe,
which informs conda-build about where the source files are located and how to
build and install the package.

You'll be working with a package that is hosted on CRAN named fansi_,
a tool that accounts for the effects of ANSI text formatting control sequences.

.. _fansi: https://github.com/conda-forge/r-fansi-feedstock

First, in your user home directory, run the conda skeleton command:

.. code-block:: bash

    conda skeleton cran fansi

The two arguments to ``conda skeleton`` are the type of hosting location,
in this case ``cran``, and the name of the package.

This creates a directory named ``r-fansi`` and creates 1
skeleton file in that directory: ``meta.yaml``. Many other files
can be added there as necessary, such as ``build.sh`` and ``bld.bat``,
test scripts, or anything else you need to build your software.
Use the ``ls`` command to verify that this file has been created.
The ``meta.yaml`` file has been populated with information from the
CRAN metadata and in many cases will not need to be edited.

Files in the folder with ``meta.yaml`` are collectively referred to
as the "conda-build recipe":

* ``meta.yaml``---Contains all the metadata in the recipe. The package name and package version sections are required---everything else is optional.

* ``bld.bat``---Windows commands to build the package.

* ``build.sh``---macOS and Linux commands to build the package.

Now that you have the conda-build recipe ready, you can use
conda-build to create the package:

.. code-block:: bash

    conda-build r-fansi

When conda-build is finished, it displays the exact path and
filename of the conda package. See :ref:`troubleshooting` if the
``conda-build`` command fails. If you receive an error with SDK on macOS,
review our :ref:`resources for macOS and SDK <mac-SDK>`.

Example file path:

.. code-block:: text

    /Users/jsmith/anaconda3/conda-bld/osx-64/r-fansi-0.4.0-r353h46e59ec_0.tar.bz2

.. note::
   Your path and filename will vary depending on your
   installation and operating system. Save the path and
   filename information for the next step.

Now you can install your newly built package in your
conda environment by using the use-local flag:

.. code-block:: bash

    conda install --use-local r-fansi

Now verify that fansi installed successfully:

.. code-block:: bash

    conda list

Scroll through the list until you find ``r-fansi``.

Notice that fansi is coming from the local conda-build channel.

.. code-block:: bash

   (base) 0561:~ jsmith$ conda list
   # packages in environment at /Users/Jsmith/anaconda3:
   # Name                    Version                   Build  Channel
   qtpy                      1.5.0                    py37_0
   r-base                    3.5.1                h539fb6c_1
   r-fansi                   0.4.0            r353h46e59ec_0    local

The version of R will be what you have in your base environment.

See :ref:`different-r-version` to set your own
R version.

At this point you now have a conda package for fansi
that can be installed in any conda environment of its
R version.

Building an R package with dependencies
=======================================

The fansi package was a simple one that didn’t have
dependencies. To build an R package with dependencies,
let’s look at the example of janitor. Janitor is a
package hosted on CRAN that is used for examining and
cleaning up data.

To begin building it, type:

.. code-block:: bash

    conda skeleton cran janitor

This creates a directory named ``r-janitor`` and
creates one skeleton file in that directory: ``meta.yaml``.
Many other files can be added there as necessary, such
as ``build.sh`` and ``bld.bat``, test scripts, or anything else
you need to build your software. Use the ``ls`` command
to verify that this file has been created. The ``meta.yaml``
file has been populated with information from the CRAN
metadata and in many cases will not need to be edited.

Now that you have the conda-build recipe ready, you can
use conda-build to create the package:

.. code-block:: bash

    conda-build r-janitor

What may happen at this point is that you will have
dependencies of this package that do not exist as conda
packages yet. They need to be turned into conda packages.
Use conda skeleton to recursively build out recipes for
the packages that it depends on:

.. code-block:: bash

    conda skeleton cran janitor --recursive

You can manually build each package individually
by typing:

.. code-block:: bash

    conda-build package-name

.. note::
   Replace "package-name" with the name of each
   package.

Once all of the package dependencies are resolved, you
can build the R package by using:

.. code-block:: bash

    conda-build .

Now you can install your newly built package in your
conda environment by using the use-local flag:

.. code-block:: bash

    conda install --use-local r-janitor


The remaining optional sections show you how to make
R packages for other R versions and other architectures
and how to upload them to your Anaconda.org account.

.. _`different-r-version`:

Optional---Building for a different R version
=============================================

By default, conda-build creates packages for the version
of R installed in the root environment. To build packages
for other versions of R, you use the ``--R`` flag followed by
a version.

For example, to explicitly build a version of the fansi package
for R 3.6.1, use:

.. code-block:: bash

    conda-build --R 3.6.1 r-fansi

Notice that the file printed at the end of the conda-build
output has changed to reflect the requested version of R.
Conda install will look in the package directory for the file
that matches your current R version.

Example file path:

.. code-block:: text

    /Users/jsmith/anaconda3/conda-bld/osx-64/r-fansi-0.4.0-r353h46e59ec_0.tar.bz2

.. note::
   Your path and filename will vary depending on your
   installation and operating system. Save the path and
   filename information for the next task.

.. _`upload-to-anaconda-org1`:

Optional---Uploading packages to Anaconda.org
=============================================
Anaconda.org is a repository for public or private packages.
Uploading to Anaconda.org allows you to easily install your package
in any environment with just the ``conda install`` command,
rather than manually copying or moving the tarball file from
one location to another. You can choose to make your files
public or private.

For more information about Anaconda.org, see the `Anaconda.org documentation
<http://docs.anaconda.org/>`_.

#. Create a free Anaconda.org account and record your new
   Anaconda.org username and password.

#. Run ``conda install anaconda-client`` and enter your
   Anaconda.org username and password.

#. Log into your Anaconda.org account from your terminal with
   the command ``anaconda login``.

Now you can upload the new local packages to Anaconda.org.

.. code-block:: text

    anaconda upload /Users/jsmith/anaconda3/conda-bld/osx-64/r-fansi-0.4.0-r353h46e59ec_0.tar.bz2


.. note::
   Change your path and filename to the exact path and
   filename you saved in :ref:`different-r-version`. Your path and filename
   will vary depending on your installation and operating system.
   If you created packages for multiple versions of R,
   you must use the ``anaconda upload`` command to upload each one.

.. tip::
   If you want to always automatically upload a successful build to Anaconda.org, run:
   ``conda config --set anaconda_upload yes``

You can log out of your Anaconda.org account with the command:

.. code-block:: bash

    anaconda logout

More information
================
For more options, see the full
:doc:`conda skeleton command documentation
<../../resources/commands/conda-skeleton>`.
