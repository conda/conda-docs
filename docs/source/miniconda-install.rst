====================
Installing Miniconda
====================

.. _cryptographic-hash-verification: https://conda.io/projects/conda/en/stable/user-guide/install/download.html#cryptographic-hash-verification
.. _conda-windows-install: https://conda.io/projects/conda/en/stable/user-guide/install/windows.html
.. _conda-macOS-install: https://conda.io/projects/conda/en/stable/user-guide/install/macos.html

This page contains more complex installation instructions for the major operating systems. For a command-line quickstart installation, see :ref:`Quick Command Line Install <quick-command-line-install>`.

.. note::

   On Windows, macOS, and Linux, it is best to install Miniconda for the local user, which does not require administrator permissions and is the most robust type of installation. However, if you need to, you can install Miniconda system wide, which does require administrator permissions.

.. tab-set::

    .. tab-item:: Windows graphical installer

        #. :doc:`Download the installer. <miniconda>`
        #. (Optional) Verify your installer's SHA-256 checksum. This check proves that the installer you downloaded is the original one.

           a. Open PowerShell version 4.0 or later. For instructions for using Windows PowerShell 3.0 or older, see the `Cryptographic hash verification <cryptographic-hash-verification>`_ instructions in the conda project documentation.
           b. Run the following command, replacing ``filename`` with the path to your installer.

              .. code-block:: powershell

                 Get-FileHash filename -Algorithm SHA256

           c. Check the hash that appears against the hash listed next to the installer you downloaded. See :doc:`all Miniconda installer hashes here <miniconda_hashes>`.

        #. Double-click the ``.exe`` file.
        #. Follow the instructions on the screen. If you are unsure about any setting, accept the defaults. You can change them later.
        #. When the installation finishes, from the Start menu, open Anaconda Prompt.
        #. Test your installation by running ``conda list``. If conda has been installed correctly, a list of installed packages appears.

        `More information on installing in silent mode on Windows is in the conda project documentation <conda-windows-install>`_.

    .. tab-item:: macOS graphical installer

        #. :doc:`Download the installer. <miniconda>`
        #. (Optional) Verify your installer's SHA-256 checksum. This check proves that the installer you downloaded is the original one.

           a. Open a terminal application.
           b. Run the following command, replacing ``filename`` with the path to your installer.

              .. code-block:: shell

                 shasum -a 256 filename

           c. Check the hash that appears against the hash listed next to the installer you downloaded. See :doc:`all Miniconda installer hashes here <miniconda_hashes>`.

        #. Double-click the ``.pkg`` file.
        #. Follow the instructions on the screen. If you are unsure about any setting, accept the defaults. You can change them later.
        #. When the installation finishes, open your terminal application.
        #. Test your installation by running ``conda list``. If conda has been installed correctly, a list of installed packages appears.

        `More information on installing in silent mode on macOS is in the conda project documentation <conda-macos-install>`_.

    .. tab-item:: Linux installer

        #. :doc:`Download the installer. <miniconda>`
        #. (Optional) Verify your installer's SHA-256 checksum. This check proves that the installer you downloaded is the original one.

           a. Open your terminal.
           b. Run the following command, replacing ``filename`` with the path to your installer.

              .. code-block:: shell

                 sha256sum filename

           c. Check the hash that appears against the hash listed next to the installer you downloaded. See :doc:`all Miniconda installer hashes here <miniconda_hashes>`.

        #. In your terminal, run the following command, replacing ``filename`` with the path to your installer.

            .. code-block:: shell

               bash filename

        #. Follow the prompts on the installer screens.

           If you are unsure about any setting, accept the defaults. You can change them later.

        #. To make the changes take effect, close and then re-open your terminal window.

        #. Test your installation by running ``conda list``. If conda has been installed correctly, a list of installed packages appears.

        `For more information on installing in silent mode, see the macOS instructions in the conda project documentation <conda-macos-install>`_.

