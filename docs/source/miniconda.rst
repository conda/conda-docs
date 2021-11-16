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

`See if Miniconda is right for you <https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html#anaconda-or-miniconda>`_.

System requirements
===================

* License: Free use and redistribution under the terms of the `EULA for Miniconda <https://www.anaconda.com/end-user-license-agreement-miniconda>`_. 
* Operating system: Windows 8 or newer, 64-bit macOS 10.13+, or Linux, including Ubuntu, RedHat, CentOS 7+, and others.
* If your operating system is older than what is currently supported, you can find older versions of the Miniconda installers in our `archive <https://repo.anaconda.com/miniconda/>`_ that might work for you. 
* System architecture: Windows- 64-bit x86, 32-bit x86; macOS- 64-bit x86 & Apple M1 (ARM64); Linux- 64-bit x86, 64-bit aarch64 (AWS Graviton2 / ARM64), 64-bit IBM Power8/Power9, s390x (Linux on IBM Z & LinuxONE).
* Minimum 400 MB disk space to download and install.

On Windows, macOS, and Linux, it is best to install Miniconda for the local user,
which does not require administrator permissions and is the most robust type of
installation. However, if you need to, you can install Miniconda system wide,
which does require administrator permissions.

Latest Miniconda Installer Links
================================

.. csv-table:: Latest - Conda 4.10.3 Python 3.9.5 released July 21, 2021
   :header: Platform,Name,SHA256 hash
   :widths: 5, 10, 80

   Windows,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe>`_,``b33797064593ab2229a0135dc69001bea05cb56a20c2f243b1231213642e260a``
   ,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86.exe>`_,``24f438e57ff2ef1ce1e93050d4e9d13f5050955f759f448d84a4018d3cd12d6b``
   MacOSX,`Miniconda3 maxOSX 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh>`_,``786de9721f43e2c7d2803144c635f5f6e4823483536dc141ccd82dbb927cd508``
   ,`Miniconda3 maxOSX 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg>`_,``8fa371ae97218c3c005cd5f04b1f40156d1506a9bd1d5c078f89d563fd416816``
   ,`Miniconda3 maxOS Apple M1 64-bit bash (Py38 conda 4.10.1 2021-11-08) <Miniconda3-latest-MacOSX-arm64.sh>`_,``4ce4047065f32e991edddbb63b3c7108e7f4534cfc1efafc332454a414deab58``   
   Linux,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh>`_,``1ea2f885b4dbc3098662845560bc64271eb17085387a70c2ba3f29fff6f8d52f``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh>`_,``4879820a10718743f945d88ef142c3a4b30dfc8e448d1ca08e019586374b773f``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-ppc64le.sh>`_,``fa92ee4773611f58ed9333f977d32bbb64769292f605d518732183be1f3321fa``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-s390x.sh>`_,``1faed9abecf4a4ddd4e0d8891fc2cdaa3394c51e877af14ad6b9d4aadb4e90d8``

Windows installers
==================

.. csv-table:: Windows
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.9,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Windows-x86_64.exe>`_,58.1 MiB,``b33797064593ab2229a0135dc69001bea05cb56a20c2f243b1231213642e260a``
   Python 3.8,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.10.3-Windows-x86_64.exe>`_,57.3 MiB,``8940cdd621557bc55743d6bb4518c6d343a4587127e76de808fb07e51df03fea``
   Python 3.7,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.10.3-Windows-x86_64.exe>`_,55.8 MiB,``9c031506bfcb0428a0ac46c9152f9bdd48d5bdaa83046691bf8e0a4480663c05``
   Python 3.9,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Windows-x86.exe>`_,55.3 MiB,``24f438e57ff2ef1ce1e93050d4e9d13f5050955f759f448d84a4018d3cd12d6b``
   Python 3.8,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.10.3-Windows-x86.exe>`_,54.5 MiB,``f81c165384c18d1986e2ba2f86cef384bc62266c46b34cd3d274e751ff5d91ed``
   Python 3.7,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.10.3-Windows-x86.exe>`_,55.3 MiB,``a1bb8338be12ee09dbd4cab9dcc2fbdc99f65d99281dd2c07d24ad0f23dd1f7c``


macOS installers
=================

