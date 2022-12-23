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

.. csv-table:: Latest - Conda 22.11.1 Python 3.10.8 released December 22, 2022
   :header: Platform,Name,SHA256 hash
   :widths: 5, 10, 80

   Windows,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe>`_,``2e3086630fa3fae7636432a954be530c88d0705fce497120d56e0f5d865b0d51``
   ,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86.exe>`_,``4fb64e6c9c28b88beab16994bfba4829110ea3145baa60bda5344174ab65d462``
   macOS,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh>`_,``7406579393427eaf9bc0e094dcd3c66d1e1b93ee9db4e7686d0a72ea5d7c0ce5``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg>`_,``9195ffba1a6984c81c69649ce976a38455ace5b474c24a4363e5ca65fc72e832``
   ,`Miniconda3 macOS Apple M1 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh>`_,``22eec9b7d3add25ac3f9b60621d8f3d8df3e63d4aa0ae5eb846b558d7ba68333``
   ,`Miniconda3 macOS Apple M1 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.pkg>`_,``fbb33c5770b10a0d5a0deef746e7499bfaf8ff840d0d517175036dd8449357f6``
   Linux,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh>`_,``00938c3534750a0e4069499baf8f4e6dc1c2e471c86a59caa0dd03f4a9269db6``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh>`_,``48a96df9ff56f7421b6dd7f9f71d548023847ba918c3826059918c08326c2017``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-ppc64le.sh>`_,``4c86c3383bb27b44f7059336c3a46c34922df42824577b93eadecefbf7423836``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-s390x.sh>`_,``a150511e7fd19d07b770f278fb5dd2df4bc24a8f55f06d6274774f209a36c766``

Windows installers
==================

.. csv-table:: Windows
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.10,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_22.11.1-1-Windows-x86_64.exe>`_,52.9 MiB,``2e3086630fa3fae7636432a954be530c88d0705fce497120d56e0f5d865b0d51``
   Python 3.9,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_22.11.1-1-Windows-x86_64.exe>`_,53.0 MiB,``4b92942fbd70e84a221306a801b3e4c06dd46e894f949a3eb19b4b150ec19171``
   Python 3.8,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_22.11.1-1-Windows-x86_64.exe>`_,52.5 MiB,``9f6ce5307db5da4e391ced4a6a73159234c3fc64ab4c1d6621dd0b64b0c24b5f``
   Python 3.7,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_22.11.1-1-Windows-x86_64.exe>`_,50.7 MiB,``4d48f78d7edbf4db0660f3b3e28b6fa17fa469cdc98c76b94e08662b92a308bd``
   Python 3.9,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_22.11.1-1-Windows-x86.exe>`_,,````
   Python 3.8,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_22.11.1-1-Windows-x86.exe>`_,,````
   Python 3.7,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_22.11.1-1-Windows-x86.exe>`_,,````


macOS installers
=================

.. csv-table:: macOS
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.10,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py310_22.11.1-1-MacOSX-x86_64.sh>`_,44.4 MiB,``7406579393427eaf9bc0e094dcd3c66d1e1b93ee9db4e7686d0a72ea5d7c0ce5``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py310_22.11.1-1-MacOSX-x86_64.pkg>`_,44.2 MiB,``9195ffba1a6984c81c69649ce976a38455ace5b474c24a4363e5ca65fc72e832``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py310_22.11.1-1-MacOSX-arm64.sh>`_,43.3 MiB,``22eec9b7d3add25ac3f9b60621d8f3d8df3e63d4aa0ae5eb846b558d7ba68333``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py310_22.11.1-1-MacOSX-arm64.pkg>`_,43.0 MiB,``fbb33c5770b10a0d5a0deef746e7499bfaf8ff840d0d517175036dd8449357f6``
   Python 3.9,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py39_22.11.1-1-MacOSX-x86_64.sh>`_,44.7 MiB,``9a537f3a1b472098754c59a30b94822f1e9458405af831172aaa8f8124e9df88``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py39_22.11.1-1-MacOSX-x86_64.pkg>`_,44.5 MiB,``c3169286b271e0621d00d821f76dd7bd2563c32389896566dee115e53f6002c1``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py39_22.11.1-1-MacOSX-arm64.sh>`_,43.6 MiB,``eca5e241faea19d4b352aba819f99f42e2336fdbeecb04f5bc89c9ca786ea798``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py39_22.11.1-1-MacOSX-arm64.pkg>`_,43.3 MiB,``4b5cd684601e638da6987b465b95b0ebbde4dcfcac840fe58095eb3940f4a62c``
   Python 3.8,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py38_22.11.1-1-MacOSX-x86_64.sh>`_,44.6 MiB,``6c4cea3c355326f503d15ae97e5126437529a595499e3ce304cd0f247e935da8``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py38_22.11.1-1-MacOSX-x86_64.pkg>`_,44.4 MiB,``62e30204221f9e65e89b3644a60d289c6582eed097f83d5dcd9752bafd743491``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py38_22.11.1-1-MacOSX-arm64.sh>`_,43.2 MiB,``bf75dbf193db6895c62b2bb963cab2534a8bbdf0ac956f270da8d7a19f4d1b54``
   ,`Miniconda3 macOS Apple M1 ARM 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py38_22.11.1-1-MacOSX-arm64.pkg>`_,42.9 MiB,``34ea0d81e51df29a47625f4900f95390bfb079f063e02ddf1ae57a2133fcef56``
   Python 3.7,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py37_22.11.1-1-MacOSX-x86_64.sh>`_,54.8 MiB,``e51d459aae45bb6b86c2716738b778b788785e6e1ea4b2ed244a0fdd754feb19``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py37_22.11.1-1-MacOSX-x86_64.pkg>`_,54.5 MiB,``b694a332b5ae4e3096c9471969cf00188257364a4bfe59d7f312b19af66bcd48``

