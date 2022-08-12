
.. _develop_ref:

conda develop
=============

.. raw:: html

   <PRE>
   <!-- Manpage converted by man2html 3.0.1 -->
   <B>CONDA(1)</B>                         User Commands                        <B>CONDA(1)</B>




   </PRE>
   <H2>NAME</H2><PRE>
          conda - conda develop


   </PRE>
   <H2>DESCRIPTION</H2><PRE>
          usage:  conda-develop  [-h]  [-npf] [-b] [-c] [-u] [-n ENVIRONMENT | <B>-p</B>
          PATH]

                 PATH [PATH ...]

          Install a Python package in 'development mode'.

          This works by creating a conda.pth file in site-packages.


   </PRE>
   <H2>OPTIONS</H2><PRE>
      <B>positional</B> <B>arguments:</B>
          PATH   Path to the source directory.

      <B>optional</B> <B>arguments:</B>
          <B>-h</B>, <B>--help</B>
                 Show this help message and exit.

          <B>-npf</B>, <B>--no-pth-file</B>
                 Relink compiled extension dependencies against  libraries  found
                 in current conda env. Do not add source to conda.pth.

          <B>-b</B>, <B>--build_ext</B>
                 Build  extensions  inplace,  invoking: python setup.py build_ext
                 <B>--inplace</B>; add to conda.pth; relink runtime libraries  to  envi-
                 ronment's lib/.

          <B>-c</B>, <B>--clean</B>
                 Invoke  clean  on  setup.py:  python  setup.py  clean  use  with
                 build_ext to clean before building.

          <B>-u</B>, <B>--uninstall</B>
                 Removes package if installed in 'development mode'  by  deleting
                 path  from conda.pth file. Ignore other options - just uninstall
                 and exit

          <B>-n</B> ENVIRONMENT, <B>--name</B> ENVIRONMENT
                 Name of environment.

          <B>-p</B> PATH, <B>--prefix</B> PATH
                 Full path to environment prefix.

      <B>conda</B> <B>commands</B> <B>available</B> <B>from</B> <B>other</B> <B>packages:</B>
                 build build-all convert develop env  index  inspect  metapackage
                 render server sign skeleton smithy tracker verify



   Anaconda, Inc.                     June 2018                          <B>CONDA(1)</B>
   </PRE>
