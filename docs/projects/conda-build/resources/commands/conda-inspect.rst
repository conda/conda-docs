
.. _inspect_ref:

conda inspect
=============

.. raw:: html

   <PRE>
   <!-- Manpage converted by man2html 3.0.1 -->
   <B>CONDA(1)</B>                         User Commands                        <B>CONDA(1)</B>




   </PRE>
   <H2>NAME</H2><PRE>
          conda - conda inspect


   </PRE>
   <H2>DESCRIPTION</H2><PRE>
          usage: conda-inspect [-h]

          {linkages,objects,channels,prefix-lengths,hash-inputs}
                 ...

          Tools for inspecting conda packages.


   </PRE>
   <H2>OPTIONS</H2><PRE>
      <B>positional</B> <B>arguments:</B>
                 {linkages,objects,channels,prefix-lengths,hash-inputs}

          linkages
                 Investigates linkages of binary libraries in a package (works in
                 Linux and OS X). This is an advanced  command  to  aid  building
                 packages that link against C libraries. Aggregates the output of
                 ldd (on Linux) and otool <B>-L</B> (on OS  X)  by  dependent  packages.
                 Useful  for  finding  broken  links,  or  links  against  system
                 libraries that ought to be dependent conda packages.

          objects
                 Investigate binary object files in a package (only works  on  OS
                 X).  This  is  an advanced command to aid building packages that
                 have compiled libraries.  Aggregates the output of otool on  all
                 the binary object files in a package.

          channels
                 Tools for investigating conda channels.

          prefix-lengths
                 Inspect  packages  in given path, finding those with binary pre-
                 fixes shorter than specified

          hash-inputs
                 Show data used to compute hash identifier (h????) for package

      <B>optional</B> <B>arguments:</B>
          <B>-h</B>, <B>--help</B>
                 Show this help message and exit.

          Run <B>--help</B> on the subcommands like 'conda inspect linkages  <B>--help</B>'  to
          see the options available.

      <B>conda</B> <B>commands</B> <B>available</B> <B>from</B> <B>other</B> <B>packages:</B>
                 build  build-all  convert  develop env index inspect metapackage
                 render server sign skeleton smithy tracker verify



   Anaconda, Inc.                     June 2018                          <B>CONDA(1)</B>
   </PRE>
