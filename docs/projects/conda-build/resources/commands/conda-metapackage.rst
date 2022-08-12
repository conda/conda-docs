
.. _metapackage_ref:

conda metapackage
=================

.. raw:: html

   <PRE>
   <!-- Manpage converted by man2html 3.0.1 -->
   <B>CONDA(1)</B>                         User Commands                        <B>CONDA(1)</B>




   </PRE>
   <H2>NAME</H2><PRE>
          conda - conda metapackage


   </PRE>
   <H2>DESCRIPTION</H2><PRE>
          usage: conda-metapackage [-h] [--no-anaconda-upload] [--token TOKEN]

          [--user USER] [--build-number BUILD_NUMBER]
                 [--build-string   BUILD_STRING]   [--dependencies  [DEPENDENCIES
                 [DEPENDENCIES ...]]]   [--home  HOME]  [--license  LICENSE_NAME]
                 [--summary  SUMMARY] [--entry-points [ENTRY_POINTS [ENTRY_POINTS
                 ...]]]  [-c CHANNEL] [--override-channels] name version

          Tool for building conda metapackages.  A metapackage is a package  with
          no  files,  only  metadata.  They are typically used to collect several
          packages together into a single package via dependencies.

          NOTE: Metapackages can also be created by creating a  recipe  with  the
          necessary  metadata  in the meta.yaml, but a metapackage can be created
          entirely from the command line with the conda metapackage command.


   </PRE>
   <H2>OPTIONS</H2><PRE>
      <B>positional</B> <B>arguments:</B>
          name   Name of the created package.

          version
                 Version of the created package.

      <B>optional</B> <B>arguments:</B>
          <B>-h</B>, <B>--help</B>
                 Show this help message and exit.

          <B>--no-anaconda-upload</B>
                 Do not ask to upload the package to anaconda.org.

          <B>--token</B> TOKEN
                 Token to pass through to anaconda upload

          <B>--user</B> USER
                 User/organization to upload packages to on anaconda.org

          <B>--label</B> LABELS
                 Label argument to pass through to anaconda upload

          <B>--build-number</B> BUILD_NUMBER
                 Build number for the package (default is 0).

          <B>--build-string</B> BUILD_STRING
                 Build string for the package (default  is  automatically  gener-
                 ated).

          <B>--dependencies</B>  [DEPENDENCIES  [DEPENDENCIES  ...]],  <B>-d</B>  [DEPENDENCIES
          [DEPENDENCIES ...]]
                 The  dependencies  of the package. To specify a version restric-
                 tion for a dependency,  wrap  the  dependency  in  quotes,  like
                 'package &gt;=2.0'.

          <B>--home</B> HOME
                 The homepage for the metapackage.

          <B>--license</B> LICENSE_NAME
                 The license of the metapackage.

          <B>--summary</B> SUMMARY
                 Summary  of the package. Pass this in as a string on the command
                 line, like <B>--summary</B> 'A metapackage for X'. It is recommended to
                 use  single quotes if you are not doing variable substitution to
                 avoid interpretation of special characters.

          <B>--entry-points</B> [ENTRY_POINTS [ENTRY_POINTS ...]]
                 Python entry points to create automatically. They should use the
                 same   syntax   as   in   the   meta.yaml  of  a  recipe,  e.g.,
                 <B>--entry-points</B> bsdiff4=bsdiff4.cli:main_bsdiff4 will  create  an
                 entry  point  called  bsdiff4  that  calls bsdiff4.cli.main_bsd-
                 iff4().

          <B>-c</B> CHANNEL, <B>--channel</B> CHANNEL
                 Additional channel  to  search  for  packages.  These  are  URLs
                 searched  in  the  order  they  are given (including file:// for
                 local directories). Then, the defaults or channels from .condarc
                 are  searched (unless <B>--override-channels</B> is given). You can use
                 'defaults' to get the default packages for conda,  and  'system'
                 to  get  the  system  packages,  which  also takes .condarc into
                 account. You can also  use  any  name  and  the  .condarc  chan-
                 nel_alias  value will be prepended. The default channel_alias is
                 http://conda.anaconda.org/.

          <B>--override-channels</B>
                 Do not search default or .condarc channels. Requires  <B>--channel</B>.

      <B>conda</B> <B>commands</B> <B>available</B> <B>from</B> <B>other</B> <B>packages:</B>
                 build  build-all  convert  develop env index inspect metapackage
                 render server sign skeleton smithy tracker verify



   Anaconda, Inc.                     June 2018                          <B>CONDA(1)</B>
   </PRE>
