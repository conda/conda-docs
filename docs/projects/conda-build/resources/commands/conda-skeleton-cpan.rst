
.. _skeleton cpan_ref:

conda skeleton cpan
===================

.. raw:: html

   <PRE>
   <!-- Manpage converted by man2html 3.0.1 -->
   <B>CONDA(1)</B>                         User Commands                        <B>CONDA(1)</B>




   </PRE>
   <H2>NAME</H2><PRE>
          conda - conda skeleton cpan


   </PRE>
   <H2>DESCRIPTION</H2><PRE>
          usage:  conda-skeleton  cpan  [-h] [--output-dir OUTPUT_DIR] [--version
          VERSION]

          [--meta-cpan-url META_CPAN_URL] [--recursive]
                 [--force] [--write_core] packages [packages ...]

      <B>positional</B> <B>arguments:</B>
          packages
                 CPAN packages to create recipe skeletons for.

      <B>optional</B> <B>arguments:</B>
          <B>-h</B>, <B>--help</B>
                 Show this help message and exit.

          <B>--output-dir</B> OUTPUT_DIR
                 Directory to write recipes to (default: .).

          <B>--version</B> VERSION
                 Version to use. Applies to all packages.

          <B>--meta-cpan-url</B> META_CPAN_URL
                 URL to use for MetaCPAN API. It must include a version, such  as
                 v1

          <B>--recursive</B>
                 Create  recipes  for  dependencies  if they do not already exist
                 (default: False).

          <B>--force</B>
                 Force overwrite of existing recipes (default: False).

          <B>--write_core</B>
                 Write recipes for perl core modules (default: False).



   Anaconda, Inc.                     June 2018                          <B>CONDA(1)</B>
   </PRE>
