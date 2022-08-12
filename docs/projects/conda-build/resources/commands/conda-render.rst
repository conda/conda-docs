
.. _render_ref:

conda render
============

.. raw:: html

   <PRE>
   <!-- Manpage converted by man2html 3.0.1 -->
   <B>CONDA(1)</B>                         User Commands                        <B>CONDA(1)</B>




   </PRE>
   <H2>NAME</H2><PRE>
          conda - conda render


   </PRE>
   <H2>DESCRIPTION</H2><PRE>
          usage: conda-render [-h] [-V] [-n] [--output] [--python PYTHON] [--perl
          PERL]

          [--numpy NUMPY] [--R R_BASE] [--lua LUA]
                 [--bootstrap  BOOTSTRAP]  [--append-file   APPEND_SECTIONS_FILE]
                 [--clobber-file CLOBBER_SECTIONS_FILE] [-m VARIANT_CONFIG_FILES]
                 [-e  EXCLUSIVE_CONFIG_FILE]  [--old-build-string]  [-c  CHANNEL]
                 [--override-channels] [-f FILE] [--verbose] RECIPE_PATH

          Tool  for  building conda packages. A conda package is a binary tarball
          containing system-level libraries, Python modules, executable programs,
          or other components. conda keeps track of dependencies between packages
          and platform specifics, making it simple to create working environments
          from

                 different sets of packages.


   </PRE>
   <H2>OPTIONS</H2><PRE>
      <B>positional</B> <B>arguments:</B>
          RECIPE_PATH
                 Path to recipe directory.

      <B>optional</B> <B>arguments:</B>
          <B>-h</B>, <B>--help</B>
                 Show this help message and exit.

          <B>-V</B>, <B>--version</B>
                 Show the conda-build version number and exit.

          <B>-n</B>, <B>--no-source</B>
                 When  templating can't be completed, do not obtain the source to
                 try fill in related template variables.

          <B>--output</B>
                 Output the conda package filename which would have been created

          <B>--python</B> PYTHON
                 Set the Python version used by conda build.

          <B>--perl</B> PERL
                 Set the Perl version used by conda build.

          <B>--numpy</B> NUMPY
                 Set the NumPy version used by conda build.

          <B>--R</B> R_BASE
                 Set the R version used by conda build.

          <B>--lua</B> LUA
                 Set the Lua version used by conda build.

          <B>--bootstrap</B> BOOTSTRAP
                 Provide initial configuration in addition to recipe.  Can  be  a
                 path to or name of an environment, which will be emulated in the
                 package.

          <B>--append-file</B> APPEND_SECTIONS_FILE
                 Append data in meta.yaml with fields from this file.  Jinja2  is
                 not done on appended fields

          <B>--clobber-file</B> CLOBBER_SECTIONS_FILE
                 Clobber data in meta.yaml with fields from this file.  Jinja2 is
                 not done on clobbered fields.

          <B>-m</B> VARIANT_CONFIG_FILES, <B>--variant-config-files</B> VARIANT_CONFIG_FILES
                 Additional variant config files to add.  These  yaml  files  can
                 contain  keys such as `c_compiler` and `target_platform` to form
                 a build matrix.

          <B>-e</B> EXCLUSIVE_CONFIG_FILE, <B>--exclusive-config-file</B> EXCLUSIVE_CONFIG_FILE
                 Exclusive variant config file  to  add.  Compared  with  <B>--vari-</B>
                 <B>ant-config-files</B>, you're allowed only one file here. Providing a
                 file here disables searching in your home directory and in  cwd.
                 The  file  specified  here  comes  at the start of the order, as
                 opposed to the end with <B>--variant-config-files</B>. Any config files
                 in  recipes  and  any  config files specified with <B>--variantcon-</B>
                 <B>fig-files</B> will override values from this file.

          <B>--old-build-string</B>
                 Disable hash additions to filenames to distinguish package vari-
                 ants  from  one another. NOTE: any filename collisions are yours
                 to handle. Any variants with overlapping names  within  a  build
                 will clobber each other.

          <B>-c</B> CHANNEL, <B>--channel</B> CHANNEL
                 Additional  channel  to  search  for  packages.  These  are URLs
                 searched in the order they  are  given  (including  file://  for
                 local directories). Then, the defaults or channels from .condarc
                 are searched (unless <B>--override-channels</B> is given). You can  use
                 'defaults'  to  get the default packages for conda, and 'system'
                 to get the system  packages,  which  also  takes  .condarc  into
                 account.  You  can  also  use  any  name  and the .condarc chan-
                 nel_alias value will be prepended. The default channel_alias  is
                 http://conda.anaconda.org/.

          <B>--override-channels</B>
                 Do  not search default or .condarc channels. Requires <B>--channel</B>.

          <B>-f</B> FILE, <B>--file</B> FILE
                 write YAML to file, given as argument here. Overwrites  existing
                 files.

          <B>--verbose</B>
                 Enable verbose output from download tools and progress updates

      <B>conda</B> <B>commands</B> <B>available</B> <B>from</B> <B>other</B> <B>packages:</B>
                 build  build-all  convert  develop env index inspect metapackage
                 render server sign skeleton smithy tracker verify



   Anaconda, Inc.                     June 2018                          <B>CONDA(1)</B>
   </PRE>
