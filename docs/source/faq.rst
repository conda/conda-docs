===
FAQ
===

.. contents::

General questions
=================

1. What is Anaconda?

*Anaconda* is a meta package for *conda*. This meta package contains a stable collection of standard
packages (like *scipy*, *numpy*, *zlib* etc.) for big data and scientific use that have all been tested
to work well together. These packages are all installed automatically with one quick installation 
routine, so it is convenient and fast. It includes Python, so it is often referred to as a “Python
distribution” that makes installing Python (and the many other packages) easy and fast, even for new 
Python users. 

2. What is conda?

Conda is a cross-platform, Python-agnostic “package manager” and “environment manager” program that 
quickly installs, runs, and updates packages and their dependencies, and easily switches between 
environments on your local computer.  Conda is included in all versions of Anaconda, Anaconda Server, 
and Miniconda.

3. What is Miniconda? 

Miniconda mini-installer is a small or “bootstrap” version of Anaconda. It installs only what you need
to get conda running. If you use Miniconda instead of the full Anaconda, you must then choose each 
package you want, and use conda to download and install them.  Miniconda can be used when disk space 
is a problem or if you do not wish to take the time to download and install all of the over 100 packages at once. 


Getting help
============

1. How can I see what conda commands are supported?

.. code-block:: bash

  conda -h

Or on the web in our command reference guide,  :doc:`/commands`.

2. How can I get help for a specific command, such as **conda create**?

.. code-block:: bash

  conda create -h

3. How can I get help with using conda? 

Download our :doc:`/using/cheatsheet` and :doc:`/install/quick` guide, take the 30-minute :doc:`test-drive`, and see the complete :doc:`/using/index` section of our documentation site. 

Get free community support with our `Google group <https://groups.google.com/a/continuum.io/forum/?fromgroups#!forum/anaconda/>`_. 

There are also paid support, training and consulting options. See our `Support Services <http://continuum.io/support/>`_ page for more information.

Searching & info
================

1. How can I find out what version of conda I have installed?

By entering the following in your terminal window:

.. code-block:: bash

  conda info

or by entering:

.. code-block:: bash

  conda -V

SEE ALSO: the complete :doc:`/using/index` section of our documentation site. 

2. How can I check if a specific package, such as *SciPy*, is available for installation?

.. code-block:: bash

  conda search scipy

3. How can I check if a specific package, such as *SciPy*,  is available for installation from the Continuum repos (i.e., from Anaconda)?

.. code-block:: bash

  conda search --override-channels --channel defaults scipy

SEE ALSO: the :doc:`/using/pkgs` section of our documentation site. 

4. How do I check if a specific package such as *iminuit* exists in a specific channel (for example,  http://conda.anaconda.org/mutirri) and is available for installation?

.. code-block:: bash

  conda search --override-channels --channel http://conda.anaconda.org/mutirri iminuit

.. _customization:


Managing Packages 
==================

Installing packages
-------------------

1. How can I install a specific package, such as SciPy?

   .. code-block:: bash

      conda install scipy

2. How can I install a package such as SciPy, in a specific version?

   .. code-block:: bash

      conda install scipy=0.15.0

3. How can I install more than one package at once, such as SciPy and *cURL*)?

   .. code-block:: bash

      conda install scipy curl

NOTE: We recommend that you install all packages at once, so all the dependencies are installed at the same time.

4. How can I install many packages at once and specify the version of the package?

   .. code-block:: bash

      conda install scipy=0.15.0 curl=7.26.0

NOTE: We recommend that you install all packages at once, so all the dependencies are installed at the same time.

Updating packages
-----------------

#. How can I update *conda* itself?

   .. code-block:: bash

      conda update conda

#. How do I update the *Anaconda* meta package?

   .. code-block:: bash

      conda update conda
      conda update anaconda

#. How can I update a specific package, such as SciPy?

   .. code-block:: bash

      conda update scipy

