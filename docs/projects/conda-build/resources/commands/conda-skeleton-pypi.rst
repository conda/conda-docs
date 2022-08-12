
.. _skeleton pypi_ref:

conda skeleton pypi
===================

.. raw:: html

   <PRE>
   <!-- Manpage converted by man2html 3.0.1 -->
   <B>CONDA(1)</B>                         User Commands                        <B>CONDA(1)</B>




   </PRE>
   <H2>NAME</H2><PRE>
          conda - conda skeleton pypi


   </PRE>
   <H2>DESCRIPTION</H2><PRE>
          usage:  conda-skeleton  pypi  [-h] [--output-dir OUTPUT_DIR] [--version
          VERSION]

          [--all-urls] [--pypi-url PYPI_URL] [--prompt]
                 [--all-extras] [--recursive] [--version-compare]  [--python-ver-
                 sion  {2.7,3.4,3.5}]  [--manual-url]  [--noarch-python]  [--set-
                 up-options    SETUP_OPTIONS]    [--pin-numpy]     [--extra-specs
                 EXTRA_SPECS] packages [packages ...]

      <B>positional</B> <B>arguments:</B>
          packages
                 PyPi packages to create recipe skeletons for. You can also spec-
                 ify package[extra,...] features.

      <B>optional</B> <B>arguments:</B>
          <B>-h</B>, <B>--help</B>
                 Show this help message and exit.

          <B>--output-dir</B> OUTPUT_DIR
                 Directory to write recipes to (default: .).

          <B>--version</B> VERSION
                 Version to use. Applies to all packages. If  not  specified  the
                 lastest visible version on PyPI is used.

          <B>--all-urls</B>
                 Look  at  all  URLs,  not just source URLs. Use this if it can't
                 find the right URL.

          <B>--pypi-url</B> PYPI_URL
                 URL to use for PyPI (default: https://pypi.io/pypi/).

          <B>--prompt</B>
                 Prompt the user on ambiguous choices. Default  is  to  make  the
                 best possible choice and continue.

          <B>--all-extras</B>
                 Add all extra feature requirements. Applies to all packages.

          <B>--recursive</B>
                 Create recipes for dependencies if they do not already exist.

          <B>--version-compare</B>
                 Compare  the  package  version  of the recipe with all available
                 versions on PyPI.

          <B>--python-version</B> {2.7,3.4,3.5}
                 Version of Python to use to run setup.py. Default is 3.6.

          <B>--manual-url</B>
                 Manually  choose  source  url  when  more  than  one  urls   are
                 present.Default is the one with least source size.

          <B>--noarch-python</B>
                 Creates recipe as noarch python

          <B>--setup-options</B> SETUP_OPTIONS
                 Options to be added to setup.py install in the recipe.  The same
                 options are passed to setup.py install in both the  construction
                 of  the recipe and in the recipe itself.For options that include
                 a double-hypen or to  pass  multiple  options,  use  the  syntax
                 <B>--setupoptions=</B>"--option1 <B>--option-with-arg</B> arg"

          <B>--pin-numpy</B>
                 Ensure  that  the  generated  recipe pins the version of numpyto
                 CONDA_NPY.

          <B>--extra-specs</B> EXTRA_SPECS
                 Extra specs for the build environment to extract the skeleton.


   </PRE>
   <H2>EXAMPLES</H2><PRE>
          Create a recipe for the sympy package:

                 conda skeleton pypi sympy

          Create a recipes for the flake8 package and all its dependencies:

                 conda skeleton pypi --recursive flake8

          Use the --pypi-url flag to point to a PyPI mirror url:

                 conda skeleton pypi --pypi-url &lt;mirror-url&gt; package_name



   Anaconda, Inc.                     June 2018                          <B>CONDA(1)</B>
   </PRE>
