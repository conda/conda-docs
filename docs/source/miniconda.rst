=========
Miniconda
=========

Miniconda is a free minimal installer for conda. It is a small bootstrap version of Anaconda that includes only conda, Python, the packages they
both depend on, and a small number of other useful packages (like pip, zlib, and a few others). If you need more packages, use the ``conda install``
command to install from thousands of packages available by default in Anaconda’s public repo, or from other channels, like conda-forge or bioconda.

**Is Miniconda the right conda install for you?** The `Anaconda or Miniconda <https://docs.conda.io/projects/conda/en/stable/user-guide/install/download.html#anaconda-or-miniconda>`_ page lists some reasons why you might want one installation over the other.

.. toctree::
   :maxdepth: 1

   miniconda-system-requirements
   miniconda-other-installer-links
   miniconda-install
   miniconda_release_notes
   miniconda-other-resources

.. _miniconda-latest-installer-links:

Latest Miniconda installer links
================================

This list of installers is for the latest release of Python: 3.11.3. For installers for older versions of Python, see :doc:`Other installer links <miniconda-other-installer-links>`. For an archive of Miniconda versions, see https://repo.anaconda.com/miniconda/.

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

.. _quick-command-line-install:

Quick command line install
==========================

These quick command line instructions will get you set up quickly with the latest Miniconda installer. For graphical installer (`.exe` and `.pkg`) and hash checking instructions, see :doc:`Installing Miniconda <miniconda-install>`.

.. tab-set::

   .. tab-item:: Windows

      These three commands quickly and quietly install the latest 64-bit version of the installer and then clean up after themselves. To install a different version or architecture of Miniconda for Windows, change the name of the ``.exe`` installer in the ``curl`` command.

      .. code-block:: none

         curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
         start /wait "" miniconda.exe /S
         del miniconda.exe

      After installing, open the Anaconda Prompt (miniconda3) program to use Miniconda3. The following commands initialize conda for the cmd.exe and Powershell shells:

      .. code-block:: none

         conda init cmd.exe
         conda init powershell

   .. tab-item:: macOS

      These four commands quickly and quietly install the latest M1 macOS version of the installer and then clean up after themselves. To install a different version or architecture of Miniconda for macOS, change the name of the ``.sh`` installer in the ``curl`` command.

      .. code-block:: bash

         mkdir -p ~/miniconda3
         curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
         bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
         rm -rf ~/miniconda3/miniconda.sh

      After installing, initialize your newly-installed Miniconda. The following commands initialize for bash and zsh shells:

      .. code-block:: bash

         ~/miniconda3/bin/conda init bash
         ~/miniconda3/bin/conda init zsh

   .. tab-item:: Linux

      These four commands quickly and quietly install the latest 64-bit version of the installer and then clean up after themselves. To install a different version or architecture of Miniconda for Linux, change the name of the ``.sh`` installer in the ``wget`` command.

      .. code-block:: bash

         mkdir -p ~/miniconda3
         wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
         bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
         rm -rf ~/miniconda3/miniconda.sh

      After installing, initialize your newly-installed Miniconda. The following commands initialize for bash and zsh shells:

      .. code-block:: bash

         ~/miniconda3/bin/conda init bash
         ~/miniconda3/bin/conda init zsh
