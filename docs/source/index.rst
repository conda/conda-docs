.. conda documentation master file, created by
   sphinx-quickstart on Sat Nov  3 16:08:12 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=====
Conda
=====

Conda is an open source package management system and environment management system for installing multiple
versions of software packages and their dependencies and switching easily between them. It works on
Linux, OS X and Windows, and was created for Python programs but can package and distribute any software.

Conda is included in all versions of Anaconda, Anaconda Server, and Miniconda, and is not available separately. 

* Miniconda is a small “bootstrap” version that includes only conda and conda-build, and installs Python. Over 200 
  scientific packages and their dependencies can be installed individually from the Continuum repository with
  the “conda install” command.
* Anaconda includes conda, conda-build, Python, and over 100 automatically installed scientific packages and
  their dependencies. Like Miniconda, over 200 scientific packages can be installed individually with
  the “conda install” command.
* Anaconda Server allows both system administrators and users to manage packages and environments on-site. Any
  software application stack can be managed, including Python, R, NodeJs, Java, and more. It is sold by
  Continuum Analytics.

The `conda` command is the primary interface for managing `Anaconda
<http://docs.continuum.io/anaconda/index.html>`_ installations. It can query
and search the Anaconda package index and current Anaconda installation,
create new conda environments, and install and update packages into existing
conda environments.


.. raw:: html

        <iframe width="560" height="315" src="https://www.youtube.com/embed/UaIvrDWrIWM" frameborder="0" allowfullscreen></iframe>


Table of Contents
-----------------
.. toctree::
   :maxdepth: 2

   get-started
   using/index
   building/build
   help/help
   get-involved

Presentations & Blog Posts
--------------------------

`Packaging and Deployment with conda - Travis Oliphant <https://speakerdeck.com/teoliphant/packaging-and-deployment-with-conda>`_

`Python 3 support in Anaconda - Ilan Schnell <http://continuum.io/blog/anaconda-python-3>`_

`New Advances in conda - Ilan Schnell <http://continuum.io/blog/new-advances-in-conda>`_

`Python Packages and Environments with conda - Bryan Van de Ven <http://continuum.io/blog/conda>`_

`Advanced features of Conda, part 1 - Aaron Meurer <http://continuum.io/blog/advanced-conda-part-1>`_

`Advanced features of Conda, part 2 - Aaron Meurer <http://continuum.io/blog/advanced-conda-part-2>`_

Requirements
------------

* python 2.7, 3.3, 3.4, or 3.5
* pycosat
* pyyaml
* requests


Indices and tables
------------------

* :ref:`genindex`
* :ref:`search`