.. csv-table:: macOS
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.9,`Miniconda3 macOS 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-MacOSX-x86_64.sh>`_,42.3 MiB,``786de9721f43e2c7d2803144c635f5f6e4823483536dc141ccd82dbb927cd508``
   ,`Miniconda3 macOS 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-MacOSX-x86_64.pkg>`_,49.9 MiB,``8fa371ae97218c3c005cd5f04b1f40156d1506a9bd1d5c078f89d563fd416816``
   Python 3.8,`Miniconda3 macOS 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.10.3-MacOSX-x86_64.sh>`_,53.3 MiB,``93e514e01142866629175f5a9e2e1d0bac8bc705f61d1ed1da3c010b7225683a``
   ,`Miniconda3 macOS 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.10.3-MacOSX-x86_64.pkg>`_,60.8 MiB,``faab44cd21b4b09f5c032aa49a8a23d3c53ef629dc9322411348ce413e41df35``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.10.1-MacOSX-arm64.sh>`_,44.9 MiB,``4ce4047065f32e991edddbb63b3c7108e7f4534cfc1efafc332454a414deab58``   
   Python 3.7,`Miniconda3 macOS 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.10.3-MacOSX-x86_64.sh>`_,50.6 MiB,``ca7492d456c319d15682b2d3845112a631365f293d38d1f62872c33a2e57e430``
   ,`Miniconda3 macOS 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.10.3-MacOSX-x86_64.pkg>`_,58.1 MiB,``c3710f25748884741ef8d97777ebb3541c992d51130298830b5b9ad449dbbf1e``

Linux installers
================

.. csv-table:: Linux
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.9,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh>`_,63.6 MiB,``1ea2f885b4dbc3098662845560bc64271eb17085387a70c2ba3f29fff6f8d52f``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-aarch64.sh>`_,62.6 MiB,``4879820a10718743f945d88ef142c3a4b30dfc8e448d1ca08e019586374b773f``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-ppc64le.sh>`_,60.6 MiB,``fa92ee4773611f58ed9333f977d32bbb64769292f605d518732183be1f3321fa``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-s390x.sh>`_,57.1 MiB,``1faed9abecf4a4ddd4e0d8891fc2cdaa3394c51e877af14ad6b9d4aadb4e90d8``
   Python 3.8,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.10.3-Linux-x86_64.sh>`_,98.8 MiB,``935d72deb16e42739d69644977290395561b7a6db059b316958d97939e9bdf3d``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.10.3-Linux-aarch64.sh>`_,94.8 MiB,``19584b4fb5c0656e0cf9de72aaa0b0a7991fbd6f1254d12e2119048c9a47e5cc``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.10.3-Linux-ppc64le.sh>`_,93.3 MiB,``c1ac79540cb77b2e0ca5b9f78b3bc367567d810118500a167dea4a0bcab5d063``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.10.3-Linux-s390x.sh>`_,89.0 MiB,``55f514110a50e98549a68912cbb03e43a36193940a1889e1c8beb30009b4da19``
   Python 3.7,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.10.3-Linux-x86_64.sh>`_,84.9 MiB,``a1a7285dea0edc430b2bc7951d89bb30a2a1b32026d2a7b02aacaaa95cf69c7c``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.10.3-Linux-aarch64.sh>`_,89.2 MiB,``65f400a906e3132ddbba35a38d619478be77d32210a2acab05133d92ba08f111``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.10.3-Linux-ppc64le.sh>`_,88.1 MiB,``e4f8b4a5eb8da1badf0b0c91fd7ee25e39120d4d77443e7a1ef3661fd439a997``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.10.3-Linux-s390x.sh>`_,84.1 MiB,``7ab9f813dd84cb0951a2d755cd84708263ce4e03c656e65e2fa79ed0f024f0f7``

Installing
==========
- :doc:`See hashes for all Miniconda installers <../miniconda_hashes>`.
- `Verify your installation <https://conda.io/projects/conda/en/latest/user-guide/install/download.html#cryptographic-hash-verification>`_.
- `Installation
  instructions <https://conda.io/projects/conda/en/latest/user-guide/install/index.html>`__.

Other resources
===============

 -  `Miniconda with Python 3.9 for Power8 &
    Power9 <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-ppc64le.sh>`__
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
 instance, the behavior of:

 .. container:: highlight-bash notranslate

    .. container:: highlight

       ::

          $ conda create -n myenv python

 will be to install Python 2.7 with the Python 2
 Miniconda and to install Python 3.8 with the Python
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
