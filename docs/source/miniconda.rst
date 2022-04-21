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
* The ``linux-aarch64`` Miniconda installer requires ``glibc >=2.26`` and thus will **not** work with CentOS 7, Ubuntu 16.04, or Debian 9 ("stretch").
* Minimum 400 MB disk space to download and install.

On Windows, macOS, and Linux, it is best to install Miniconda for the local user,
which does not require administrator permissions and is the most robust type of
installation. However, if you need to, you can install Miniconda system wide,
which does require administrator permissions.

Latest Miniconda Installer Links
================================

.. csv-table:: Latest - Conda 4.11.0 Python 3.9.7 released February 15, 2022
   :header: Platform,Name,SHA256 hash
   :widths: 5, 10, 80

   Windows,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe>`_,``6013152b169c2c2d4bcd75bb03a1b8bf208b8545d69116a59351af695d9a0081``
   ,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86.exe>`_,``12a3a7e8aab7a974705ea4ee5bfc44f7c733241dd1b022f8012cbd42309b8472``
   MacOSX,`Miniconda3 MacOSX 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh>`_,``7717253055e7c09339cd3d0815a0b1986b9138dcfcb8ec33b9733df32dd40eaa``
   ,`Miniconda3 MacOSX 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg>`_,``d3e63d7e8aa3ffb7b095e0b984db47309bb1cb1ec2138f5e6a96a34173671451``
   ,`Miniconda3 macOS Apple M1 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh>`_,``7d3d6e695e62651a2473425b84762b1c1b819a97a2c4419b2b60ae94cab8381b``
   Linux,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh>`_,``4ee9c3aa53329cd7a63b49877c0babb49b19b7e5af29807b793a76bdb1d362b4``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh>`_,``00c7127a8a8d3f4b9c2ab3391c661239d5b9a88eafe895fd0f3f2a8d9c0f4556``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-ppc64le.sh>`_,``8ee1f8d17ef7c8cb08a85f7d858b1cb55866c06fcf7545b98c3b82e4d0277e66``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-s390x.sh>`_,``e5e5e89cdcef9332fe632cd25d318cf71f681eef029a24495c713b18e66a8018``

Windows installers
==================

.. csv-table:: Windows
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.9,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Windows-x86_64.exe>`_,70.4 MiB,``6013152b169c2c2d4bcd75bb03a1b8bf208b8545d69116a59351af695d9a0081``
   Python 3.8,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.11.0-Windows-x86_64.exe>`_,69.8 MiB,``29d8d1720034df262b079514e5f200140f7303b37bfe90ae8a2b40b8f294d2d8``
   Python 3.7,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.11.0-Windows-x86_64.exe>`_,68.1 MiB,``0b4890b2b1782c91ae2de2f77a2f6c5cecb9b54729565771f5301c1fc60fa024``
   Python 3.9,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Windows-x86.exe>`_,66.5 MiB,``12a3a7e8aab7a974705ea4ee5bfc44f7c733241dd1b022f8012cbd42309b8472``
   Python 3.8,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.11.0-Windows-x86.exe>`_,65.6 MiB,``df115c77915519a9a4de9c04ca26f81703be6ac0344762023557fc7659659ac0``
   Python 3.7,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.11.0-Windows-x86.exe>`_,64.2 MiB,``64a18114bc66aaa73f431ef8ca1edc7b16ad5564a16e18f13e1a69272d85ca5d``


macOS installers
=================

