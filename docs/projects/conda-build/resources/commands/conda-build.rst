
.. _build_ref:

conda-build
===========

.. raw:: html

   <PRE>
   <!-- Manpage converted by man2html 3.0.1 -->
   <B>CONDA(1)</B>                         User Commands                        <B>CONDA(1)</B>




   </PRE>
   <H2>NAME</H2><PRE>
          conda - conda build


   </PRE>
   <H2>DESCRIPTION</H2><PRE>
          usage:  conda-build [-h] [-V] [-n] [--output] [--python PYTHON] [--perl
          PERL]

                 [--numpy NUMPY] [--R R_BASE] [--lua LUA] [--bootstrap BOOTSTRAP]
                 [--append-file   APPEND_SECTIONS_FILE]   [--clobber-file   CLOB-
                 BER_SECTIONS_FILE] [-m VARIANT_CONFIG_FILES] [-e  EXCLUSIVE_CON-
                 FIG_FILE]  [--old-build-string] [--check] [--no-anaconda-upload]
                 [--no-include-recipe]   [-s]   [-t]   [--no-test]   [-b]    [-p]
                 [--skip-existing]  [--keep-old-work]  [--dirty]  [-q]  [--debug]
                 [--token TOKEN] [--user  USER]  [--no-force-upload]  [--password
                 PASSWORD]  [--sign  SIGN]  [--sign-with  SIGN_WITH]  [--identity
                 IDENTITY] [--config-file CONFIG_FILE] [--repository  REPOSITORY]
                 [--no-activate]   [--no-build-id]   [--croot  CROOT]  [--verify]
                 [--output-folder  OUTPUT_FOLDER]   [--no-prefix-length-fallback]
                 [--prefix-length-fallback]    [--prefix-length   _PREFIX_LENGTH]
                 [--no-locking]   [--no-remove-work-dir]    [--error-overlinking]
                 [--no-error-overlinking]                    [--long-test-prefix]
                 [--no-long-test-prefix] [--keep-going]  [--cache-dir  CACHE_DIR]
                 [--no-copy-test-source-files] [--merge-build-host] [--stats-file
                 STATS_FILE] [--extra-deps EXTRA_DEPS [EXTRA_DEPS ...]] [-c CHAN-
                 NEL] [--override-channels] RECIPE_PATH [RECIPE_PATH ...]

          Tool  for  building conda packages. A conda package is a binary tarball
          containing system-level libraries, Python modules, executable programs,
          or other components. conda keeps track of dependencies between packages
          and platform specifics, making it simple to create working environments
          from different sets of packages.

      <B>positional</B> <B>arguments:</B>
          RECIPE_PATH
                 Path  to  recipe  directory. Pass 'purge' here to clean the work
                 and test intermediates.

      <B>optional</B> <B>arguments:</B>
          <B>-h</B>, <B>--help</B>
                 Show this help message and exit.

          <B>-V</B>, <B>--version</B>
                 Show the conda-build version number and exit.

          <B>-n</B>, <B>--no-source</B>
                 When templating can't be completed, do not obtain the source  to
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
                 Provide  initial  configuration in addition to recipe.  Can be a
                 path to or name of an environment, which will be emulated in the
                 package.

          <B>--append-file</B> APPEND_SECTIONS_FILE
                 Append  data in meta.yaml with fields from this file.  Jinja2 is
                 not done on appended fields

          <B>--clobber-file</B> CLOBBER_SECTIONS_FILE
                 Clobber data in meta.yaml with fields from this file.  Jinja2 is
                 not done on clobbered fields.

          <B>-m</B> VARIANT_CONFIG_FILES, <B>--variant-config-files</B> VARIANT_CONFIG_FILES
                 Additional  variant  config  files  to add. These yaml files can
                 contain keys such as `c_compiler` and `target_platform` to  form
                 a build matrix.

          <B>-e</B> EXCLUSIVE_CONFIG_FILE, <B>--exclusive-config-file</B> EXCLUSIVE_CONFIG_FILE
                 Exclusive  variant  config  file  to  add. Compared with <B>--vari-</B>
                 <B>ant-config-files</B>, you're allowed only one file here. Providing a
                 file  here disables searching in your home directory and in cwd.
                 The file specified here comes at the  start  of  the  order,  as
                 opposed to the end with <B>--variant-config-files</B>. Any config files
                 in recipes and any config  files  specified  with  <B>--variantcon-</B>
                 <B>fig-files</B> will override values from this file.

          <B>--old-build-string</B>
                 Disable hash additions to filenames to distinguish package vari-
                 ants from one another. NOTE: any filename collisions  are  yours
                 to  handle.  Any  variants with overlapping names within a build
                 will clobber each other.

          <B>--check</B>
                 Only check (validate) the recipe.

          <B>--no-anaconda-upload</B>
                 Do not ask to upload the package to anaconda.org.

          <B>--no-include-recipe</B>
                 Don't include the recipe inside the built package.

          <B>-s</B>, <B>--source</B>
                 Only obtain the source (but don't build).

          <B>-t</B>, <B>--test</B>
                 Test package (assumes package  is  already  built).   RECIPE_DIR
                 argument  can  be  either recipe directory, in which case source
                 download may be necessary to resolve package version, or path to
                 built  package  .tar.bz2 file, in which case no source is neces-
                 sary.

          <B>--no-test</B>
                 Do not test the package.

          <B>-b</B>, <B>--build-only</B>
                 Only run the build, without  any  post  processing  or  testing.
                 Implies <B>--no-test</B> and <B>--no-anaconda-upload</B>.

          <B>-p</B>, <B>--post</B>
                 Run   the  post-build  logic.  Implies  <B>--no-test</B>  and  <B>--noana-</B>
                 <B>conda-upload</B>.

          <B>--skip-existing</B>
                 Skip recipes for which there already exists  an  existing  build
                 (locally or in the channels).

          <B>--keep-old-work</B>
                 Do  not  remove anything from environment, even after successful
                 build and test.

          <B>--dirty</B>
                 Do not remove work directory or _build environment, to speed  up
                 debugging. Does not apply patches or download source.

          <B>-q</B>, <B>--quiet</B>
                 do not display progress bar

          <B>--debug</B>
                 Show debug output from source checkouts and conda

          <B>--token</B> TOKEN
                 Token to pass through to anaconda upload

          <B>--user</B> USER
                 User/organization to upload packages to on anaconda.org or pypi

          <B>--label</B> LABELS
                 Label argument to pass through to anaconda upload

          <B>--no-force-upload</B>
                 Disable force upload to anaconda.org, preventing overwriting any
                 existing packages

          <B>--no-activate</B>
                 do not activate the build and test envs; just prepend to PATH

          <B>--no-build-id</B>
                 do not generate unique build folder names. Use if having  issues
                 with paths being too long.

          <B>--croot</B> CROOT
                 Build  root  folder.  Equivalent  to CONDA_BLD_PATH, but applies
                 only to this call of conda-build.

          <B>--verify</B>
                 do not run verification on recipes or packages when building

          <B>--output-folder</B> OUTPUT_FOLDER
                 folder to dump output package to.  Package  are  moved  here  if
                 build  or  test succeeds. Destination folder must exist prior to
                 using this.

          <B>--no-prefix-length-fallback</B>
                 Disable fallback to older 80 character prefix length if environ-
                 ment  creation fails due to insufficient prefix length in depen-
                 dency packages

          <B>--prefix-length-fallback</B>
                 Disable fallback to older 80 character prefix length if environ-
                 ment  creation fails due to insufficient prefix length in depen-
                 dency packages

          <B>--prefix-length</B> _PREFIX_LENGTH
                 length of build prefix. For packages with  binaries  that  embed
                 the path, this is critical to ensuring that your package can run
                 as many places as possible.  Notethat this value can be  altered
                 by  the  OS  below  conda-build  (e.g.  encrypted filesystems on
                 Linux), and you should prefer to set <B>--croot</B> to a  non-encrypted
                 location instead, so that you maintain a known prefix length.

          <B>--no-locking</B>
                 Disable  locking,  to  avoid  unresolved  race condition issues.
                 Unsafe to run multiple builds at once on one  system  with  this
                 set.

          <B>--no-remove-work-dir</B>
                 Disable removal of the work dir before testing. Be careful using
                 this option, as you package may depend on  files  that  are  not
                 included in the package, and may pass tests, but ultimately fail
                 on installed systems.

          <B>--error-overlinking</B>
                 Enable error when shared libraries from transitive  dependencies
                 are  directly  linked  to any executables or shared libraries in
                 built packages. This is disabled by default, but will be enabled
                 by default in condabuild 4.0.

          <B>--no-error-overlinking</B>
                 Disable error when shared libraries from transitive dependencies
                 are directly linked to any executables or  shared  libraries  in
                 built packages. This is currently the default behavior, but will
                 change in conda-build 4.0.

          <B>--long-test-prefix</B>
                 Use a long prefix for the test prefix, as well as the build pre-
                 fix.  Affects  only  Linux  and  Mac.  Prefix length matches the
                 <B>--prefix-length</B> flag. This is on by default in conda-build 3.0+

          <B>--no-long-test-prefix</B>
                 Do not use a long prefix for the test prefix,  as  well  as  the
                 build prefix. Affects only Linux and Mac.  Prefix length matches
                 the <B>--prefix-length</B> flag.

          <B>--keep-going</B>, <B>-k</B>
                 When running tests, keep going after each failure.   Default  is
                 to stop on the first failure.

          <B>--cache-dir</B> CACHE_DIR
                 Path to store the source files (archives, git clones, etc.) dur-
                 ing the build.

          <B>--no-copy-test-source-files</B>
                 Disables copying the files necessary  for  testing  the  package
                 into  the  info/test  folder. Passing this argument means it may
                 not be possible to test the  package  without  internet  access.
                 There is also a danger that the source archive(s) containing the
                 files could become unavailable sometime in the future.

          <B>--merge-build-host</B>
                 Merge the build and host directories, even when host section  or
                 compiler jinja2 is present

          <B>--stats-file</B> STATS_FILE
                 File path to save build statistics to. Stats are in JSON format

          <B>--extra-deps</B> EXTRA_DEPS [EXTRA_DEPS ...]
                 Extra  dependencies  to  add  to all environment creation steps.
                 This is only enabled for testing with the  <B>-t</B>  or  <B>--test</B>  flag.
                 Change meta.yaml or use templates otherwise.

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

      <B>PyPI</B> <B>upload</B> <B>parameters</B> <B>(twine):</B>
          <B>--password</B> PASSWORD
                 password to use when uploading packages to pypi

          <B>--sign</B> SIGN
                 sign files when uploading to pypi

          <B>--sign-with</B> SIGN_WITH
                 program to use to sign files when uploading to pypi

          <B>--identity</B> IDENTITY
                 GPG identity to use to sign files when uploading to pypi

          <B>--config-file</B> CONFIG_FILE
                 path to .pypirc file to use when uploading to pypi

          <B>--repository</B> REPOSITORY, <B>-r</B> REPOSITORY
                 PyPI repository to upload to

      <B>conda</B> <B>commands</B> <B>available</B> <B>from</B> <B>other</B> <B>packages:</B>
                 build build-all convert develop env  index  inspect  metapackage
                 render server sign skeleton smithy tracker verify



   Anaconda, Inc.                     June 2018                          <B>CONDA(1)</B>
   </PRE>
