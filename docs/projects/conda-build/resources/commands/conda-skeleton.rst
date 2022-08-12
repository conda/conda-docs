
.. _skeleton_ref:

conda skeleton
==============

.. raw:: html

   <PRE>
   <!-- Manpage converted by man2html 3.0.1 -->
   <B>CONDA(1)</B>                         User Commands                        <B>CONDA(1)</B>




   </PRE>
   <H2>NAME</H2><PRE>
          conda - conda skeleton


   </PRE>
   <H2>DESCRIPTION</H2><PRE>
          usage: conda-skeleton [-h] {cpan,cran,luarocks,pypi,rpm} ...

          Generates  a  boilerplate/skeleton  recipe,  which you can then edit to
          create a full recipe. Some simple skeleton recipes may  not  even  need
          edits.


   </PRE>
   <H2>OPTIONS</H2><PRE>
      <B>positional</B> <B>arguments:</B>
                 {cpan,cran,luarocks,pypi,rpm}

          cpan   Create  recipe skeleton for packages hosted on the Comprehensive
                 Perl Archive Network (CPAN) (cpan.org).

          cran   Create recipe skeleton for packages hosted on the  Comprehensive
                 R Archive Network (CRAN) (cran.r-project.org).

          luarocks
                 Create recipe skeleton for luarocks, hosted at luarocks.org

          pypi   Create recipe skeleton for packages hosted on the Python Packag-
                 ing Index (PyPI) (pypi.io).

          rpm    Create recipe skeleton for RPM files

      <B>optional</B> <B>arguments:</B>
          <B>-h</B>, <B>--help</B>
                 Show this help message and exit.

          Run <B>--help</B> on the subcommands like 'conda skeleton pypi <B>--help</B>' to  see
          the options available.

      <B>conda</B> <B>commands</B> <B>available</B> <B>from</B> <B>other</B> <B>packages:</B>
                 build  build-all  convert  develop env index inspect metapackage
                 render server sign skeleton smithy tracker verify



   Anaconda, Inc.                     June 2018                          <B>CONDA(1)</B>
   </PRE>
