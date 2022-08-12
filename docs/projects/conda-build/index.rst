.. _index:

conda-build
===========

Conda-build contains commands and tools to use conda to build your
own packages.
It also provides helpful tools to constrain or pin
versions in recipes. Building a conda package requires
:doc:`installing conda-build <install-conda-build>` and
creating a conda :doc:`recipe <concepts/recipe>`.
You then use the ``conda build`` command to build the conda package
from the conda recipe.

You can build conda packages from a variety of source code
projects, most notably Python. For help packing a Python project,
see the `Setuptools
documentation <https://setuptools.readthedocs.io/en/latest/>`_.

 .. note::
    If you are planning to upload your packages to
    anaconda.org, you will need an `anaconda.org <http://anaconda.org>`_
    account and `anaconda-client <https://github.com/Anaconda-Platform/anaconda-client>`.

.. toctree::
   :hidden:

   install-conda-build
   concepts/index
   user-guide/index
   resources/index
   changelog