.. csv-table:: macOS
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.9,`Miniconda3 macOS 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-MacOSX-x86_64.sh>`_,55.2 MiB,``7717253055e7c09339cd3d0815a0b1986b9138dcfcb8ec33b9733df32dd40eaa``
   ,`Miniconda3 macOS 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-MacOSX-x86_64.pkg>`_,61.9 MiB,``d3e63d7e8aa3ffb7b095e0b984db47309bb1cb1ec2138f5e6a96a34173671451``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-MacOSX-arm64.sh>`_,55.2 MiB,``7d3d6e695e62651a2473425b84762b1c1b819a97a2c4419b2b60ae94cab8381b``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-MacOSX-arm64.pkg>`_,63.2 MiB,``66e5eab94e950ed3afbdf6ee2b0b44e9bf1efdc894d1fd5b8294a4cdade9f118``
   Python 3.8,`Miniconda3 macOS 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.11.0-MacOSX-x86_64.sh>`_,55.7 MiB,``e13a4590879638197b0c506768438406b07de614911610e314f8c78133915b1c``
   ,`Miniconda3 macOS 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.11.0-MacOSX-x86_64.pkg>`_,62.4 MiB,``3ca9720a2b47fbbff529057fd4ec8781a23cb825eec289b487dfa040b7ae8e25``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.11.0-MacOSX-arm64.sh>`_,55.6 MiB,``21faf85f8e4278e528025f1f15e3dff1503693953814c64754a7f93df680be5c``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.11.0-MacOSX-arm64.pkg>`_,63.5 MiB,``724f94292293c3cbfa7c8c97a8ce40e18023f34e0eccb093d6d90113e331c8ad``
   Python 3.7,`Miniconda3 macOS 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.11.0-MacOSX-x86_64.sh>`_,63.5 MiB,``c3a863eb85ad7035e5578684509b0b8387e8eb93c022495ab987baac3df6ef41``
   ,`Miniconda3 macOS 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.11.0-MacOSX-x86_64.pkg>`_,70.2 MiB,``e28d2edb8d79b884f9f35479d35635b2d3d415f3af634b39043aff4ed14a0458``

Linux installers
================

.. csv-table:: Linux
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.9,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Linux-x86_64.sh>`_,72.2 MiB,``4ee9c3aa53329cd7a63b49877c0babb49b19b7e5af29807b793a76bdb1d362b4``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Linux-aarch64.sh>`_,74.4 MiB,``00c7127a8a8d3f4b9c2ab3391c661239d5b9a88eafe895fd0f3f2a8d9c0f4556``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Linux-ppc64le.sh>`_,73.5 MiB,``8ee1f8d17ef7c8cb08a85f7d858b1cb55866c06fcf7545b98c3b82e4d0277e66``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Linux-s390x.sh>`_,68.2 MiB,``e5e5e89cdcef9332fe632cd25d318cf71f681eef029a24495c713b18e66a8018``
   Python 3.8,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.11.0-Linux-x86_64.sh>`_,71.7 MiB,``4bb91089ecc5cc2538dece680bfe2e8192de1901e5e420f63d4e78eb26b0ac1a``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.11.0-Linux-aarch64.sh>`_,63.6 MiB,``607549f9f9c5c703be850fa3025e845656d275d8226b679faf3b1c1813c692ce``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.11.0-Linux-ppc64le.sh>`_,65.2 MiB,``2f606bd65ffe76a7866bc445d96105d0a15b7447e59e4317d2e017f7786272d0``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.11.0-Linux-s390x.sh>`_,67.8 MiB,``f70343824949d45e19d96664cd6fa9893583ea61cce0eb3adf5606f4d453bd18``
   Python 3.7,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.11.0-Linux-x86_64.sh>`_,98.9 MiB,``745c99af2cb0d0e0f43c7ed1a3417ff4d5118eafb501518120ea30361f1bb8f6``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.11.0-Linux-aarch64.sh>`_,100.9 MiB,``736bd228d336f4b2d16cdc94f2e08a5c80c18dc42b0edfc59fe3f66ffb93a87d``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.11.0-Linux-ppc64le.sh>`_,101.0 MiB,``041ba0d993398200b3e7f88aee862a23a7cb4ca8ddafbc9d74f8aabb0a5747db``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_4.11.0-Linux-s390x.sh>`_,95.2 MiB,``b05a2be21e83cedc1350d5895ed8639f21f6a7fc7d36b3cb4f18e1df3f49b03e``

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
