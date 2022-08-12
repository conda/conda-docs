=======================
Building conda packages
=======================

Overview
========

This tutorial describes how to use conda-build to create conda
packages on Windows, macOS, and Linux using the examples of
SEP and GDAL. Additional Windows-specific instructions are provided in the
:ref:`toolkit` section.

The final built packages from this tutorial are available on
`Anaconda Cloud <https://anaconda.org>`_:

* `SEP <https://anaconda.org/wwarner/sep/files>`_.

* `GDAL <https://anaconda.org/conda-forge/gdal/files>`_.

This tutorial also describes writing recipes. You can see the
final `SEP recipe
<https://github.com/conda-forge/sep-feedstock>`_
and the `GDAL recipe
<https://github.com/conda-forge/gdal-feedstock>`_
on GitHub in the `conda-build documentation repository
<https://github.com/conda/conda-build/tree/main/docs>`_.

Who is this for?
================

This tutorial is for Windows, macOS, and Linux users who wish to
build more complex conda packages. This tutorial will involve building
scientific packages, which require compilers for several different
Python versions.


.. _before-you-start4:

Before you start
================

Before you start, make sure you have installed:

   * `Conda <https://conda.io/projects/conda/en/latest/user-guide/install/index.html>`_.
   * :ref:`Conda-build <install-conda-build>`.
   * Any compilers you want.

.. _toolkit:

Toolkit
=======

Microsoft Visual Studio
-----------------------

In the standard practices of the conda developers, conda packages
for different versions of Python are each built with their own
version of Visual Studio (VS):

* Python 2.7 packages with Visual Studio 2008
* Python 3.4 packages with VS 2010
* Python 3.5 packages with VS 2015, (default) 2017
* Python 3.6 packages with VS 2015, (default) 2017
* Python 3.7 packages with VS 2015, (default) 2017

Using these versions of VS to build packages for each of these
versions of Python is also the practice used for the official
python.org builds of Python. Currently VS 2008 and VS 2010 are
available only through resellers, while VS 2015 and VS 2017 can
be purchased online from Microsoft. Note there is also a community
edition of VS 2015 and VS 2017 which may be used.


Alternatives to Microsoft Visual Studio
----------------------------------------

There are free alternatives available for each version of the VS
compilers:

* Instead of VS 2008, it is often possible to substitute the
  `free Microsoft Visual C++ Compiler for Python 2.7
  <https://www.microsoft.com/en-us/download/details.aspx?id=44266>`_.

* Instead of VS 2010, it is often possible to substitute the
  `free Microsoft Windows SDK for Windows 7 and .NET Framework 4
  <https://www.microsoft.com/en-us/download/details.aspx?id=8279>`_.

* Make sure that you also install `VS 2010 Service Pack 1 (SP1)
  <https://www.microsoft.com/en-us/download/details.aspx?id=34677>`_.

* Due to a bug in the VS 2010 SP1 installer, the compiler tools
  may be removed during installation of VS 2010 SP1. They can be
  restored as described in `Microsoft Visual C++ 2010 Service
  Pack 1 Compiler Update for the Windows SDK 7.1
  <https://www.microsoft.com/en-us/download/details.aspx?id=4422>`_.

* Visual Studio 2015 has a full-featured, free `Community edition
  <https://www.visualstudio.com/en-us/products/visual-studio-community-vs.aspx>`_
  for academic research, open source projects, and certain other
  use cases.


The MS Visual C++ Compiler for Python 2.7 and the Microsoft
Windows SDK for Windows 7 and .NET Framework 4 are both
reasonably well tested. Conda-build is carefully tested to
support these configurations, but there are known issues with the
CMake build tool and these free VS 2008 and 2010 alternatives.
In these cases, you should prefer the "NMake Makefile" generator,
rather than a Visual Studio solution generator.


Windows versions
-----------------

You can use any recent version of Windows. These examples were
built on Windows 10.

Other tools
------------

Some environments initially lack tools such as patch or Git
that may be needed for some build workflows.

On Windows, these can be installed with conda:

``conda install git m2-patch``


On macOS and Linux, replace ``m2-patch`` with patch.


Developing a build strategy
============================

Conda recipes are typically built with a trial-and-error method.
Often the first attempt to build a package fails with compiler
or linker errors, often caused by missing dependencies. The person
writing the recipe then examines these errors and modifies the
recipe to include the missing dependencies, usually as part of the
``meta.yaml`` file. Then the recipe writer attempts the build
again and, after a few of these cycles of trial and error, the
package builds successfully.


Building with a Python version different from your Miniconda installation
==========================================================================

Miniconda2 and Miniconda3 can each build packages for either
Python 2 or Python 3 simply by specifying the version you want.
Miniconda2 includes only Python 2 and Miniconda3 includes only
Python 3.

