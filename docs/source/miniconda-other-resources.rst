===============
Other resources
===============

 -  `Miniconda Docker images <https://hub.docker.com/r/continuumio/>`_
 -  `Miniconda AWS images <https://aws.amazon.com/marketplace/seller-profile?id=29f81979-a535-4f44-9e9f-6800807ad996>`_
 -  `Installer and SHA256 hash archive <https://repo.anaconda.com/miniconda/>`_
 -  `conda release notes <https://conda.io/projects/continuumio-conda/en/latest/release-notes.html>`_

Miniconda's installers contain the conda package manager, Python, and a few necessary packages. Once Miniconda is
installed, you can use the conda command to install any other packages and create environments.

For example:

 .. container:: highlight-bash notranslate

    .. container:: highlight

       ::

          $ conda install numpy
          ...
          $ conda create -n py3k anaconda python=3
          ...

There are two variants of the installer: Miniconda is Python 2 based, while Miniconda3 is Python 3 based.
Which Miniconda is installed only affects the root environment. Regardless of which version of Miniconda you
install, you can still use conda to install both Python 2.x and Python 3.x environments.

However, Miniconda3 (the Python 3 version of Miniconda) will default to Python 3 when creating new environments
and building packages.

For example, take the command below:

 .. container:: highlight-bash notranslate

    .. container:: highlight

       ::

          $ conda create -n myenv python

Miniconda (Python 2 based) installs Python 2.7, while Miniconda3 (Python 3 based) installs Python 3.11 by default.
You can override the default by explicitly setting ``python=2`` or ``python=3`` when creating the environment. The
Miniconda version also determines the default value of ``CONDA_PY`` when using ``conda build``.

 .. note::
    If you already have Miniconda or Anaconda installed, and you just want to upgrade, you should
    not use the installer. Just use ``conda update conda``.
