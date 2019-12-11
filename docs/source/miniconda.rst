.. This page is generated from the create_miniconda_rst.py script.
   To make changes edit the miniconda.rst.jinja2 file and execute the script
   to re-generate miniconda.rst

=========
Miniconda
=========

Miniconda is a free minimal installer for conda. It is a small, bootstrap
version of Anaconda that includes only conda, Python, the packages they depend
on, and a small number of other useful packages, including pip, zlib and a
few others. Use the ``conda install command`` to install 720+ additional conda
packages from the Anaconda repository.

`See if Miniconda is right for you <https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html#anaconda-or-miniconda>`_.

Windows installers
==================

.. csv-table:: Windows
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.7,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe>`_,51.5 MiB,``f18060cc0bb50ae75e4d602b7ce35197c8e31e81288d069b758594f1bb46ab45``
   ,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86.exe>`_,54.0 MiB,``7c30778941d2bba03531ba269a78a108b01fa366530290376e7c3b467f3c66ba``
   Python 2.7,`Miniconda2 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda2-latest-Windows-x86_64.exe>`_,50.9 MiB,``8647c54058f11842c37854edeff4d20bc1fbdad8b88d9d34d76fda1630e64846``
   ,`Miniconda2 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda2-latest-Windows-x86.exe>`_,48.7 MiB,``0d106228d6a4610b599df965dd6d9bb659329a17e3d693e3274b20291a7c6f94``


MacOSX installers
=================

.. csv-table:: MacOSX
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.7,`Miniconda3 MacOSX 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh>`_,49.4 MiB,``5cf91dde8f6024061c8b9239a1b4c34380238297adbdb9ef2061eb9d1a7f69bc``
   ,`Miniconda3 MacOSX 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg>`_,59.8 MiB,``9927f1de5151a1a6431b02846fbca089e8b97a55a244f02ffc3207522092907b``
   Python 2.7,`Miniconda2 MacOSX 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda2-latest-MacOSX-x86_64.sh>`_,39.4 MiB,``0db8f4037e40e13eb1d2adc89e054dfb165470cc77be45ef2bf9cb31c8b72f39``
   ,`Miniconda2 MacOSX 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda2-latest-MacOSX-x86_64.pkg>`_,47.8 MiB,``fcc30b2e18f7a292b34b2e24ad855786a66423f860157fa2b77e48b6392f0abb``

Linux installers
================

.. csv-table:: Linux
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.7,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh>`_,68.5 MiB,``bfe34e1fa28d6d75a7ad05fd02fa5472275673d5f5621b77380898dee1be15d2``
   ,`Miniconda3 Linux 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86.sh>`_,62.7 MiB,``f387eded3fa4ddc3104b7775e62d59065b30205c2758a8b86b4c27144adafcc4``
   Python 2.7,`Miniconda2 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda2-latest-Linux-x86_64.sh>`_,46.0 MiB,``383fe7b6c2574e425eee3c65533a5101e68a2d525e66356844a80aa02a556695``
   ,`Miniconda2 Linux 32-bit <https://repo.anaconda.com/miniconda/Miniconda2-latest-Linux-x86.sh>`_,39.0 MiB,``2e20ac4379ca5262e7612f84ad26b1a2f2782d0994facdecb28e0baf51749979``

Installing
==========
- :doc:`See hashes for all Miniconda installers <../miniconda_hashes>`.
- `Verify your installation <https://conda.io/projects/conda/en/latest/user-guide/install/download.html#cryptographic-hash-verification>`_.
- `Installation
  instructions <https://conda.io/projects/conda/en/latest/user-guide/install/index.html>`__.

Other resources
===============

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
 instance, the behavior of:

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