Installing only one makes it easier to keep track of
the builds, but it is possible to have both installed on the same
system at the same time. If you have both installed, use the
``where`` command on Windows, or ``which`` command on Linux to
see which version comes first on PATH since this is the one you will be using::

  where python

To build a package for a Python version other than the one in
your Miniconda installation, use the ``--python`` option in the
``conda-build`` command.

EXAMPLE: To build a Python 3.5 package with Miniconda2::

    conda-build recipeDirectory --python=3.5

.. note::
   Replace ``recipeDirectory`` with the name and path of your
   recipe directory.

Automated testing
==================

After the build, if the recipe directory contains a test file. This test
file is named ``run_test.bat`` on Windows, ``run_test.sh`` on macOS or Linux,
or ``run_test.py`` on any platform. The file runs to test the package
and any errors are reported. After seeing "check the output," you can
also test if this package was built by using the command::

$ conda build --test <path to package>.tar.bz2

.. note::
   Use the :ref:`Test section of the meta.yaml file
   <meta-test>` to move data files from the recipe directory to the
   test directory when the test is run.


Building a SEP package with conda and Python 2 or 3
=====================================================

The `SEP documentation <https://sep.readthedocs.io>`_ states
that SEP runs on Python 2 and 3, and it depends only on NumPy.
Searching for SEP and PyPI shows that there is already `a PyPI
package for SEP <https://pypi.python.org/pypi/sep>`_.

Because a PyPI package for SEP already exists, the
``conda skeleton`` command can make a skeleton or outline of a
conda recipe based on the PyPI package. Then the recipe outline
can be completed manually and conda can build a conda package
from the completed recipe.


Install Visual Studio
----------------------

If you have not already done so, install the appropriate
version of Visual Studio:

* For Python 3---Visual Studio 2017:

  #. Choose Custom install.

  #. Under Programming Languages, choose to install Visual C++.

* For Python 2---Visual Studio 2008:

  #. Choose Custom install.

  #. Choose to install X64 Compilers and Tools. Install Service Pack 1.


Make a conda skeleton recipe
-----------------------------

#. Run the skeleton command::

       conda skeleton pypi sep

   The ``skeleton`` command installs into a newly created
   directory called ``sep``.

#. Go to the ``sep`` directory to view the files::

       cd sep

   One skeleton file has been created: ``meta.yaml``


Edit the skeleton files
------------------------

For this package, ``bld.bat`` and ``build.sh`` need no changes.
You need to edit the ``meta.yaml`` file to add the dependency on
NumPy and add an optional test for the built package by importing
it. For more information about what can be specified in ``meta.yaml``,
see :doc:`../../resources/define-metadata`.

#. In the requirements section of the ``meta.yaml`` file, add a
   line that adds NumPy as a requirement to build the package.

#. Add a second line to list NumPy as a requirement to run the
   package.

#. Set the NumPy version to the letters ``x.x``.

#. Make sure the new line is aligned with ``- python`` on the
   line above it, so as to ensure proper yaml format.

EXAMPLE:

.. code-block:: yaml

    requirements:
      host:
        - python
        - numpy     x.x

      run:
        - python
        - numpy     x.x

Notice that there are two types of requirements, host and run.
Host represents packages that need to be specific to the target
platform when the target platform is not necessarily the same as
the native build platform. Run represents the dependencies that
should be installed when the package is installed.

.. note::
   Using the letters ``x.x`` instead of a specific version
   such as ``1.11`` pins NumPy dynamically, so that the actual
   version of NumPy is taken from the build command. Currently, NumPy
   is the only package that can be pinned dynamically. Pinning is
   important for SEP because this package uses NumPy's C API through
   Cython. That API changes between NumPy versions, so it is
   important to use the same NumPy version at runtime that was used
   at build time.


OPTIONAL: Add a test for the built package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Adding this optional test will test the package at the end of the
build by making sure that the Python statement ``import sep``
runs successfully:

#. Add ``- sep``, checking to be sure that the indentation is
   consistent with the rest of the file.

   EXAMPLE:

   .. code-block:: yaml

    test:
      # Python imports
      imports:
        - sep


Build the package
-----------------

Build the package using the recipe you just created::

    conda build sep


Check the output
----------------

#. Check the output to make sure that the build completed
   successfully. The output contains the location of the final
   package file and a command to upload the package to Anaconda
   Cloud. The output will look something like:

   .. code-block:: yaml

      # Automatic uploading is disabled
      # If you want to upload package(s) to anaconda.org later, type:
      anaconda upload /Users/builder/miniconda3/conda-bld/osx-64/sep-1.0.3-np111py36_0.tar.bz2
      # To have conda build upload to anaconda.org automatically, use
      # $ conda config --set anaconda_upload yes
      anaconda_upload is not set.  Not uploading wheels: []
      ####################################################################################
      Resource usage summary:
      Total time: 0:00:56.4
      CPU usage: sys=0:00:00.7, user=0:00:07.0
      Maximum memory usage observed: 220.1M
      Total disk usage observed (not including envs): 3.9K
      ####################################################################################
      Source and build intermediates have been left in /Users/builder/miniconda3/conda-bld.
      There are currently 437 accumulated.
      To remove them, you can run the ```conda build purge``` command

