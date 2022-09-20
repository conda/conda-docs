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
* System architecture: Windows- 64-bit x86, 32-bit x86; macOS- 64-bit x86 & Apple M1 (ARM64); Linux- 64-bit x86, 64-bit aarch64 (AWS Graviton2), 64-bit IBM Power8/Power9, s390x (Linux on IBM Z & LinuxONE).
* The ``linux-aarch64`` Miniconda installer requires ``glibc >=2.26`` and thus will **not** work with CentOS 7, Ubuntu 16.04, or Debian 9 ("stretch").
* Minimum 400 MB disk space to download and install.

On Windows, macOS, and Linux, it is best to install Miniconda for the local user,
which does not require administrator permissions and is the most robust type of
installation. However, if you need to, you can install Miniconda system wide,
which does require administrator permissions.

Latest Miniconda Installer Links
================================

.. csv-table:: Latest - Conda 4.12.0 Python 3.9.7 released February 15, 2022
   :header: Platform,Name,SHA256 hash
   :widths: 5, 10, 80

   Windows,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe>`_,``1acbc2e8277ddd54a5f724896c7edee112d068529588d944702966c867e7e9cc``
   ,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86.exe>`_,``4fb64e6c9c28b88beab16994bfba4829110ea3145baa60bda5344174ab65d462``
   macOS,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh>`_,``007bae6f18dc7b6f2ca6209b5a0c9bd2f283154152f82becf787aac709a51633``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg>`_,``cb56184637711685b08f6eba9532cef6985ed7007b38e789613d5dd3f94ccc6b``
   ,`Miniconda3 macOS Apple M1 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh>`_,``4bd112168cc33f8a4a60d3ef7e72b52a85972d588cd065be803eb21d73b625ef``
   ,`Miniconda3 macOS Apple M1 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.pkg>`_,``0cb5165ca751e827d91a4ae6823bfda24d22c398a0b3b01213e57377a2c54226``
   Linux,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh>`_,``78f39f9bae971ec1ae7969f0516017f2413f17796670f7040725dd83fcff5689``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh>`_,``5f4f865812101fdc747cea5b820806f678bb50fe0a61f19dc8aa369c52c4e513``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-ppc64le.sh>`_,``1fe3305d0ccc9e55b336b051ae12d82f33af408af4b560625674fa7ad915102b``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-s390x.sh>`_,``ff6fdad3068ab5b15939c6f422ac329fa005d56ee0876c985e22e622d930e424``

Windows installers
==================

.. csv-table:: Windows
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.9,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Windows-x86_64.exe>`_,71.2 MiB,``1acbc2e8277ddd54a5f724896c7edee112d068529588d944702966c867e7e9cc``
   Python 3.8,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Windows-x86_64.exe>`_,70.6 MiB,``94f24e52e316fa935ccf94b0c504ceca8e6abc6190c68378e18550c95bb7cee1``
   Python 3.7,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.12.0-Windows-x86_64.exe>`_,69.0 MiB,``b221ccdb2bbc5a8209a292f858ae05fd87f882f79be75b37d26faa881523c057``
   Python 3.9,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Windows-x86.exe>`_,67.8 MiB,``4fb64e6c9c28b88beab16994bfba4829110ea3145baa60bda5344174ab65d462``
   Python 3.8,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Windows-x86.exe>`_,66.8 MiB,``60cc5874b3cce9d80a38fb2b28df96d880e8e95d1b5848b15c20f1181e2807db``
   Python 3.7,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.12.0-Windows-x86.exe>`_,65.5 MiB,``a6af674b984a333b53aaf99043f6af4f50b0bb2ab78e0b732aa60c47bbfb0704``


macOS installers
=================

