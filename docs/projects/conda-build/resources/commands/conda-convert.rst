
.. _convert_ref:

conda convert
=============

.. raw:: html

   <PRE>
   <!-- Manpage converted by man2html 3.0.1 -->
   <B>CONDA(1)</B>                         User Commands                        <B>CONDA(1)</B>




   </PRE>
   <H2>NAME</H2><PRE>
          conda - conda convert


   </PRE>
   <H2>DESCRIPTION</H2><PRE>
          usage: conda-convert [-h]

          [-p
          {osx-64,linux-32,linux-64,linux-ppc64le,linux-armv6l,linux-armv7l,linux-aarch64,win-32,win-64,all}]
                 [--dependencies      [DEPENDENCIES      [DEPENDENCIES     ...]]]
                 [--show-imports] [-f]  [-o  OUTPUT_DIR]  [-v]  [--dry-run]  [-q]
                 files [files ...]

          Various  tools  to  convert conda packages. Takes a pure Python package
          build for one platform and converts it to work on  one  or  more  other
          platforms, or all.


   </PRE>
   <H2>OPTIONS</H2><PRE>
      <B>positional</B> <B>arguments:</B>
          files  Package files to convert.

      <B>optional</B> <B>arguments:</B>
          <B>-h</B>, <B>--help</B>
                 Show this help message and exit.

          <B>-p</B>
          {osx-64,linux-32,linux-64,linux-ppc64le,linux-armv6l,linux-armv7l,linux-aarch64,win-32,win-64,all},
          <B>--platform</B>
          {osx-64,linux-32,linux-64,linux-ppc64le,linux-armv6l,linux-armv7l,linux-aarch64,win-32,win-64,all}
                 Platform to convert the packages to.

          <B>--dependencies</B>  [DEPENDENCIES  [DEPENDENCIES  ...]],  <B>-d</B>  [DEPENDENCIES
          [DEPENDENCIES ...]]
                 Additional  (besides python) dependencies of the converted pack-
                 age. To specify a version restriction for a dependency, wrap the
                 dependency in quotes, like 'package &gt;=2.0'.

          <B>--show-imports</B>
                 Show Python imports for compiled parts of the package.

          <B>-f</B>, <B>--force</B>
                 Force convert, even when a package has compiled C extensions.

          <B>-o</B> OUTPUT_DIR, <B>--output-dir</B> OUTPUT_DIR
                 Directory  to write the output files. The packages will be orga-
                 nized   in   platform/   subdirectories,   e.g.,    win-32/pack-
                 age-1.0-py27_0.tar.bz2.

          <B>-v</B>, <B>--verbose</B>
                 Print verbose output.

          <B>--dry-run</B>
                 Only display what would have been done.

          <B>-q</B>, <B>--quiet</B>
                 Don't print as much output.

          Tool to convert packages

          conda convert converts pure Python packages to other platforms.

          Packages  are  automatically  organized  in subdirectories according to
          platform, e.g.,

          osx-64/

                 package-1.0-py33.tar.bz2

          win-32/

                 package-1.0-py33.tar.bz2


   </PRE>
   <H2>EXAMPLES</H2><PRE>
          Convert a package built with conda build to Windows 64-bit,  and  place
          the  resulting  package  in  the current directory (supposing a default
          Anaconda install on Mac OS X):

                 conda convert package-1.0-py33.tar.bz2 -p win-64

      <B>conda</B> <B>commands</B> <B>available</B> <B>from</B> <B>other</B> <B>packages:</B>
                 build build-all convert develop env  index  inspect  metapackage
                 render server sign skeleton smithy tracker verify



   Anaconda, Inc.                     June 2018                          <B>CONDA(1)</B>
   </PRE>
