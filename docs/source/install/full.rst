Full installation
=================

.. contents::

Conda is a cross-platform package manager and environment manager program that installs, runs, and updates 
packages and their dependencies, so you can easily set up and switch between environments on your local 
computer.  Conda is included in all versions of **Anaconda, Anaconda Server**, and **Miniconda**.

If you are in a hurry, try our two-minute :doc:`Miniconda quick install <quick>`. 
Miniconda includes only conda, conda-build, and their dependencies so you can install cleanly and quickly.

These instructions are for a full install of Anaconda, which includes conda, conda-build, and 150+ 
open source packages. 

TIP: For installation instructions using our graphical installers for OS X or Windows, please see 
the `Anaconda Install <http://docs.continuum.io/anaconda/install.html>`_ page. 


Anaconda requirements
------------------------------------

32 or 64 bit computer, 32MB available, Linux, OS X or Windows.

300 MB to download Anaconda plus another 300 to install it. 

NOTE: You do NOT need root privileges to install Anaconda if you select a user writable install location.

Install instructions
--------------------

Linux Anaconda install 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In your browser download the `Anaconda installer <http://continuum.io/downloads>`_ for 
Linux, then in your terminal window type the following and follow the prompts on 
the installer screens. If unsure about any setting, simply accept the defaults as 
they all can be changed later:

.. code::

   bash Anaconda-latest-Linux-x86_64.sh

NOTE: The install will not take effect until AFTER you close and re-open your terminal window.

**Linux Anaconda update**

In your terminal window, type the following:  ``conda update conda``

**Linux Anaconda uninstall**

Because Anaconda is contained in one directory, uninstalling Anaconda is simple -- in your terminal 
window, remove the entire anaconda install directory: ``rm -rf ~/anaconda``


OS X Anaconda install
~~~~~~~~~~~~~~~~~~~~~

In your browser download the `Anaconda installer <http://continuum.io/downloads>`_ for 
OS X, then double click the .pkg file and follow the instructions on the screen. 
If unsure about any setting, simply accept the defaults as they all can be changed later.

NOTE: The install will not take effect until AFTER you close and reopen your terminal window.

**OS X Anaconda update**

Open a terminal window, navigate to the anaconda directory, then type ``conda update conda``

**OS X Anaconda uninstall**

Because Anaconda is contained in one directory, uninstalling Anaconda is simple -- in 
your terminal window, remove the entire miniconda install directory: ``rm -rf ~/anaconda``


Windows Anaconda install
~~~~~~~~~~~~~~~~~~~~~~~~~

In your browser download the `Anaconda installer <http://continuum.io/downloads>`_ for 
Windows, then  double click the .exe file and follow the instructions on the screen. 
If unsure about any setting, simply accept the defaults as they all can be changed later.

NOTE: When finished, a new terminal window will open. If not, click Start - Run - Command Prompt. 

**Windows Anaconda update**

Open a terminal window with Start - Run - Command Prompt, navigate to the anaconda folder, then type ``conda update conda``

**Windows Anaconda Uninstall**

Go to Control Panel, click “Add or remove Program,” select “Python 2.7 (Miniconda)” and click Remove Program. 
