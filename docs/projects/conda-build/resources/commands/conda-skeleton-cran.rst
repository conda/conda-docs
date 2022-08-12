
.. _skeleton cran_ref:

conda skeleton cran
===================

.. raw:: html

   <PRE>
   <!-- Manpage converted by man2html 3.0.1 -->
   <B>CONDA(1)</B>                         User Commands                        <B>CONDA(1)</B>




   </PRE>
   <H2>NAME</H2><PRE>
          conda - conda skeleton cran


   </PRE>
   <H2>DESCRIPTION</H2><PRE>
          usage: conda-skeleton cran [-h] [--output-dir OUTPUT_DIR]

          [--output-suffix OUTPUT_SUFFIX]
                 [--add-maintainer ADD_MAINTAINER] [--version VERSION] [--git-tag
                 GIT_TAG]   [--all-urls]   [--cran-url   CRAN_URL]    [--r-interp
                 R_INTERP]          [--use-binaries-ver         USE_BINARIES_VER]
                 [--use-noarch-generic]     [--use-rtools-win]      [--recursive]
                 [--no-recursive]        [--no-archive]       [--version-compare]
                 [--update-policy      {error,skip-up-to-date,skip-existing,over-
                 write,merge-keep-build-num,merge-incr-build-num}]    [-m   VARI-
                 ANT_CONFIG_FILES] packages [packages ...]

      <B>positional</B> <B>arguments:</B>
          packages
                 CRAN packages to create recipe skeletons for.

      <B>optional</B> <B>arguments:</B>
          <B>-h</B>, <B>--help</B>
                 Show this help message and exit.

          <B>--output-dir</B> OUTPUT_DIR
                 Directory to write recipes to (default: .).

          <B>--output-suffix</B> OUTPUT_SUFFIX
                 Suffix to add to recipe dir, can contain other dirs (eg:  <B>-feed-</B>
                 <B>stock</B>/recipe). (default: )

          <B>--add-maintainer</B> ADD_MAINTAINER
                 Add this github username as a maintainer if not already present.
                 (default: None)

          <B>--version</B> VERSION
                 Version to use. Applies to all packages. (default: None)

          <B>--git-tag</B> GIT_TAG
                 Git tag to use for GitHub recipes. (default: None)

          <B>--all-urls</B>
                 Look at all URLs, not just source URLs. Use  this  if  it  can't
                 find the right URL. (default: False)

          <B>--cran-url</B> CRAN_URL
                 URL to use for as source package repository (default: None)

          <B>--r-interp</B> R_INTERP
                 Declare R interpreter package (default: r-base)

          <B>--use-binaries-ver</B> USE_BINARIES_VER
                 Repackage  binaries from version provided by argument instead of
                 building from source. (default: None)

          <B>--use-noarch-generic</B>
                 Mark packages that do not need compilation as `noarch:  generic`
                 (default: False)

          <B>--use-rtools-win</B>
                 Use Rtools when building from source on Windows (default: False)

          <B>--recursive</B>
                 Create recipes for dependencies if they do  not  already  exist.
                 (default: False)

          <B>--no-recursive</B>
                 Don't  create  recipes  for  dependencies if they do not already
                 exist. (default: True)

          <B>--no-archive</B>
                 Don't include an Archive download url. (default: True)

          <B>--version-compare</B>
                 Compare the package version of the recipe with the one available
                 on  CRAN.  Exits  1 if a newer version is available and 0 other-
                 wise. (default: False)

          <B>--update-policy</B>              {error,skip-up-to-date,skip-existing,over-
          write,merge-keep-build-num,merge-incr-build-num}
                 Dictates what to do when existing packages  are  encountered  in
                 the output directory (set by <B>--outputdir</B>). In the present imple-
                 mentation, the  merge  options  avoid  overwriting  bld.bat  and
                 build.sh  and  only  manage  copying  across  patches,  and  the
                 `build/{number,script_env}` fields. When  the  version  changes,
                 both  merge options reset `build/number` to 0.  When the version
                 does not change they either keep the old `build/number` or  else
                 increase it by one.  (default: error)

          <B>-m</B> VARIANT_CONFIG_FILES, <B>--variant-config-files</B> VARIANT_CONFIG_FILES
                 Variant  config  file  to add. These yaml files can contain keys
                 such as `cran_mirror`. Only one can be provided here.  (default:
                 None)



   Anaconda, Inc.                     June 2018                          <B>CONDA(1)</B>
   </PRE>
