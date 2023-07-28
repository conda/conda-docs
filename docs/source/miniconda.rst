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
   miniconda-installer-links
   miniconda-install
   miniconda_release_notes
   miniconda-other-resources

Quick command line install
==========================

These quick command line instructions will get you set up quickly with the latest Miniconda installer. For graphical installer (`.exe` and `.pkg`) and hash checking instructions, see :doc:`Installing Miniconda <miniconda-install>`.

.. tab-set::

   .. tab-item:: macOS

      These four commands quickly and quietly install the latest M1 macOS version of the installer and then clean up after themselves. To install a different version or architecture of Miniconda for macOS, change the name of the ``.sh`` installer in the ``curl`` command.

      .. code-block:: bash

         mkdir -p ~/miniconda3
         curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
         bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
         rm -rf ~miniconda3/miniconda.sh

      After installing, initialize your newly-installed Miniconda. The following commands initialize for bash and zsh shells:

      .. code-block:: bash

         ~/miniconda3/bin/conda init bash
         ~/miniconda3/bin/conda init zsh

   .. tab-item:: Linux

      These four commands quickly and quietly install the latest 64-bit version of the installer and then clean up after themselves. To install a different version or architecture of Miniconda for Linux, change the name of the ``.sh`` installer in the ``wget`` command.

      .. code-block:: bash

         mkdir -p ~/miniconda3
         wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o ~/miniconda3/miniconda.sh
         bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
         rm -rf ~/miniconda3/miniconda.sh

      After installing, initialize your newly-installed Miniconda. The following commands initialize for bash and zsh shells:

      .. code-block:: bash

         ~/miniconda3/bin/conda init bash
         ~/miniconda3/bin/conda init zsh