.. csv-table:: macOS
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.9,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-MacOSX-x86_64.sh>`_,56.0 MiB,``007bae6f18dc7b6f2ca6209b5a0c9bd2f283154152f82becf787aac709a51633``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-MacOSX-x86_64.pkg>`_,62.7 MiB,``cb56184637711685b08f6eba9532cef6985ed7007b38e789613d5dd3f94ccc6b``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-MacOSX-arm64.sh>`_,52.2 MiB,``4bd112168cc33f8a4a60d3ef7e72b52a85972d588cd065be803eb21d73b625ef``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-MacOSX-arm64.pkg>`_,63.5 MiB,``0cb5165ca751e827d91a4ae6823bfda24d22c398a0b3b01213e57377a2c54226``
   Python 3.8,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-MacOSX-x86_64.sh>`_,56.4 MiB,``f930f5b1c85e509ebbf9f28e13c697a082581f21472dc5360c41905d10802c7b``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-MacOSX-x86_64.pkg>`_,63.1 MiB,``62eda1322b971d43409e5dde8dc0fd7bfe799d18a49fb2d8d6ad1f6833448f5c``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-MacOSX-arm64.sh>`_,52.5 MiB,``13b992328ef088a49a685ae84461f132f8719bf0cabc43792fc9009b0421f611``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-MacOSX-arm64.pkg>`_,63.8 MiB,``e92fd40710f7123d9e1b2d44f71e7b2101e3397049b87807ccf612c964beef35``
   Python 3.7,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.12.0-MacOSX-x86_64.sh>`_,66.0 MiB,``323179e4873e291f07db041f3d968da2ffc102dcf709915b48a253914d981868``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.12.0-MacOSX-x86_64.pkg>`_,72.7 MiB,``9278875a235ef625d581c63b46129b27373c3cf5516d36250a1a3640978280cd``

Linux installers
================

.. csv-table:: Linux
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.9,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh>`_,73.1 MiB,``78f39f9bae971ec1ae7969f0516017f2413f17796670f7040725dd83fcff5689``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-aarch64.sh>`_,75.3 MiB,``5f4f865812101fdc747cea5b820806f678bb50fe0a61f19dc8aa369c52c4e513``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-ppc64le.sh>`_,74.3 MiB,``1fe3305d0ccc9e55b336b051ae12d82f33af408af4b560625674fa7ad915102b``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-s390x.sh>`_,69.2 MiB,``ff6fdad3068ab5b15939c6f422ac329fa005d56ee0876c985e22e622d930e424``
   Python 3.8,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-x86_64.sh>`_,72.6 MiB,``3190da6626f86eee8abf1b2fd7a5af492994eb2667357ee4243975cdbb175d7a``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-aarch64.sh>`_,64.4 MiB,``0c20f121dc4c8010032d64f8e9b27d79e52d28355eb8d7972eafc90652387777``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-ppc64le.sh>`_,65.9 MiB,``4be4086710845d10a8911856e9aea706c1464051a24c19aabf7f6e1a1aedf454``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-s390x.sh>`_,68.7 MiB,``3125961430c77eae81556fa59fe25dca9e5808f76c05f87092d6f2d57f85e933``
   Python 3.7,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.12.0-Linux-x86_64.sh>`_,100.1 MiB,``4dc4214839c60b2f5eb3efbdee1ef5d9b45e74f2c09fcae6c8934a13f36ffc3e``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.12.0-Linux-aarch64.sh>`_,101.7 MiB,``47affd9577889f80197aadbdf1198b04a41528421aaf0ec1f28b04a50b9f3ab8``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.12.0-Linux-ppc64le.sh>`_,101.4 MiB,``c99b66a726a5116f7c825f9535de45fcac9e4e8ae825428abfb190f7748a5fd0``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.12.0-Linux-s390x.sh>`_,95.9 MiB,``8401eb61094297cc53709fec4654695d59652b3adde241963d3d993a6d760ed5``

Installing
==========
- :doc:`See hashes for all Miniconda installers <../miniconda_hashes>`.
- `Verify your installation <https://conda.io/projects/conda/en/latest/user-guide/install/download.html#cryptographic-hash-verification>`_.
- `Installation
  instructions <https://conda.io/projects/conda/en/latest/user-guide/install/index.html>`__.

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
