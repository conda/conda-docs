==================
Using R with conda
==================

With a single conda command you can easily install the R
programming language and over 80 of the most used R packages for
data science. Conda helps you keep your packages and dependencies
up to date. You can also easily create and share your own custom
R packages.

R Essentials works very much like Anaconda:

Use the Terminal or an Anaconda Prompt for the following steps.

* You can install all of the most popular packages with all of
  their dependencies with a single command::

    conda install r-essentials

* You can update all of the packages and their dependencies with
  a single command::

    conda update r-essentials

* If a new version of a package is available in the R channel,
  you can use ``conda update`` to also update specific packages.

As of early 2018, the default R interpreter installed into new
environments is MRO. For environments with R already installed,
conda won't switch to MRO without explicitly instructing conda
to use the ``r-base`` package. To explicitly request MRO as
the R interpreter for an environment, use the ``mro-base`` package.


Installing R Essentials
=======================

#. `Download <https://www.continuum.io/downloads>`_ and
   `install <https://docs.continuum.io/anaconda/install/>`_
   Anaconda.

#. To install the R Essentials package into the current environment,
   in your Terminal window or an Anaconda Prompt, run:

   .. code::

      conda install r-essentials


Create a new environment with Anaconda R instead of MRO
=======================================================

When creating a new environment, you can opt for Anaconda R rather than
MRO by explicitly including ``r-base`` in your list of packages. For example,
with conda 4.4,

   .. code::
      conda create -n anaconda-r r-essentials r-base
      conda activate anaconda-r

will give you an environment that uses Anaconda R as the R interpreter.


Switch an existing R environment to MRO
=======================================

Using conda 4.4 or later, executing

   .. code::
      conda install mro-base

in an existing environment containing R will ensure that the R interpreter
for that environment is MRO.  If using conda 4.3, switching to MRO is a
two step process:

   .. code::
      conda remove --force r-base _r-mutex
      conda install mro-base


Make Anaconda R the default R instead of MRO
============================================

Using conda 4.4 or later (check ``conda info``, or ``conda update conda``!)
executing the command

    .. code::
       conda config --system --set pinned_packages _r-mutex=*=anacondar*

will exclude MRO as the default R and force Anaconda R as the default.



Creating and sharing your own custom R bundle
==============================================

Creating and sharing your own custom R bundles with others is
similar to creating and sharing conda packages.

EXAMPLE: To create a simple custom R bundle metapackage named
"Custom-R-Bundle" that contains several popular programs and
their dependencies, in the Terminal window or an Anaconda Prompt, run::

   conda metapackage custom-r-bundle 0.1.0 --dependencies r-irkernel jupyter r-ggplot2 r-dplyr --summary "My custom R bundle"


Now you can easily share your new metapackage with friends and
colleagues by uploading it to your channel on `Anaconda Cloud
<https://anaconda.org>`_::

  conda install anaconda-client
  anaconda login
  anaconda upload path/to/custom-r-bundle-0.1.0-0.tar.bz2

Your friends and colleagues can now access your custom R bundle
from any computer by running in the Terminal window or an Anaconda Prompt::

  conda install -c <your anaconda.org username> custom-r-bundle

For more information, see `Jupyter and conda for R language
<https://www.continuum.io/blog/developer/jupyter-and-conda-r>`_.