Linux installers
================

.. csv-table:: Linux
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.10,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_22.11.1-1-Linux-x86_64.sh>`_,69.0 MiB,``00938c3534750a0e4069499baf8f4e6dc1c2e471c86a59caa0dd03f4a9269db6``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_22.11.1-1-Linux-aarch64.sh>`_,49.6 MiB,``48a96df9ff56f7421b6dd7f9f71d548023847ba918c3826059918c08326c2017``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_22.11.1-1-Linux-ppc64le.sh>`_,50.0 MiB,``4c86c3383bb27b44f7059336c3a46c34922df42824577b93eadecefbf7423836``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_22.11.1-1-Linux-s390x.sh>`_,61.2 MiB,``a150511e7fd19d07b770f278fb5dd2df4bc24a8f55f06d6274774f209a36c766``
   Python 3.9,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_22.11.1-1-Linux-x86_64.sh>`_,66.7 MiB,``e685005710679914a909bfb9c52183b3ccc56ad7bb84acc861d596fcbe5d28bb``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_22.11.1-1-Linux-aarch64.sh>`_,60.3 MiB,``031b6c52060bb75e930846c0a66baa91db8196f0d97fd32f3822c54db6b7c76a``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_22.11.1-1-Linux-ppc64le.sh>`_,60.4 MiB,``16cc2d74644cf838d2761723c01172e0b704674317630480902ef429af29bd0b``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_22.11.1-1-Linux-s390x.sh>`_,58.8 MiB,``ed6176aa6b52e22d939ea5c0c38f9f3cf52d2519a5d0dcb414936287893a31f9``
   Python 3.8,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_22.11.1-1-Linux-x86_64.sh>`_,61.6 MiB,``473e5ecc8e078e9ef89355fbca21f8eefa5f9081544befca99867c7beac3150d``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_22.11.1-1-Linux-aarch64.sh>`_,48.1 MiB,``ff65684bce7a7ad7abb698ff649195816ee0f47a4f17cb9632a44abf69357ea5``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_22.11.1-1-Linux-ppc64le.sh>`_,48.5 MiB,``59fd0901f9fa1ba6b07e734adff4d6c5215e9d7f13ad37f0044af22e9b72194a``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_22.11.1-1-Linux-s390x.sh>`_,57.9 MiB,``5bdc6ead307c098b32ba8473b7cbbe87eb80f8eca9adba03f47848bcb34a9b38``
   Python 3.7,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_22.11.1-1-Linux-x86_64.sh>`_,82.3 MiB,``22b14d52265b4e609c6ce78e2f2884b277d976b83b5f9c8a83423e3eba2ccfbe``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_22.11.1-1-Linux-aarch64.sh>`_,80.5 MiB,``ebba2f7e33ce5594c50e6422477106e6bb327310838fbac3db89d2eaebcde943``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_22.11.1-1-Linux-ppc64le.sh>`_,81.1 MiB,``dda16ae14992697e3c90b56fe9de819f5f3b1dcb3ac7a31d24ab5736ccd5f129``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py37_22.11.1-1-Linux-s390x.sh>`_,78.7 MiB,``3c71628865164c3f8b461f8e4b2a353ff1367eed61c83b9c3e14fc201608b1a7``

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
