
.. _index_ref:

conda index
===========

.. raw:: html

   <PRE>
   <!-- Manpage converted by man2html 3.0.1 -->
   <B>CONDA(1)</B>                         User Commands                        <B>CONDA(1)</B>




   </PRE>
   <H2>NAME</H2><PRE>
          conda - conda index


   </PRE>
   <H2>DESCRIPTION</H2><PRE>
          usage: conda-index [-h] [-c] [-f] [-q] [--no-remove]

                 [--channel-name CHANNEL_NAME] [dir [dir ...]]

          Update package index metadata files in given directories.


   </PRE>
   <H2>OPTIONS</H2><PRE>
      <B>positional</B> <B>arguments:</B>
          dir    Directory that contains an index to be updated.

      <B>optional</B> <B>arguments:</B>
          <B>-h</B>, <B>--help</B>
                 Show this help message and exit.

          <B>-c</B>, <B>--check-md5</B>
                 Use  MD5 values instead of file modification times for determin-
                 ing if a package's metadata needs to be updated.

          <B>-f</B>, <B>--force</B>
                 Force reading all files.

          <B>-q</B>, <B>--quiet</B>
                 Don't show any output.

          <B>--no-remove</B>
                 Don't remove entries for files that don't exist.

          <B>--channel-name</B> CHANNEL_NAME
                 Adding a channel name will create an index.html file within  the
                 subdir.

      <B>conda</B> <B>commands</B> <B>available</B> <B>from</B> <B>other</B> <B>packages:</B>
                 build  build-all  convert  develop env index inspect metapackage
                 render server sign skeleton smithy tracker verify



   Anaconda, Inc.                     June 2018                          <B>CONDA(1)</B>
   </PRE>
