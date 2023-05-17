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

* License: Free use and redistribution under the terms of the `EULA for Miniconda <https://legal.anaconda.com/policies/en?name=offering-specific-terms#miniconda>`_.
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

.. csv-table:: Latest - Conda 23.3.1 Python 3.10.10 released April 24, 2023
   :header: Platform,Name,SHA256 hash
   :widths: 5, 10, 80

   Windows,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe>`_,``307194e1f12bbeb52b083634e89cc67db4f7980bd542254b43d3309eaf7cb358``
   ,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86.exe>`_,``4fb64e6c9c28b88beab16994bfba4829110ea3145baa60bda5344174ab65d462``
   macOS,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh>`_,``5abc78b664b7da9d14ade330534cc98283bb838c6b10ad9cfd8b9cc4153f8104``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg>`_,``cca31a0f1e5394f2b739726dc22551c2a19afdf689c13a25668887ba706cba58``
   ,`Miniconda3 macOS Apple M1 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh>`_,``9d1d12573339c49050b0d5a840af0ff6c32d33c3de1b3db478c01878eb003d64``
   ,`Miniconda3 macOS Apple M1 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.pkg>`_,``6997472c5ff90a772eb77e6397f4e3e227736c83a7f7b839da33d6cc7facb75d``
   Linux,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh>`_,``aef279d6baea7f67940f16aad17ebe5f6aac97487c7c03466ff01f4819e5a651``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh>`_,``6950c7b1f4f65ce9b87ee1a2d684837771ae7b2e6044e0da9e915d1dee6c924c``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-ppc64le.sh>`_,``b3de538cd542bc4f5a2f2d2a79386288d6e04f0e1459755f3cefe64763e51d16``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-s390x.sh>`_,``ed4f51afc967e921ff5721151f567a4c43c4288ac93ec2393c6238b8c4891de8``

Windows installers
==================

