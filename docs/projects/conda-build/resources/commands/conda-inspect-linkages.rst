
.. _inspect linkages_ref:

conda inspect linkages
======================

.. raw:: html

   <PRE>
   <!-- Manpage converted by man2html 3.0.1 -->
   <B>CONDA(1)</B>                         User Commands                        <B>CONDA(1)</B>




   </PRE>
   <H2>NAME</H2><PRE>
          conda - conda inspect linkages


   </PRE>
   <H2>DESCRIPTION</H2><PRE>
          usage: conda-inspect linkages [-h] [--untracked] [--show-files]

          [--groupby {package,dependency}]
                 [--sysroot SYSROOT] [--all] [-n ENVIRONMENT | <B>-p</B> PATH] [packages
                 [packages ...]]

          Investigates linkages of binary libraries in a package (works in  Linux
          and  OS  X).  This is an advanced command to aid building packages that
          link against C libraries. Aggregates the output of ldd (on  Linux)  and
          otool  <B>-L</B>  (on  OS  X) by dependent packages. Useful for finding broken
          links, or links against system libraries that  ought  to  be  dependent
          conda packages.


   </PRE>
   <H2>OPTIONS</H2><PRE>
      <B>positional</B> <B>arguments:</B>
          packages
                 Conda packages to inspect.

      <B>optional</B> <B>arguments:</B>
          <B>-h</B>, <B>--help</B>
                 Show this help message and exit.

          <B>--untracked</B>
                 Inspect  the  untracked files in the environment. This is useful
                 when used in conjunction with conda build <B>--build-only</B>.

          <B>--show-files</B>
                 Show the files in the package that link to each library

          <B>--groupby</B> {package,dependency}
                 Attribute to group by (default: package). Useful  when  used  in
                 conjunction with <B>--all</B>.

          <B>--sysroot</B> SYSROOT
                 System root in which to look for system libraries.

          <B>--all</B>  Generate a report for all packages in the environment.

          <B>-n</B> ENVIRONMENT, <B>--name</B> ENVIRONMENT
                 Name of environment.

          <B>-p</B> PATH, <B>--prefix</B> PATH
                 Full path to environment prefix.



   Anaconda, Inc.                     June 2018                          <B>CONDA(1)</B>
   </PRE>
