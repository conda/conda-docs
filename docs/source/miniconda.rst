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
* Operating system: Windows 10 or newer, 64-bit macOS 10.13+, or Linux, including Ubuntu, RedHat, CentOS 7+, and others.
* If your operating system is older than what is currently supported, you can find older versions of the Miniconda installers in our `archive <https://repo.anaconda.com/miniconda/>`_ that might work for you.
* System architecture: Windows- 64-bit x86, 32-bit x86; macOS- 64-bit x86 & Apple M1 (ARM64); Linux- 64-bit x86, 64-bit aarch64 (AWS Graviton2), 64-bit IBM Power8/Power9, s390x (Linux on IBM Z & LinuxONE).
* The ``linux-aarch64`` Miniconda installer requires ``glibc >=2.26`` and thus will **not** work with CentOS 7, Ubuntu 16.04, or Debian 9 ("stretch").
* Minimum 400 MB disk space to download and install.

On Windows, macOS, and Linux, it is best to install Miniconda for the local user,
which does not require administrator permissions and is the most robust type of
installation. However, if you need to, you can install Miniconda system wide,
which does require administrator permissions.

Installing
==========
- :doc:`See hashes for all Miniconda installers <../miniconda_hashes>`.
- `Verify your installation <https://conda.io/projects/conda/en/stable/user-guide/install/download.html#cryptographic-hash-verification>`_.
- `Installation
  instructions <https://conda.io/projects/conda/en/stable/user-guide/install/index.html>`__.

Latest Miniconda Installer Links
================================

.. csv-table:: Latest - Conda 23.5.0 Python 3.11.3 released July 11, 2023
   :header: Platform,Name,SHA256 hash
   :widths: 5, 10, 80

   Windows,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe>`_,``51a50e2997bc4ec9361733f90cb1ed343910fbc73e8a2b01b86e514921f1c026``
   ,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86.exe>`_,``4fb64e6c9c28b88beab16994bfba4829110ea3145baa60bda5344174ab65d462``
   macOS,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh>`_,``2503d9e852fcaf85adca825bde84bdc297b118fd2c14316e4f27a93a190a7bdd``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg>`_,``2f9a3ccb69c146a748c1270a625a481f73c49d714a35c5ea84399e32892af830``
   ,`Miniconda3 macOS Apple M1 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh>`_,``c4ce7311d2d1c729bf8d98e6d5aa2581ce0b08a1480985e63efaf8529b2fc6ca``
   ,`Miniconda3 macOS Apple M1 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.pkg>`_,``b0eba1878ce8d4f0c36bead75e849a5f513055756d794344ff6b371e47b66cbe``
   Linux,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh>`_,``61a5c087893f6210176045931b89ee6e8760c17abd9c862b2cab4c1b7d00f7c8``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh>`_,``6e3e60e7093194b3435fde19efc54d0dd78be393bf5b7487cc28cd1039ebed4d``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-ppc64le.sh>`_,``c1ab8b5d629f66a1609e456a0d6a83a2896af6dc0b2b702025cb19456030eacd``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-s390x.sh>`_,``42e7cc490fc81d9b1dc56cf8bd951e084e804824d60aca3a4b15d35c57ad373e``

Windows installers
==================

.. csv-table:: Windows
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.11,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.0-3-Windows-x86_64.exe>`_,73.2 MiB,``51a50e2997bc4ec9361733f90cb1ed343910fbc73e8a2b01b86e514921f1c026``
   Python 3.10,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.0-3-Windows-x86_64.exe>`_,69.5 MiB,``cb4e61bc59068a5e3732a2a58b0414c970848d3499c64c725ccd7d0000964335``
   Python 3.9,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.0-3-Windows-x86_64.exe>`_,70.0 MiB,``0b457f3279409325eb95939a69a2cbd81d3cfb8d5df672b85315c14eb0ee9544``
   ,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Windows-x86.exe>`_,67.8 MiB,``4fb64e6c9c28b88beab16994bfba4829110ea3145baa60bda5344174ab65d462``
   Python 3.8,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.5.0-3-Windows-x86_64.exe>`_,71.0 MiB,``a643675ca68f7c0577864e20f73615a52aeb9c07663576411a86964326fe4288``
   ,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Windows-x86.exe>`_,66.8 MiB,``60cc5874b3cce9d80a38fb2b28df96d880e8e95d1b5848b15c20f1181e2807db``

macOS installers
================

