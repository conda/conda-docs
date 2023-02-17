.. This page is generated from the create_miniconda_rst.py script.
   To make changes edit the miniconda.rst.jinja2 file and execute the script
   to re-generate miniconda.rst

=========
Miniconda
=========

Miniconda is a free minimal installer for conda. It is a small, bootstrap
version of Anaconda that includes only conda, Python, the packages they depend
on, and a small number of other useful packages, including pip, zlib and a
few others. Use the ``conda install`` command to install 720+ additional conda
packages from the Anaconda repository.

`See if Miniconda is right for you <https://docs.conda.io/projects/conda/en/stable/user-guide/install/download.html#anaconda-or-miniconda>`_.

System requirements
===================

* License: Free use and redistribution under the terms of the `EULA for Miniconda <https://www.anaconda.com/end-user-license-agreement-miniconda>`_.
* Operating system: Windows 8 or newer, 64-bit macOS 10.13+, or Linux, including Ubuntu, RedHat, CentOS 7+, and others.
* If your operating system is older than what is currently supported, you can find older versions of the Miniconda installers in our `archive <https://repo.anaconda.com/miniconda/>`_ that might work for you.
* System architecture: Windows- 64-bit x86, 32-bit x86; macOS- 64-bit x86 & Apple M1 (ARM64); Linux- 64-bit x86, 64-bit aarch64 (AWS Graviton2), 64-bit IBM Power8/Power9, s390x (Linux on IBM Z & LinuxONE).
* The ``linux-aarch64`` Miniconda installer requires ``glibc >=2.26`` and thus will **not** work with CentOS 7, Ubuntu 16.04, or Debian 9 ("stretch").
* Minimum 400 MB disk space to download and install.

On Windows, macOS, and Linux, it is best to install Miniconda for the local user,
which does not require administrator permissions and is the most robust type of
installation. However, if you need to, you can install Miniconda system wide,
which does require administrator permissions.

Latest Miniconda Installer Links
================================

.. csv-table:: Latest - Conda 23.1.0 Python 3.10.9 released February 7, 2023
   :header: Platform,Name,SHA256 hash
   :widths: 5, 10, 80

   Windows,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe>`_,``d4517212c8ac44fd8b5ccc2d4d9f38c2dd924c77a81c2be92c3a72e70dd3e907``
   ,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86.exe>`_,``4fb64e6c9c28b88beab16994bfba4829110ea3145baa60bda5344174ab65d462``
   macOS,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh>`_,``bfb81814e16eb450b1dbde7b4ecb9ebc5186834cb4ede5926c699762ca69953b``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg>`_,``bcc0067864011a93083ff2d6fe7b29e877c1477f24ee9d34b54d0165f8b32f11``
   ,`Miniconda3 macOS Apple M1 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh>`_,``cc5bcf95d5db0f7f454b2d800d52da8b70563f8454d529e7ac2da9725650eb27``
   ,`Miniconda3 macOS Apple M1 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.pkg>`_,``09d893e44400f61d36daeaa9befff8219a7e0127358d904a4368b2f0ae738df0``
   Linux,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh>`_,``32d73e1bc33fda089d7cd9ef4c1be542616bd8e437d1f77afeeaf7afdb019787``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh>`_,``80d6c306b015e1e3b01ea59dc66c676a81fa30279bc2da1f180a7ef7b2191d6e``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-ppc64le.sh>`_,``9ca8077a0af8845fc574a120ef8d68690d7a9862d354a2a4468de5d2196f406c``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-s390x.sh>`_,``0d00a9d34c5fd17d116bf4e7c893b7441a67c7a25416ede90289d87216104a97``

Windows installers
==================

