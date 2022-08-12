
.. _inspect objects_ref:

conda inspect objects
=====================

.. raw:: html

   <PRE>
   <!-- Manpage converted by man2html 3.0.1 -->
   <B>CONDA(1)</B>                         User Commands                        <B>CONDA(1)</B>




   </PRE>
   <H2>NAME</H2><PRE>
          conda - conda inspect objects


   </PRE>
   <H2>DESCRIPTION</H2><PRE>
          usage: conda-inspect objects [-h] [--untracked]

          [--groupby {filename,filetype,rpath}] [--all]
                 [-n ENVIRONMENT | <B>-p</B> PATH] [packages [packages ...]]

          Investigate binary object files in a package (only works on OS X). This
          is an advanced command to aid  building  packages  that  have  compiled
          libraries.  Aggregates  the  output  of  otool on all the binary object
          files in a package.


   </PRE>
   <H2>OPTIONS</H2><PRE>
      <B>positional</B> <B>arguments:</B>
          packages
                 Conda packages to inspect.

      <B>optional</B> <B>arguments:</B>
          <B>-h</B>, <B>--help</B>
                 Show this help message and exit.

          <B>--untracked</B>
                 Inspect the untracked files in the environment. This  is  useful
                 when used in conjunction with conda build <B>--build-only</B>.

          <B>--groupby</B> {filename,filetype,rpath}
                 Attribute to group by (default: filename).

          <B>--all</B>  Generate a report for all packages in the environment.

          <B>-n</B> ENVIRONMENT, <B>--name</B> ENVIRONMENT
                 Name of environment.

          <B>-p</B> PATH, <B>--prefix</B> PATH
                 Full path to environment prefix.



   Anaconda, Inc.                     June 2018                          <B>CONDA(1)</B>
   </PRE>
