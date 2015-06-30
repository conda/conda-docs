Quick install
=============

Conda is a cross-platform package manager and environment manager program that installs, 
runs, and updates packages and their dependencies, so you can easily set up and switch 
between environments on your local computer.  Conda is included in all versions 
of **Anaconda, Anaconda Server**, and **Miniconda**.

The fastest way to get and install conda is to `download Miniconda <http://conda.pydata.org/miniconda.html>`_, 
a mini version of Anaconda that includes just conda, its dependencies, and Python. 
Anaconda has all that plus 150+ open source packages that install at the same time, 
and 250 packages that can be installed with the simple ``conda install`` command. 

You can be using Python in two minutes or less with this quick install guide - including 
install, update and uninstall. If you have any problems, please see the full installation instructions.

TIP: If you prefer to have the 150+ open source packages included with Anaconda, 
and have 10 minutes and disk space required, you can download Anaconda simply by 
replacing the word “Miniconda” with “Anaconda” in the examples below.


.. contents::


Miniconda quick install requirements
------------------------------------

32- or 64-bit computer, 32MB available, Linux, OS X or Windows.

NOTE: If you choose to install the full Anaconda package, it requires 300+ MB for 
the download plus another 300+ to install it. 


Linux Miniconda install
-----------------------

In your browser download the `Miniconda installer for Linux <http://conda.pydata.org/miniconda.html>`_, then in your terminal 
window type the following and follow the prompts on the installer screens. If unsure 
about any setting, simply accept the defaults as they all can be changed later:

.. code::

   bash Miniconda-latest-Linux-x86_64.sh

Now close and re-open your terminal window for the changes to take effect.

To test your installation, enter the command ``conda list.`` If installed 
correctly, you will see a list of packages that were installed. 

Next, go to our :doc:`30-minute conda test drive </test-drive>`.

**Linux Miniconda update**

In your terminal window, type the following:  ``conda update conda``

**Linux Miniconda uninstall**

Because Miniconda is contained in one directory, uninstalling Miniconda is simple -- in 
your terminal window, remove the entire miniconda install directory: ``rm -rf ~/miniconda``


OS X Miniconda install
----------------------

In your browser download the `Miniconda installer for OS X <http://conda.pydata.org/miniconda.html>`_, then in your terminal 
window type the following and follow the prompts on the installer screens. If unsure about any setting, 
simply accept the defaults as they all can be changed later.

.. code::

   bash Miniconda-latest-MacOSX-x86_64.sh

Now close and re-open your terminal window for the changes to take effect.

To test your installation, enter the command ``conda list.`` If installed 
correctly, you will see a list of packages that were installed. 

Next, go to our :doc:`30-minute conda test drive </test-drive>`.

**OS X Miniconda update**

Open a terminal window, navigate to the anaconda directory, then type ``conda update conda``.

**OS X Miniconda uninstall**

Because Miniconda is contained in one directory, uninstalling Miniconda is simple -- in 
your terminal window, remove the entire miniconda install directory: ``rm -rf ~/miniconda``


Windows Miniconda install
-------------------------

In your browser download the `Miniconda installer for Windows <http://conda.pydata.org/miniconda.html>`_, then double click 
the .exe file and follow the instructions on the screen.  If unsure about any setting, 
simply accept the defaults as they all can be changed later.

NOTE: When finished, a new terminal window will open. If not, click Start - Run - Command Prompt. 

To test your installation, enter the command ``conda list.`` If installed 
correctly, you will see a list of packages that were installed. 

Next, go to our :doc:`30-minute conda test drive </test-drive>`.

**Windows Miniconda update**

Open a terminal window with Start - Run - Command Prompt, navigate to the anaconda folder, then type ``conda update conda``

**Windows Miniconda Uninstall**

Go to Control Panel, click “Add or remove Program,” select “Python 2.7 (Miniconda)” and click Remove Program. 