2. If there are any linker or compiler errors, modify the recipe
   and build again.


Building a GDAL package with conda and Python 2 or 3
====================================================

This procedure describes how to build a package with Python 2 or Python 3.
Follow the instructions for your preferred version.

To begin, install Anaconda or Miniconda and conda-build. If you are using a
Windows machine, also use conda to install Git and the m2-patch.

.. code-block:: bash

    conda install git
    conda install m2-patch

Because GDAL includes C and C++, building it on Windows requires Visual Studio.
This procedure describes how to build a package with Python 2 or
Python 3. Follow the instructions for the version with which you want
to build.


To build a GDAL package:

#. Install Visual Studio:

   * For Python 3, install `Visual Studio 2017 <https://docs.microsoft.com/en-us/visualstudio/install/install-visual-studio?view=vs-2017>`_.
     Choose Custom install. Under Programming Languages, select workloads that
     come from Visual Studio so you choose the Desktop Development with C++ and
     Universal Platform C.

   * For Python 2, install `Visual Studio 2008 <http://download.microsoft.com/download/E/8/E/E8EEB394-7F42-4963-A2D8-29559B738298/VS2008ExpressWithSP1ENUX1504728.iso>`_.
     Choose Custom install. Choose to install X64 Compilers and Tools.
     Install Visual Studio 2008 Service Pack 1.

#. Install Git.
   Because the GDAL package sources are retrieved from GitHub
   for the build, you must install Git::

      conda install git m2-patch conda-build

#. Get gdal-feedstock. For the purpose of this tutorial, we will be using a recipe from Anaconda::

    git clone https://github.com/AnacondaRecipes/gdal-feedstock.git

#. Use conda-build to build the gdal-feedstock::

    conda build gdal-feedstock

#. Check the output to make sure the build completed
   successfully. The output also contains the location of the
   final package file and a command to upload the package to
   Cloud. For this package in particular, there should be two
   packages outputted: libgdal and GDAL.

#. In case of any linker or compiler errors, modify the recipe
   and run it again.

Let’s take a better look at what’s happening inside the gdal-feedstock.
In particular, what is happening in the ``meta.yaml``.

The first interesting bit happens under ``source`` in the patches
section:
::

  patches:
    # BUILT_AS_DYNAMIC_LIB.
    - 0001-windowshdf5.patch
    # Use multiple cores on Windows.
    - 0002-multiprocessor.patch
    # disable 12 bit jpeg on Windows as we aren't using internal jpeg
    - 0003-disable_jpeg12.patch

This section says that when this package is being built on a Windows
platform, apply the following patch files. Notice that the patch files
are in the `patches` directory of the recipe. These patches will only
be applied to Windows since the ``# [win]`` selector is applied to each
of the patch entries. For more about selectors, see
:ref:`preprocess-selectors`.

In the requirements section, notice how there are both a build and
host set of requirements. For this recipe, all the compilers required to
build the package are listed in the build requirements.
Normally, this section will list out packages required to build the package.
GDAL requires CMake on Windows, as well as C compilers.
Notice that the C compilers are pulled into the recipe using the syntax
``{{ compiler('c') }}``. Since conda-build 3, conda-build defines a jinja2
function ``compiler()`` to specify compiler packages dynamically. So, using
the ``compiler(‘c’)`` function in a conda recipe will pull in the correct
compiler for any build platform. For more information about compilers with
conda-build see :ref:`compiler-tools<compiler-tools>`.

Also note that the compilers used by conda-build can be specified using
a ``conda_build_config.yaml``. For more information about how to do that,
see :ref:`using-your-customized-compiler-package-with-conda-build-3`.

Notice that this package has an ``outputs`` section.
This section is a list of packages to output as a result of building
this package. In this case, the packages libgdal and GDAL will be built.
Similar to a normal recipe, the outputs can have build scripts,
tests scripts and requirements specified.
For more information on how outputs work, see the :ref:`package-outputs`.

Now, let's try to build GDAL against some build matrix.
We will specify building against Python 3.7 and 3.5 using a conda-build config.
Add the following to your ``conda_build_config.yaml``:

..  code-block:: yaml

    python:
       - 3.7
       - 3.5


Now you can build GDAL using conda-build with the command::

  conda build gdal-feedstock

Or explicitly set the location of the conda-build variant matrix::

  conda build gdal-feedstock --variant-config-file conda_build_config.yaml

If you want to know more about build variants and ``conda_build_config.yaml``,
including how to specify a config file and what can go into it, take a look
at :ref:`conda-build-variant-config-files`.
