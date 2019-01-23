Miniconda
=========

 +------+--------------------+--------------------+--------------------+
 |      | Windows            | Mac OS X           | Linux              |
 +------+--------------------+--------------------+--------------------+
 |Python| `64-bit (exe       | `64-bit (bash      | `64-bit (bash      |
 |3.7   | installer) <https: | installer) <https: | installer) <https: |
 |      | //repo.anaconda.co | //repo.anaconda.co | //repo.anaconda.co |
 |      | m/miniconda/Minico | m/miniconda/Minico | m/miniconda/Minico |
 |      | nda3-latest-Window | nda3-latest-MacOSX | nda3-latest-Linux- |
 |      | s-x86_64.exe>`__   | -x86_64.sh>`__     | x86_64.sh>`__      |
 |      |                    |                    |                    |
 |      | `32-bit (exe       | `64-bit (.pkg      | `32-bit (bash      |
 |      | installer) <https: | installer) <https: | installer) <https: |
 |      | //repo.anaconda.co | //repo.anaconda.co | //repo.anaconda.co |
 |      | m/miniconda/Minico | m/miniconda/Minico | m/miniconda/Minico |
 |      | nda3-latest-Window | nda3-latest-MacOSX | nda3-latest-Linux- |
 |      | s-x86.exe>`__      | -x86_64.pkg>`__    | x86.sh>`__         |
 +------+--------------------+--------------------+--------------------+
 |Python| `64-bit (exe       | `64-bit (bash      | `64-bit (bash      |
 |2.7   | installer) <https: | installer) <https: | installer) <https: |
 |      | //repo.anaconda.co | //repo.anaconda.co | //repo.anaconda.co |
 |      | m/miniconda/Minico | m/miniconda/Minico | m/miniconda/Minico |
 |      | nda2-latest-Window | nda2-latest-MacOSX | nda2-latest-Linux- |
 |      | s-x86_64.exe>`__   | -x86_64.sh>`__     | x86_64.sh>`__      |
 |      |                    |                    |                    |
 |      | `32-bit (exe       | `64-bit (.pkg      | `32-bit (bash      |
 |      | installer) <https: | installer) <https: | installer) <https: |
 |      | //repo.anaconda.co | //repo.anaconda.co | //repo.anaconda.co |
 |      | m/miniconda/Minico | m/miniconda/Minico | m/miniconda/Minico |
 |      | nda2-latest-Window | nda2-latest-MacOSX | nda2-latest-Linux- |
 |      | s-x86.exe>`__      | -x86_64.pkg>`__    | x86.sh>`__         |
 +------+--------------------+--------------------+--------------------+

 `Installation
 instructions <https://conda.io/projects/conda/en/latest/user-guide/install/index.html>`__

 Other resources:

 -  `Miniconda with Python 3.7 for Power8 &
    Power9 <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-ppc64le.sh>`__
 -  `Miniconda with Python 2.7 for Power8 &
    Power9 <https://repo.anaconda.com/miniconda/Miniconda2-latest-Linux-ppc64le.sh>`__
 -  `Miniconda Docker
    images <https://hub.docker.com/r/continuumio/>`__
 -  `Miniconda AWS
    images <https://aws.amazon.com/marketplace/seller-profile?id=29f81979-a535-4f44-9e9f-6800807ad996>`__
 -  `Archive and MD5 sums for the
    installers <https://repo.anaconda.com/miniconda/>`__
 -  `conda change
    log <https://conda.io/projects/continuumio-conda/en/latest/release-notes.html>`__

 These Miniconda installers contain the conda
 package manager and Python. Once Miniconda is
 installed, you can use the conda command to install
 any other packages and create environments, etc.
 For example:

 .. container:: highlight-bash notranslate

    .. container:: highlight

       ::

          $ conda install numpy
          ...
          $ conda create -n py3k anaconda python=3
          ...

 There are two variants of the installer: Miniconda
 is Python 2 based and Miniconda3 is Python 3 based.
 Note that the choice of which Miniconda is
 installed only affects the root environment.
 Regardless of which version of Miniconda you
 install, you can still install both Python 2.x and
 Python 3.x environments.

 The other difference is that the Python 3 version
 of Miniconda will default to Python 3 when creating
 new environments and building packages. So for
 instance, the behavior of

 .. container:: highlight-bash notranslate

    .. container:: highlight

       ::

          $ conda create -n myenv python

 will be to install Python 2.7 with the Python 2
 Miniconda and to install Python 3.7 with the Python
 3 Miniconda. You can override the default by
 explicitly setting ``python=2`` or ``python=3``. It
 also determines the default value of ``CONDA_PY``
 when using ``conda build``.

 **Note**: If you already have Miniconda or Anaconda
 installed, and you just want to upgrade, you should
 not use the installer. Just use ``conda update``.
 For instance

 .. container:: highlight-bash notranslate

    .. container:: highlight

       ::

          $ conda update conda

 will update conda.