.. csv-table:: Windows
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.10,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.1.0-1-Windows-x86_64.exe>`_,53.2 MiB,``d4517212c8ac44fd8b5ccc2d4d9f38c2dd924c77a81c2be92c3a72e70dd3e907``
   Python 3.9,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.1.0-1-Windows-x86_64.exe>`_,52.9 MiB,``a2e7ec485e5412673fad31e6a5a79f9de73792e7c966764f92eabf25ec37557f``
   Python 3.8,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.1.0-1-Windows-x86_64.exe>`_,52.4 MiB,``4178df2a15284fd07b10c5fad592e5c15e6be5bfc37ee90d8e02bbde7792f6f9``
   Python 3.7,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_23.1.0-1-Windows-x86_64.exe>`_,50.6 MiB,``2319e6ab37215daf08f47b0da35a53f6a648121029113ae2ba53917d777b84bd``
   Python 3.9,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Windows-x86.exe>`_,67.8 MiB,``4fb64e6c9c28b88beab16994bfba4829110ea3145baa60bda5344174ab65d462``
   Python 3.8,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Windows-x86.exe>`_,66.8 MiB,``60cc5874b3cce9d80a38fb2b28df96d880e8e95d1b5848b15c20f1181e2807db``
   Python 3.7,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.12.0-Windows-x86.exe>`_,65.5 MiB,``a6af674b984a333b53aaf99043f6af4f50b0bb2ab78e0b732aa60c47bbfb0704``


macOS installers
=================

.. csv-table:: macOS
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.10,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.1.0-1-MacOSX-x86_64.sh>`_,43.0 MiB,``bfb81814e16eb450b1dbde7b4ecb9ebc5186834cb4ede5926c699762ca69953b``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.1.0-1-MacOSX-x86_64.pkg>`_,42.8 MiB,``bcc0067864011a93083ff2d6fe7b29e877c1477f24ee9d34b54d0165f8b32f11``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.1.0-1-MacOSX-arm64.sh>`_,41.7 MiB,``cc5bcf95d5db0f7f454b2d800d52da8b70563f8454d529e7ac2da9725650eb27``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.1.0-1-MacOSX-arm64.pkg>`_,41.4 MiB,``09d893e44400f61d36daeaa9befff8219a7e0127358d904a4368b2f0ae738df0``
   Python 3.9,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.1.0-1-MacOSX-x86_64.sh>`_,43.3 MiB,``d78eaac94f85bacbc704f629bdfbc2cd42a72dc3a4fd383a3bfc80997495320e``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.1.0-1-MacOSX-x86_64.pkg>`_,43.1 MiB,``878c7939731a712ba3dccfccf8df3c0ac8e5a7d7486b43bfc9e422907ecf8ca5``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.1.0-1-MacOSX-arm64.sh>`_,43.0 MiB,``a7133a703e41ea0b1738196fb03f72b22250327adea94521c9dd6100c304dc63``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.1.0-1-MacOSX-arm64.pkg>`_,42.7 MiB,``b09fa8474db00127701a670886e8608da6e00c4be97d93f5dd57bbd497cdb92a``
   Python 3.8,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.1.0-1-MacOSX-x86_64.sh>`_,43.3 MiB,``5d789cda38b23245ffed6b88c60b7479d984bbf20e3b70d66cd150f04a9c25c5``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.1.0-1-MacOSX-x86_64.pkg>`_,43.1 MiB,``beed5074ac12b9ef2820f03a3a0efe910cdd545af8fe0aad1d9c190173150f88``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.1.0-1-MacOSX-arm64.sh>`_,42.9 MiB,``8dfab7797151a31b16c174da9a5bc09529d5859f21e77f0655ea9b18209cc926``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.1.0-1-MacOSX-arm64.pkg>`_,42.6 MiB,``975d6daa8afd01459b99b924703494a23519ed113bac5ba7f7db355904f37b22``
   Python 3.7,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py37_23.1.0-1-MacOSX-x86_64.sh>`_,53.3 MiB,``bdfb2f01c0a3917bf258daffc65b69bfe07e29753be624aaf9cbda5ba02f43f4``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py37_23.1.0-1-MacOSX-x86_64.pkg>`_,53.0 MiB,``0384041d2ccf777d88ec7ce9326ee15140becbd5faa0fb2cd1269d1e4cc8fc6f``

Linux installers
================

.. csv-table:: Linux
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.10,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.1.0-1-Linux-x86_64.sh>`_,71.0 MiB,``32d73e1bc33fda089d7cd9ef4c1be542616bd8e437d1f77afeeaf7afdb019787``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.1.0-1-Linux-aarch64.sh>`_,51.6 MiB,``80d6c306b015e1e3b01ea59dc66c676a81fa30279bc2da1f180a7ef7b2191d6e``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.1.0-1-Linux-ppc64le.sh>`_,52.4 MiB,``9ca8077a0af8845fc574a120ef8d68690d7a9862d354a2a4468de5d2196f406c``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.1.0-1-Linux-s390x.sh>`_,67.6 MiB,``0d00a9d34c5fd17d116bf4e7c893b7441a67c7a25416ede90289d87216104a97``
   Python 3.9,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.1.0-1-Linux-x86_64.sh>`_,66.7 MiB,``5dc619babc1d19d6688617966251a38d245cb93d69066ccde9a013e1ebb5bf18``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.1.0-1-Linux-aarch64.sh>`_,60.5 MiB,``5e67416a574c49e19dc21d5b9ed586400863a685bc4e34b4d933ea8c7c1ed2da``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.1.0-1-Linux-ppc64le.sh>`_,60.6 MiB,``cf5d7cad2b0eb260903b3661ee3fa822eecb25cf3c9b14bc9de10d72963d3d5a``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.1.0-1-Linux-s390x.sh>`_,62.8 MiB,``5159322f15d9e2b22b3cf90fe88b336d84f62189178c872a9288a339d86f5d20``
   Python 3.8,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.1.0-1-Linux-x86_64.sh>`_,65.4 MiB,``640b7dceee6fad10cb7e7b54667b2945c4d6f57625d062b2b0952b7f3a908ab7``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.1.0-1-Linux-aarch64.sh>`_,48.2 MiB,``10ea91cc579a64a3a88727119ac3f55839562f55118458b82824b544bc74f90d``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.1.0-1-Linux-ppc64le.sh>`_,48.5 MiB,``d89faee2d839c7e8a2c96f3ca60295c08e837c2f134f6bb9e9e21b707babedc2``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.1.0-1-Linux-s390x.sh>`_,61.5 MiB,``3d1e06eddaef0976530c54ed7dda80df62705c16513634e58f7d1c4567227b9e``
   Python 3.7,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_23.1.0-1-Linux-x86_64.sh>`_,86.5 MiB,``fc96109ea96493e31f70abbc5cae58e80634480c0686ab46924549ac41176812``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_23.1.0-1-Linux-aarch64.sh>`_,80.7 MiB,``31c1d635fae931b7c0687018cc87e918e8098ed5dd5e76a658e10c57e00ef864``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_23.1.0-1-Linux-ppc64le.sh>`_,81.2 MiB,``d2de534bfa46aa34ef0b115a309de7e8a681683af65faf86bcee6a00460f07be``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_23.1.0-1-Linux-s390x.sh>`_,82.8 MiB,``72a8fa9aca5abaf99771110746b1345a33d390c9b29a7b4daffe6a2ff00f2366``

Installing
==========
- :doc:`See hashes for all Miniconda installers <../miniconda_hashes>`.
- `Verify your installation <https://conda.io/projects/conda/en/stable/user-guide/install/download.html#cryptographic-hash-verification>`_.
- `Installation
  instructions <https://conda.io/projects/conda/en/stable/user-guide/install/index.html>`__.

Other resources
===============

 -  `Miniconda Docker
    images <https://hub.docker.com/r/continuumio/>`__
 -  `Miniconda AWS
    images <https://aws.amazon.com/marketplace/seller-profile?id=29f81979-a535-4f44-9e9f-6800807ad996>`__
 -  `Archive and SHA256 sums for the
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
 instance, the behavior of:

 .. container:: highlight-bash notranslate

    .. container:: highlight

       ::

          $ conda create -n myenv python

 will be to install Python 2.7 with the Python 2
 Miniconda and to install Python 3.10 with the Python
 3 Miniconda. You can override the default by
 explicitly setting ``python=2`` or ``python=3``. It
 also determines the default value of ``CONDA_PY``
 when using ``conda build``.

 .. note::
    If you already have Miniconda or Anaconda
    installed, and you just want to upgrade, you should
    not use the installer. Just use ``conda update``.

 For instance:

 .. container:: highlight-bash notranslate

    .. container:: highlight

       ::

          $ conda update conda

 will update conda.
