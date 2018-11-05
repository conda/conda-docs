.. _miniconda:

===========
 Miniconda
===========

.. table::
   :widths: 1 3 3 3
   :column-alignment: center center center center

   +----------+-------------------+-----------------+-----------------+
   |          ||Windows|          ||Mac|            ||Linux|          |
   |          |                   |                 |                 |
   |          |Windows            |Mac OS X         |Linux            |
   +----------+-------------------+-----------------+-----------------+
   |**Python  |`64-bit (exe       |`64-bit (bash    |`64-bit (bash    |
   |3.7**     |installer)         |installer)       |installer)       |
   |          |<Windows-py3-64_>`_|<Mac-py3-64_>`_  |<Linux-py3-64_>`_|
   |          |                   |                 |                 |
   |          |`32-bit (exe       |`64-bit (.pkg    |`32-bit (bash    |
   |          |installer)         |installer)       |installer)       |
   |          |<Windows-py3-32_>`_|<Mac-py3p-64_>`_ |<Linux-py3-32_>`_|
   |          |                   |                 |                 |
   +----------+-------------------+-----------------+-----------------+
   |**Python  |`64-bit (exe       |`64-bit (bash    |`64-bit (bash    |
   |2.7**     |installer)         |installer)       |installer)       |
   |          |<Windows-py2-64_>`_|<Mac-py2-64_>`_  |<Linux-py2-64_>`_|
   |          |                   |                 |                 |
   |          |`32-bit (exe       |`64-bit (.pkg    |`32-bit (bash    |
   |          |installer)         |installer)       |installer)       |
   |          |<Windows-py2-32_>`_|<Mac-py2p-64_>`_ |<Linux-py2-32_>`_|
   |          |                   |                 |                 |
   +----------+-------------------+-----------------+-----------------+

`Installation instructions <https://conda.io/docs/user-guide/install/index.html>`_

Other resources:

* `Miniconda with Python 3.7 for Power8 <https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-ppc64le.sh>`_
* `Miniconda with Python 2.7 for Power8 <https://repo.anaconda.com/miniconda/Miniconda2-latest-Linux-ppc64le.sh>`_
* `Miniconda Docker images <https://hub.docker.com/r/continuumio/>`_
* `Miniconda AWS images <https://aws.amazon.com/marketplace/seller-profile?id=29f81979-a535-4f44-9e9f-6800807ad996>`_
* `Archive and MD5 sums for the installers <https://repo.anaconda.com/miniconda/>`_
* `conda change log <https://github.com/conda/conda/blob/master/CHANGELOG.md>`_

These Miniconda installers contain the conda package manager and Python. Once
Miniconda is installed, you can use the conda command to install any other
packages and create environments, etc. For example:

.. code-block:: bash


   $ conda install numpy
   ...
   $ conda create -n py3k anaconda python=3
   ...

There are two variants of the installer: Miniconda is Python 2 based and Miniconda3 is Python 3 based. Note that the choice of which Miniconda is installed only affects the root environment. Regardless of which version of Miniconda you install, you can still install both Python 2.x and Python 3.x environments.

The other difference is that the Python 3 version of Miniconda will default to
Python 3 when creating new environments and building packages. So for
instance, the behavior of

.. code-block:: bash

   $ conda create -n myenv python

will be to install Python 2.7 with the Python 2 Miniconda and to install
Python 3.7 with the Python 3 Miniconda. You can override the default by
explicitly setting ``python=2`` or ``python=3``. It also determines the
default value of ``CONDA_PY`` when using ``conda build``.

**Note**: If you already have Miniconda or Anaconda installed, and you just
want to upgrade, you should not use the installer. Just use ``conda
update``. For instance

.. code-block:: bash

   $ conda update conda

will update conda.

.. _images:

.. |Linux| replace:: :fonticon:`icon-linux icon-4x`

.. |Mac| replace:: :fonticon:`icon-apple icon-4x`

.. |Windows| replace:: :fonticon:`icon-windows icon-4x`

.. _Windows-py2-64: https://repo.anaconda.com/miniconda/Miniconda2-latest-Windows-x86_64.exe

.. _Mac-py2-64: https://repo.anaconda.com/miniconda/Miniconda2-latest-MacOSX-x86_64.sh

.. _Mac-py2p-64: https://repo.anaconda.com/miniconda/Miniconda2-latest-MacOSX-x86_64.pkg

.. _Linux-py2-64: https://repo.anaconda.com/miniconda/Miniconda2-latest-Linux-x86_64.sh

.. _Windows-py2-32: https://repo.anaconda.com/miniconda/Miniconda2-latest-Windows-x86.exe

.. _Linux-py2-32: https://repo.anaconda.com/miniconda/Miniconda2-latest-Linux-x86.sh

.. _Windows-py3-64: https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe

.. _Mac-py3-64: https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh

.. _Mac-py3p-64: https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg

.. _Linux-py3-64: https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

.. _Windows-py3-32: https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86.exe

.. _Linux-py3-32: https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86.sh
