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

   Python 3.8,`Miniconda3 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe>`_,58.1 MiB,``b33797064593ab2229a0135dc69001bea05cb56a20c2f243b1231213642e260a``
   ,`Miniconda3 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86.exe>`_,55.3 MiB,``24f438e57ff2ef1ce1e93050d4e9d13f5050955f759f448d84a4018d3cd12d6b``
   Python 2.7,`Miniconda2 Windows 64-bit <https://repo.anaconda.com/miniconda/Miniconda2-latest-Windows-x86_64.exe>`_,54.1 MiB,``6973025404832944e074bf02bda8c4594980eeed4707bb51baa8fbdba4bf326c``
   ,`Miniconda2 Windows 32-bit <https://repo.anaconda.com/miniconda/Miniconda2-latest-Windows-x86.exe>`_,47.7 MiB,``c8049d26f8b6b954b57bcd4e99ad72d1ffa13f4a6b218e64e641504437b2617b``


MacOSX installers
=================

.. csv-table:: MacOSX
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.8,`Miniconda3 MacOSX 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh>`_,42.3 MiB,``786de9721f43e2c7d2803144c635f5f6e4823483536dc141ccd82dbb927cd508``
   ,`Miniconda3 MacOSX 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg>`_,49.9 MiB,``8fa371ae97218c3c005cd5f04b1f40156d1506a9bd1d5c078f89d563fd416816``
   Python 2.7,`Miniconda2 MacOSX 64-bit bash <https://repo.anaconda.com/miniconda/Miniconda2-latest-MacOSX-x86_64.sh>`_,40.3 MiB,``0e2961e20a2239c140766456388beba6630f0c869020d2bd1870c3d040980b45``
   ,`Miniconda2 MacOSX 64-bit pkg <https://repo.anaconda.com/miniconda/Miniconda2-latest-MacOSX-x86_64.pkg>`_,48.4 MiB,``9ca4313e8162a939c7a5a4f48d657722594f8db9a98472803d63c3a7f66fa1da``

Linux installers
================

.. csv-table:: Linux
   :header: Python version,Name,Size,SHA256 hash
   :widths: 5, 10, 5, 80

   Python 3.8,`Miniconda3 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh>`_,63.6 MiB,``1ea2f885b4dbc3098662845560bc64271eb17085387a70c2ba3f29fff6f8d52f``
   Python 3.7,`Miniconda3 Linux 32-bit <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86.sh>`_,62.7 MiB,``f387eded3fa4ddc3104b7775e62d59065b30205c2758a8b86b4c27144adafcc4``
   Python 2.7,`Miniconda2 Linux 64-bit <https://repo.anaconda.com/miniconda/Miniconda2-latest-Linux-x86_64.sh>`_,48.7 MiB,``b820dde1a0ba868c4c948fe6ace7300a252b33b5befd078a15d4a017476b8979``
   ,`Miniconda2 Linux 32-bit <https://repo.anaconda.com/miniconda/Miniconda2-latest-Linux-x86.sh>`_,39.0 MiB,``2e20ac4379ca5262e7612f84ad26b1a2f2782d0994facdecb28e0baf51749979``

Installing
==========
- :doc:`See hashes for all Miniconda installers <../miniconda_hashes>`.
- `Verify your installation <https://conda.io/projects/conda/en/latest/user-guide/install/download.html#cryptographic-hash-verification>`_.
- `Installation
  instructions <https://conda.io/projects/conda/en/latest/user-guide/install/index.html>`__.

Other resources
===============

 -  `Miniconda with Python 3.8 for Power8 &
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