.. csv-table:: Windows
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.10,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-Windows-x86_64.exe>`_,53.9 MiB,``307194e1f12bbeb52b083634e89cc67db4f7980bd542254b43d3309eaf7cb358``
   Python 3.9,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-Windows-x86_64.exe>`_,53.7 MiB,``155958e7922d8b7aa6cb3115aeb66d2efcdae1237a6f1c11e23ca75ea96d291a``
   Python 3.8,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.3.1-0-Windows-x86_64.exe>`_,53.1 MiB,``f567b46b2312af5e60ec8f45daf9be626295b7716651e6e7434c447feea9123a``
   Python 3.7,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_23.3.1-0-Windows-x86_64.exe>`_,,````
   Python 3.9,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Windows-x86.exe>`_,67.8 MiB,``4fb64e6c9c28b88beab16994bfba4829110ea3145baa60bda5344174ab65d462``
   Python 3.8,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Windows-x86.exe>`_,66.8 MiB,``60cc5874b3cce9d80a38fb2b28df96d880e8e95d1b5848b15c20f1181e2807db``
   Python 3.7,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.12.0-Windows-x86.exe>`_,,````


macOS installers
=================

.. csv-table:: macOS
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.10,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-MacOSX-x86_64.sh>`_,44.1 MiB,``5abc78b664b7da9d14ade330534cc98283bb838c6b10ad9cfd8b9cc4153f8104``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-MacOSX-x86_64.pkg>`_,43.8 MiB,``cca31a0f1e5394f2b739726dc22551c2a19afdf689c13a25668887ba706cba58``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-MacOSX-arm64.sh>`_,42.6 MiB,``9d1d12573339c49050b0d5a840af0ff6c32d33c3de1b3db478c01878eb003d64``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-MacOSX-arm64.pkg>`_,42.3 MiB,``6997472c5ff90a772eb77e6397f4e3e227736c83a7f7b839da33d6cc7facb75d``
   Python 3.9,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-MacOSX-x86_64.sh>`_,44.4 MiB,``54d739715feb0cd5c127865215cc9f50697709d71e9ee7da430576c5a1c8010d``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-MacOSX-x86_64.pkg>`_,44.1 MiB,``6960a11f74a0717adaacdc979d1817f5d0e3612d2ef7a409d547fbeac6d58ed7``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-MacOSX-arm64.sh>`_,43.0 MiB,``c74474bab188b8b3dcaf0f0ca52f5e0743591dbe171766016023d052acf96502``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-MacOSX-arm64.pkg>`_,42.7 MiB,``9bc8a8fde9d01e26ee37a6611a92a66d36db66ff82e76bd4f18cb28cfbad7a1f``
   Python 3.8,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.3.1-0-MacOSX-x86_64.sh>`_,44.2 MiB,``eb7b2d285f6d3b7c9cde9576c8c647e70b65361426b0e0e069b4ab23ccbb79e2``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.3.1-0-MacOSX-x86_64.pkg>`_,43.9 MiB,``23d6fa672be46632abd0bbed1f12ce9542a6cb4a38922dab503d9a6096d186d3``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.3.1-0-MacOSX-arm64.sh>`_,42.9 MiB,``e0151c68f6a11a38b29c2f4a775bf6a22187fa2c8ca0f31930d69f2f013c0810``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.3.1-0-MacOSX-arm64.pkg>`_,42.6 MiB,``6714fdefd12e1a65c7fd344f3829a4b054ae42d3d1368b07ceeab9dcc41ad48b``
   Python 3.7,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py37_23.3.1-0-MacOSX-x86_64.sh>`_,,````
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py37_23.3.1-0-MacOSX-x86_64.pkg>`_,,````

Linux installers
================

.. csv-table:: Linux
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.10,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-Linux-x86_64.sh>`_,69.7 MiB,``aef279d6baea7f67940f16aad17ebe5f6aac97487c7c03466ff01f4819e5a651``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-Linux-aarch64.sh>`_,50.3 MiB,``6950c7b1f4f65ce9b87ee1a2d684837771ae7b2e6044e0da9e915d1dee6c924c``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-Linux-ppc64le.sh>`_,50.8 MiB,``b3de538cd542bc4f5a2f2d2a79386288d6e04f0e1459755f3cefe64763e51d16``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.3.1-0-Linux-s390x.sh>`_,66.0 MiB,``ed4f51afc967e921ff5721151f567a4c43c4288ac93ec2393c6238b8c4891de8``
   Python 3.9,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-Linux-x86_64.sh>`_,67.3 MiB,``1564571a6a06a9999a75a6c65d63cb82911fc647e96ba5b729f904bf00c177d3``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-Linux-aarch64.sh>`_,61.0 MiB,``e93ccab720b57f821e0d758f54e9aee9bd2f0ea931ebb26b78d866704437a296``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-Linux-ppc64le.sh>`_,61.2 MiB,``d2bcef86812863adaf11fcda6df829aa508760cbde4a19174cf0fec03e8498f5``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.3.1-0-Linux-s390x.sh>`_,63.3 MiB,``d0b658566edd239dd50fc28ab1d3a57b8b0da707481b3b18c27d11273c4fdb5a``
   Python 3.8,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.3.1-0-Linux-x86_64.sh>`_,65.8 MiB,``d1f3a4388c1a6fd065e32870f67abc39eb38f4edd36c4947ec7411e32311bd59``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.3.1-0-Linux-aarch64.sh>`_,48.8 MiB,``ad491ebad6efec7470fe2139c8b407a895cb2c828b3233b97da6e4f22cae0cde``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.3.1-0-Linux-ppc64le.sh>`_,49.3 MiB,``8aa819800ba3ec88ad8518a9e4fc71ada8087547300fc53527c4ecc8072a4d50``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.3.1-0-Linux-s390x.sh>`_,62.0 MiB,``e4d83bb9f0900c9128504f7e3c4d3b9e5eaf3b87c4bb5190a3086947e92bd3fa``
   Python 3.7,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_23.3.1-0-Linux-x86_64.sh>`_,,````
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_23.3.1-0-Linux-aarch64.sh>`_,,````
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_23.3.1-0-Linux-ppc64le.sh>`_,,````
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_23.3.1-0-Linux-s390x.sh>`_,,````

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