#. How can I prevent a specific package from being updated?

   You can *pin* a package specification in an environment, which will prevent
   it from being updated, unless the ``--no-pin`` flag is passed to conda. To
   do so, add a file named ``pinned`` to the environment's ``conda-meta``
   directory with a list of specs. For example, a file with this command:

   ::

      numpy 1.7.*
      scipy ==0.14.2

   will force numpy to stay on the 1.7 series (any version that starts with
   "1.7."), and will force scipy to stay at exactly version 0.14.2.

   NOTE: With this pinned file, ``conda update numpy`` will keep numpy at 1.7.1, and
   ``conda install scipy=0.15.0`` will lead to an error. To force either of
   these, use the ``--no-pin`` flag, like ``conda update numpy --no-pin``. The
   way pinning works is that the pinned specs are included with each conda
   install, so subsequent ``conda update`` commands without ``--no-pin`` will revert numpy back
   to the 1.7 series.

Removing packages
------------------

#. How can I remove a specific package, such as SciPy?

   .. code-block:: bash

      conda remove scipy

#. How can I remove multiple packages at once, for example, SciPy and *cURL*?

   .. code-block:: bash

      conda remove scipy curl

Managing Environments
=====================

Getting info about environments
-------------------------------

1. How can I get a list of all of my environments?

   .. code-block:: bash

      conda info -e

SEE ALSO: the :doc:`/using/envs` section of our documentation site. 

2. How can I show the name of the active environment in my command prompt?

   The anaconda (or miniconda) installer asks whether it should always add the name 
   of the active environment to the command prompt by inserting it into the environment 
   variable called PATH in the Bash shell. The default is no.

   To turn it on later:
   
     .. code-block:: bash
        
        source deactivate
        conda config --set changeps1 true

   To see how it works:
   
     .. code-block:: bash
        
        source activate environmentname
        source deactivate
   
   NOTE: Replace environmentname with an actual environment name.

   To turn it back off:
   
     .. code-block:: bash
     
        source deactivate
        conda config --set changeps1 false

3. How can I list all installed packages in a specific environment, for example, ``myenv``?

   If ``myenv`` is not activated:

     .. code-block:: bash

        conda list -n myenv

   If ``myenv`` is activated:

     .. code-block:: bash

        conda list

4. How can I check if a package (for example, SciPy) is already installed in an existing environment such as ``myenv``?

     .. code-block:: bash

        conda list -n myenv scipy

Creating new environments
-------------------------

1. How can I create a new and clean environment, for example,``myenv``?

   .. code-block:: bash

      conda create -n myenv python

SEE ALSO: the :doc:`/using/envs` section of our documentation site. 

2. How can I create a new environment such as ``myenv`` with a specific version of *python* 
   as the default interpreter inside it?

   .. code-block:: bash

      conda create -n myenv python=3.4

3. How can I create a new environment, for example, ``myenv`` with a specific package in it, for example, SciPy?

   - In one line:

     .. code-block:: bash

        conda create -n myenv scipy

   - In multiple lines:

     .. code-block:: bash

        conda create -n myenv python
        conda install -n myenv scipy

4. How can I create a new environment with a specific package in a specific version?

   - In one line:

     .. code-block:: bash

        conda create -n myenv scipy=0.15.0

   - In multiple lines:

     .. code-block:: bash

        conda create -n myenv python
        conda install -n myenv scipy=0.15.0

5. How can I use pip in my environment ``myenv``?

   .. code-block:: bash

      conda install -n myenv pip
      source activate myenv
      pip <pip_subcommand>

Activate and deactivate
-----------------------

1. How can I activate the existing environment ``myenv``?

**Linux, OS X:** ``source activate myenv``

**Windows:** activate myenv``

SEE ALSO: the :doc:`/using/envs` section of our documentation site. 

2. How can I deactivate the active environment ``myenv``?

