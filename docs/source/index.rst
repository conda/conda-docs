===================
Conda Documentation
===================

Conda provides package, dependency, and environment management for any language.
The following documentation site provides all you need to get started with
leveraging the power of conda.

.. grid:: 1 2 2 2

    .. grid-item::

        .. card:: Getting started :octicon:`rocket;1em;sd-text-primary`
            :link: https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html

            Learn how to get started using conda with tutorials and quick start guides

    .. grid-item::

        .. card:: Package search :octicon:`search;1em;sd-text-primary`
            :link: https://anaconda.org

            Find all the packages for your project on `anaconda.org <https://anaconda.org>`_

    .. grid-item::

        .. card:: Commands :octicon:`terminal;1em;sd-text-primary`
            :link: https://docs.conda.io/projects/conda/en/stable/commands/index.html

            Documentation for all essential conda commands

    .. grid-item::

        .. card:: Building Packages :octicon:`package;1em;sd-text-primary`
            :link: https://docs.conda.io/projects/conda-build/en/stable/index.html

            Learn how to build and distribute your software with conda

    .. grid-item::

        .. card:: What's new? :octicon:`globe;1em;sd-text-primary`
            :link: https://conda.org/blog

            Check out our blog for the latest release notes and other news

    .. grid-item::

        .. card:: Developer guide :octicon:`file-code;1em;sd-text-primary`
            :link: https://docs.conda.io/projects/conda/en/stable/dev-guide/index.html

            Take deep dives into advanced topics on the internal workings of conda

Install  :octicon:`download;1em;sd-text-primary`
================================================

We recommend the following conda distributions to install conda:

.. grid:: 2

    .. grid-item-card:: Miniconda

        `Miniconda <https://docs.anaconda.com/miniconda>`__ is an installer
        by `Anaconda <https://anaconda.com/>`__ that comes
        preconfigured for use with the Anaconda Repository. See the
        notes about Anaconda's :ref:`Terms of Service <anaconda-tos_notes>`.

        .. button-link:: https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe
            :color: primary

            :fab:`windows` Windows :bdg-light-line:`x86_64` :octicon:`download`

        .. button-link:: https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.pkg
            :color: primary

            :fab:`apple` macOS :bdg-light-line:`arm64 (Apple Silicon)` :octicon:`download`

        .. button-link:: https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg
            :color: primary

            :fab:`apple` macOS :bdg-light-line:`x86_64 (Intel)` :octicon:`download`

        .. button-link:: https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
            :color: primary

            :fab:`linux` Linux :bdg-light-line:`x86_64 (amd64)` :octicon:`download`

        .. button-link:: https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh
            :color: primary

            :fab:`linux` Linux :bdg-light-line:`aarch64 (arm64)` :octicon:`download`

        ++++

        Or with :fa:`beer-mug-empty` `Homebrew <https://brew.sh/>`__:

        .. code-block:: bash

            brew install miniconda

    .. grid-item-card:: Miniforge

        Miniforge is an installer maintained by the `conda-forge community <https://
        conda-forge.org>`__ that comes preconfigured for use with the conda-forge
        channel.

        .. button-link:: https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe
            :color: primary

            :fab:`windows` Windows :bdg-light-line:`x86_64` :octicon:`download`

        .. button-link:: https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh
            :color: primary

            :fab:`apple` macOS :bdg-light-line:`arm64 (Apple Silicon)` :octicon:`download`

        .. button-link:: https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-x86_64.sh
            :color: primary

            :fab:`apple` macOS :bdg-light-line:`x86_64 (Intel)` :octicon:`download`

        .. button-link:: https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
            :color: primary

            :fab:`linux` Linux :bdg-light-line:`x86_64 (amd64)` :octicon:`download`

        .. button-link:: https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh
            :color: primary

            :fab:`linux` Linux :bdg-light-line:`aarch64 (arm64)` :octicon:`download`

        +++

        Or with :fa:`beer-mug-empty` `Homebrew <https://brew.sh/>`__:

        .. code-block:: bash

            brew install miniforge


.. raw:: html

    <p class="text-small">For more detailed instructions, see <a href="https://docs.anaconda.com/miniconda/" target="_blank">Miniconda's installation guide</a> and
    <a href="https://conda-forge.org/download/" target="_blank">conda-forge's download site</a>.</p>

Projects :octicon:`package;1em;sd-text-primary`
===============================================

.. grid:: 1 2 2 2

    .. grid-item::

        .. card:: conda :octicon:`terminal;1em;sd-text-primary`
            :link: https://docs.conda.io/projects/conda/en/stable/

            Conda provides all essential commands for creating and using environments

    .. grid-item::

        .. card:: conda build :octicon:`package;1em;sd-text-primary`
            :link: https://docs.conda.io/projects/conda-build/en/stable/

            Conda build provides many tools that can be used to build conda packages

    .. grid-item::

        .. card:: Miniconda :octicon:`database;1em;sd-text-primary`
            :link: https://docs.anaconda.com/free/miniconda/

            Miniconda is a conda installer provided by Anaconda

    .. grid-item::

        .. card:: conda lock :octicon:`lock;1em;sd-text-primary`
            :link: https://conda.github.io/conda-lock/

            Conda lock generates fully reproducible lock files for conda environments

    .. grid-item::

        .. card:: constructor :octicon:`package-dependents;1em;sd-text-primary`
            :link: https://conda.github.io/constructor/

            Constructor builds OS-specific installers for conda packages

    .. grid-item::

        .. card:: conda pack :octicon:`file-submodule;1em;sd-text-primary`
            :link: https://conda.github.io/conda-pack/

            Conda pack creates distributable archives of conda environments

.. toctree::
   :hidden:
   :maxdepth: 1

   help-support
   contributing
   license

.. |reg|    unicode:: U+000AE .. REGISTERED SIGN
