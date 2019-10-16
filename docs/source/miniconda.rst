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

   Python 3.7,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe>`_,50.6 MiB,``6263b5c45038a624eb265341eae5180a87c0fe0a97f1ce4ff0b9b9d91807cfd3``
   ,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86.exe>`_,53.2 MiB,``ff851cfe7cb4c21adbed48cb7f74d7e2ec457d76c02269132e6093e0fe8838c4``
   Python 2.7,`Miniconda2 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda2-latest-Windows-x86_64.exe>`_,50.0 MiB,``63b8220df057aa91bbb5ab71b3f8f7ea8489a5f0b46d49a36f7804b30683717b``
   ,`Miniconda2 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda2-latest-Windows-x86.exe>`_,48.0 MiB,``a636f00fe9ff218825c8f256962ef7a108529936d1cb7ce9270192cabc542d3c``


MacOSX installers
=================

.. csv-table:: MacOSX
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.7,`Miniconda3 MacOSX 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh>`_,48.2 MiB,``a879d93f42bdc796a4b975a11d109dfacc11a7ba6c4106aedf657d5e1fd79410``
   ,`Miniconda3 MacOSX 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg>`_,59.8 MiB,``6636f7a41d54136f2623d1ff5be2543b142b5810d7734f57bf47d1931d7c0b03``
   Python 2.7,`Miniconda2 MacOSX 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda2-latest-MacOSX-x86_64.sh>`_,38.1 MiB,``3159ea8f0ef8d394e17b2e363444e22b579e631675d468b8bce49047763ca435``
   ,`Miniconda2 MacOSX 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda2-latest-MacOSX-x86_64.pkg>`_,47.8 MiB,``7d113df5704aecbff25429410e22b2fc55cd729053b5c20edc7f7470d07b38fb``

Linux installers
================

.. csv-table:: Linux
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.7,`Miniconda Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh>`_,67.2 MiB,``a23fcffe97690d3bbcd34cda798c3a3318e0f35d863c5d4aca3fc983fe8450b7``
   ,`Miniconda3 Linux 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86.sh>`_,62.7 MiB,``f387eded3fa4ddc3104b7775e62d59065b30205c2758a8b86b4c27144adafcc4``
   Python 2.7,`Miniconda2 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda2-latest-Linux-x86_64.sh>`_,44.8 MiB,``2248d5f2eeeff69b142a6ccf3148357b8e42f9c4141ab97a17c9e27f6149c417``
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