.. csv-table:: macOS
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.11,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.0-3-MacOSX-x86_64.sh>`_,69.6 MiB,``2503d9e852fcaf85adca825bde84bdc297b118fd2c14316e4f27a93a190a7bdd``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.0-3-MacOSX-x86_64.pkg>`_,69.2 MiB,``2f9a3ccb69c146a748c1270a625a481f73c49d714a35c5ea84399e32892af830``
   ,`Miniconda3 macOS Apple M1 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.0-3-MacOSX-arm64.sh>`_,68.6 MiB,``c4ce7311d2d1c729bf8d98e6d5aa2581ce0b08a1480985e63efaf8529b2fc6ca``
   ,`Miniconda3 macOS Apple M1 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.0-3-MacOSX-arm64.pkg>`_,68.2 MiB,``b0eba1878ce8d4f0c36bead75e849a5f513055756d794344ff6b371e47b66cbe``
   Python 3.10,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.0-3-MacOSX-x86_64.sh>`_,65.6 MiB,``03a98ff5d1c813d7bf969203fe404d7a6f149b335c2077703656807721603495``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.0-3-MacOSX-x86_64.pkg>`_,65.3 MiB,``4cbc8d3bec69286364c4fe5b02e88b8059de4ffbb4707f1e589c5deef1a210ff``
   ,`Miniconda3 macOS Apple M1 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.0-3-MacOSX-arm64.sh>`_,64.6 MiB,``ff2121c0a8245bbe63ff70cdb76b492c831889225f9c5277e096f08fd03e7f17``
   ,`Miniconda3 macOS Apple M1 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.0-3-MacOSX-arm64.pkg>`_,64.2 MiB,``a6dbd3472410e6afa8b56bf80f2083d2d8ac0922c0d9c07b818c9a131662bb59``
   Python 3.9,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.0-3-MacOSX-x86_64.sh>`_,65.0 MiB,``86ae780b5c5a32c45bc0f2e146941afea6dd1ca48e8d5e1bf99a83df255a0a78``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.0-3-MacOSX-x86_64.pkg>`_,64.6 MiB,``3a75740b5798e48f22538c7cff4b3d9d9549df4eda5e7a6ced5ebc3eab10f297``
   ,`Miniconda3 macOS Apple M1 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.0-3-MacOSX-arm64.sh>`_,64.1 MiB,``d006d99f86850510f9aed1a81e16a4213a4829e7ea6913f0c42054b4b0ac05a7``
   ,`Miniconda3 macOS Apple M1 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.0-3-MacOSX-arm64.pkg>`_,63.7 MiB,``7669a7826ac1195483ca2abd51b7f749620db3aff2f3851670441fc56652a35b``
   Python 3.8,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.5.0-3-MacOSX-x86_64.sh>`_,66.5 MiB,``54ead65ad1ff77d9cba2512a8765d64e6b7d8ae154e2fc1a6fcb01395b9a8cf3``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.5.0-3-MacOSX-x86_64.pkg>`_,66.2 MiB,``1f53b13e8224b40ad9292c4884c3052359b1826a90b49f4e4724affa10d31bb6``
   ,`Miniconda3 macOS Apple M1 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.5.0-3-MacOSX-arm64.sh>`_,65.7 MiB,``5daf6837136d08a17f039b29993f67207ba90dcc90abe94c6d5a8925f6888076``
   ,`Miniconda3 macOS Apple M1 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.5.0-3-MacOSX-arm64.pkg>`_,65.3 MiB,``789317cc46f3d1766fe44b701c435f5505318c60eb18d607401b30a9cd7bcc3c``

Linux installers
================

.. csv-table:: Linux
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.11,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.0-3-Linux-x86_64.sh>`_,98.4 MiB,``61a5c087893f6210176045931b89ee6e8760c17abd9c862b2cab4c1b7d00f7c8``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.0-3-Linux-aarch64.sh>`_,76.4 MiB,``6e3e60e7093194b3435fde19efc54d0dd78be393bf5b7487cc28cd1039ebed4d``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.0-3-Linux-ppc64le.sh>`_,77.4 MiB,``c1ab8b5d629f66a1609e456a0d6a83a2896af6dc0b2b702025cb19456030eacd``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.0-3-Linux-s390x.sh>`_,94.5 MiB,``42e7cc490fc81d9b1dc56cf8bd951e084e804824d60aca3a4b15d35c57ad373e``
   Python 3.10,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.0-3-Linux-x86_64.sh>`_,91.4 MiB,``738890e7a6f0719a942c632a0aab1df7a5a592c5667d0495d1f0495990a709ba``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.0-3-Linux-aarch64.sh>`_,72.9 MiB,``a632110a9ebddd8528b26241663ee9368d218e36b40e570072774897762f1de8``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.0-3-Linux-ppc64le.sh>`_,74.1 MiB,``5ed0af4645f49c4412e33a3f94396bcb3eb25f4a3ccb0bfe5bc23ef06bad6f3f``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.0-3-Linux-s390x.sh>`_,88.0 MiB,``5701eba074e3c2894949370ab456df48361a2efaad9b11209dbf8258ddf1e331``
   Python 3.9,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.0-3-Linux-x86_64.sh>`_,89.1 MiB,``b7fc320922235ccbaacba7b5a61e34671e75f3a2c7110c63db0c6a9f98ecf8a8``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.0-3-Linux-aarch64.sh>`_,83.9 MiB,``f77868e96eee904cd137ebe463439258d76281830bb9e2bd330d23aea1ddd31a``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.0-3-Linux-ppc64le.sh>`_,84.5 MiB,``4bbda8ba3b8d1d26f04a469bbe29b3ef626a8b10b823f64314719e132f7c3696``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.0-3-Linux-s390x.sh>`_,85.5 MiB,``7ef72ef1411b028788c81308238b604cba46315cb42e70a2d65511c05440ebca``
   Python 3.8,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.5.0-3-Linux-x86_64.sh>`_,89.3 MiB,``f833ae8ad96db31d4f2a09d12f1b188721c769d60d813d7e6341c19e77bc791f``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.5.0-3-Linux-aarch64.sh>`_,72.7 MiB,``853e1c3c24f1c4cc2a1c57b05059740127724a2b346f887e3f0bb92a6cd05fe1``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.5.0-3-Linux-ppc64le.sh>`_,74.1 MiB,``5bef0b71b9c9c6a27e534894e913e47e545793a549a8815bb4a66a8c9d793d45``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.5.0-3-Linux-s390x.sh>`_,85.8 MiB,``e0271bc3af023053258cfe01059d53769bbd32dc5542b5c96280d29dcd8568f6``

Release Notes
=============

:doc:`Release Notes for Miniconda <../miniconda_release_notes>`


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