**Linux, OS X:** ``source deactivate myenv``

**Windows:** deactivate myenv``

NOTE: It is good practice to deactivate one environment before activating another.

Installing packages
-------------------

1. How can I install a specific package for example, SciPy, in an existing environment ``myenv``?

     .. code-block:: bash

        conda install -n myenv scipy

2. How can I install a specific version of a package like SciPy in the existing environment ``myenv``?

   If ``myenv`` not activated:

     .. code-block:: bash

        conda install -n myenv scipy=0.15.0

The -n or name tells conda to install the environment into the environment named myenv.

   If ``myenv`` is activated:

     .. code-block:: bash

        conda install scipy=0.15.0

3. How can I automatically install pip or another program every time I create a new environment?

   .. code-block:: bash

      conda config --add create_default_packages pip

   After performing the above command you can create new environments in the
   standard way, and the default package(s) will be installed in all of them.

4. How can I automatically install a specific package like SciPy during creation of any of new environment?

   .. code-block:: bash

      conda config --add create_default_packages scipy

After performing the above command you can create new environments in the
standard way, and the latest version of SciPy will be installed in all of them.

5. How can I automatically install a specific version of a package such as SciPy during creation of any of new environment?

   .. code-block:: bash

      conda config --add create_default_packages scipy=0.15.0

After performing the above command you can create new environments in the standard way, and SciPy Version 0.15.0 will be installed in all of them.

6. How can I ignore packages from automatic installation during creation of new and clean environment, such as ``myenv``?

   .. code-block:: bash

      conda create --no-default-packages -n myenv python

Removing packages and environments
----------------------------------

#. How can I remove the package SciPy in an existing environment such as ``myenv``?

   If ``myenv`` is not activated:

     .. code-block:: bash

        conda remove -n myenv scipy

   If ``myenv`` is activated:

     .. code-block:: bash

        conda remove scipy

#. How can I remove an existing environment such as ``myenv``?

     .. code-block:: bash

        conda remove -n myenv --all


Customization (.condarc file)
=============================

NOTE: It may be necessary to add the "force" option ``-f`` to the following commands.

#. How can I get all keys and their values from my .condarc file?

   .. code-block:: bash

      conda config --get

#. How can I get the value of a specific key (for example, channels) from my .condarc file?

   .. code-block:: bash

      conda config --get channels

#. How can I add a new value (for example, http://conda.anaconda.org/mutirri) to a specific key (for example, channels)?

   .. code-block:: bash

      conda config --add channels http://conda.anaconda.org/mutirri

#. How can I remove an existing value (for example, http://conda.anaconda.org/mutirri) from a specific key?

   .. code-block:: bash

      conda config --remove channels http://conda.anaconda.org/mutirri

#. How can I remove a key (for example, the channels key) and all of its values?

   .. code-block:: bash

      conda config --remove-key channels


Conda build and recipes
=======================

#. How can I create a skeleton conda recipe for package such as *bottle* if I
   know that this package is on PyPI?

   .. code-block:: bash

      conda skeleton pypi bottle

   You can then build it with

   .. code-block:: bash

      conda build bottle

SEE ALSO: :doc:`/build_tutorials/pkgs` tutorial.

.. toctree::
   :hidden:

   redirects
   help/silent
   travis
   help/conda-pip-virtualenv-translator.rst

Conda, pip, and virtualenv
==========================

If you are already familiar with pip or virtualenv, please see our chart comparing 
:doc:`Conda, pip, and virtualenv <help/conda-pip-virtualenv-translator>`.

Silent installation
===================

:doc:`Silent installation <help/silent>`  of Miniconda or Anaconda can be used for deployment or testing or building services such as Travis CI and Appveyor.

Using conda with Travis CI
==========================

Conda can be combined with :doc:`continuous integration systems <travis>` such as Travis CI and AppVeyor to provide frequent, automated testing of your code.
