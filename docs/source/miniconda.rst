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

.. csv-table:: Latest - Conda 23.5.2 Python 3.11.3 released July 13, 2023
   :header: Platform,Name,SHA256 hash
   :widths: 5, 10, 80

   Windows,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe>`_,``00e8370542836862d4c790aa8966f1d7344a8addd4b766004febcb23f40e2914``
   ,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86.exe>`_,``4fb64e6c9c28b88beab16994bfba4829110ea3145baa60bda5344174ab65d462``
   macOS,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh>`_,``1622e7a0fa60a7d3d892c2d8153b54cd6ffe3e6b979d931320ba56bd52581d4b``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg>`_,``2236a243b6cbe6f16ec324ecc9e631102494c031d41791b44612bbb6a7a1a6b4``
   ,`Miniconda3 macOS Apple M1 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh>`_,``c8f436dbde130f171d39dd7b4fca669c223f130ba7789b83959adc1611a35644``
   ,`Miniconda3 macOS Apple M1 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.pkg>`_,``837371f3b6e8ae2b65bdfc8370e6be812b564ff9f40bcd4eb0b22f84bf9b4fe5``
   Linux,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh>`_,``634d76df5e489c44ade4085552b97bebc786d49245ed1a830022b0b406de5817``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh>`_,``3962738cfac270ae4ff30da0e382aecf6b3305a12064b196457747b157749a7a``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-ppc64le.sh>`_,``92237cb2a443dd15005ec004f2f744b14de02cd5513a00983c2f191eb43d1b29``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-s390x.sh>`_,``221a4cd7f0a9275c3263efa07fa37385746de884f4306bb5d1fe5733ca770550``

Windows installers
==================

.. csv-table:: Windows
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.11,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.2-0-Windows-x86_64.exe>`_,73.2 MiB,``00e8370542836862d4c790aa8966f1d7344a8addd4b766004febcb23f40e2914``
   Python 3.10,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.2-0-Windows-x86_64.exe>`_,69.5 MiB,``e15638645b34921098a3f760fd8af07e53a427f59b99a0f049420a7751cbbc05``
   Python 3.9,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.2-0-Windows-x86_64.exe>`_,70.0 MiB,``f5738ced68d9ed82996575202dea9375c51fa6419a8e0f3456398c6557a87dc2``
   ,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Windows-x86.exe>`_,67.8 MiB,``4fb64e6c9c28b88beab16994bfba4829110ea3145baa60bda5344174ab65d462``
   Python 3.8,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.5.2-0-Windows-x86_64.exe>`_,71.0 MiB,``585befbcd3a3b532d34bba8ab63818d6bc7cfde975b5d6a7fc49483b6a84f371``
   ,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Windows-x86.exe>`_,66.8 MiB,``60cc5874b3cce9d80a38fb2b28df96d880e8e95d1b5848b15c20f1181e2807db``

macOS installers
================

.. csv-table:: macOS
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.11,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.2-0-MacOSX-x86_64.sh>`_,69.6 MiB,``1622e7a0fa60a7d3d892c2d8153b54cd6ffe3e6b979d931320ba56bd52581d4b``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.2-0-MacOSX-x86_64.pkg>`_,69.2 MiB,``2236a243b6cbe6f16ec324ecc9e631102494c031d41791b44612bbb6a7a1a6b4``
   ,`Miniconda3 macOS Apple M1 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.2-0-MacOSX-arm64.sh>`_,68.6 MiB,``c8f436dbde130f171d39dd7b4fca669c223f130ba7789b83959adc1611a35644``
   ,`Miniconda3 macOS Apple M1 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.2-0-MacOSX-arm64.pkg>`_,68.1 MiB,``837371f3b6e8ae2b65bdfc8370e6be812b564ff9f40bcd4eb0b22f84bf9b4fe5``
   Python 3.10,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.2-0-MacOSX-x86_64.sh>`_,65.6 MiB,``13c57188a4bcb7462a7580c9ddf8ff2d301e353c835d33042a51a231667cf25d``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.2-0-MacOSX-x86_64.pkg>`_,65.2 MiB,``7654b911e5649b051d9695e015bc2f24309fbade5d6298ba4c2f2d2118bd524a``
   ,`Miniconda3 macOS Apple M1 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.2-0-MacOSX-arm64.sh>`_,64.6 MiB,``71b7ca2ae4068504f9c6dab30fd6e83694086241156af1e319d598befe0f3a26``
   ,`Miniconda3 macOS Apple M1 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.2-0-MacOSX-arm64.pkg>`_,64.2 MiB,``57674d7cd22529e8425c76507ebbc4ebb6eb4c2fa36b9563439ceb88b5401765``
   Python 3.9,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.2-0-MacOSX-x86_64.sh>`_,65.0 MiB,``dcbbdf92dc2954c79002b64ed53d3451e191dbdde0b30c67334f41dc6ca46ac1``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.2-0-MacOSX-x86_64.pkg>`_,64.6 MiB,``dd4068750b09409436f5e4829007b06e1726c34acf1aff7248a73b2562b6599f``
   ,`Miniconda3 macOS Apple M1 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.2-0-MacOSX-arm64.sh>`_,64.1 MiB,``1b10164086354b39a46ff928eef5797ff57e0fa9706ccaf7d4e621b416541479``
   ,`Miniconda3 macOS Apple M1 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.2-0-MacOSX-arm64.pkg>`_,63.7 MiB,``c8fa540f615cf164f5a1200313be78654aaf074ca184bf22c4423e90802edd37``
   Python 3.8,`Miniconda3 macOS Intel x86 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.5.2-0-MacOSX-x86_64.sh>`_,66.5 MiB,``6dc8bfb3b382c31be1755545ae6afc5fbdf8a67726ffdb8a05b917204bd08779``
   ,`Miniconda3 macOS Intel x86 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.5.2-0-MacOSX-x86_64.pkg>`_,66.2 MiB,``ad702119896d6dbf25c945174b9999f5bff562e214654310d7f281aa18140349``
   ,`Miniconda3 macOS Apple M1 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.5.2-0-MacOSX-arm64.sh>`_,65.7 MiB,``782bd1a401b20b41227a086adae98e270bbc942c3b7621788fb5574a9583142e``
   ,`Miniconda3 macOS Apple M1 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.5.2-0-MacOSX-arm64.pkg>`_,65.3 MiB,``dd3eeb5b09f45aa5a1a4f921581582450f4c05ae35f7dd9f837a24f61f9442f5``

Linux installers
================

.. csv-table:: Linux
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.11,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.2-0-Linux-x86_64.sh>`_,98.4 MiB,``634d76df5e489c44ade4085552b97bebc786d49245ed1a830022b0b406de5817``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.2-0-Linux-aarch64.sh>`_,76.4 MiB,``3962738cfac270ae4ff30da0e382aecf6b3305a12064b196457747b157749a7a``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.2-0-Linux-ppc64le.sh>`_,77.3 MiB,``92237cb2a443dd15005ec004f2f744b14de02cd5513a00983c2f191eb43d1b29``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py311_23.5.2-0-Linux-s390x.sh>`_,94.5 MiB,``221a4cd7f0a9275c3263efa07fa37385746de884f4306bb5d1fe5733ca770550``
   Python 3.10,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.2-0-Linux-x86_64.sh>`_,91.4 MiB,``ea5e6e8a3d5a0247b9df85382d27220fac8e59b5778fd313c5913879cd9baafc``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.2-0-Linux-aarch64.sh>`_,72.9 MiB,``24f7fe91032538cf2d9748facabae346e45e46ca21bb5f2d5875b7865dca6fa4``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.2-0-Linux-ppc64le.sh>`_,74.1 MiB,``3a76e4e400271d1589770dac8f696b03d1faf45fee57da38e8c399b6cb0daadb``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py310_23.5.2-0-Linux-s390x.sh>`_,88.0 MiB,``7a65b8593db0ec4b561b9968daca7c7c4f5f95cb21fe717ba895fded924bc056``
   Python 3.9,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.2-0-Linux-x86_64.sh>`_,89.1 MiB,``9829d95f639bd0053b2ed06d1204e60644617bf37dd5cc57523732e0e8d64516``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.2-0-Linux-aarch64.sh>`_,83.9 MiB,``ecc06a39bdf786ebb8325a2754690a808f873154719c97d10087ef0883b69e84``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.2-0-Linux-ppc64le.sh>`_,84.5 MiB,``dc5aee01ee36a154b8070e6948b9a43773b6942476a144bc89e6135ac5beac58``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py39_23.5.2-0-Linux-s390x.sh>`_,85.5 MiB,``40ece8784a9e7dd521ab354ffc816bb466842ae3eee681a93647945c5070c9b4``
   Python 3.8,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.5.2-0-Linux-x86_64.sh>`_,89.3 MiB,``e2a4438671e0e42c5bba14cb51de6ce9763938184d6ca2967340bbe972bbe7e6``
   ,`Miniconda3 Linux-aarch64 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.5.2-0-Linux-aarch64.sh>`_,72.7 MiB,``cd39b811ac9a2f9094c4dfff9ec0f7ec811d6ad7ede5ab3f1a31d330ab3a2c55``
   ,`Miniconda3 Linux-ppc64le 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.5.2-0-Linux-ppc64le.sh>`_,74.1 MiB,``6fc3bf00d4fe0c724fab884d93b981acbc22bb8fc41c144df6d2fc080ff80e25``
   ,`Miniconda3 Linux-s390x 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-py38_23.5.2-0-Linux-s390x.sh>`_,85.8 MiB,``b840fd5a8474a3e6831cd50a64eadf73239c6ad7deeebf2c3d3fe366220b2722``

Release Notes
=============
- :doc:`Release Notes for Miniconda <../miniconda_release_notes>`

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
