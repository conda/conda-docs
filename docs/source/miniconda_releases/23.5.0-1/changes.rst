User-facing changes
^^^^^^^^^^^^^^^^^^^

* Conda has been updated to v23.5.0
* OpenSSL has been updated to version 3
* The default installer uses python-3.11.3


Bug fixes
^^^^^^^^^

* Address a bug that can cause accidental file deletion with Windows uninstallers (see our `blog post <https://www.anaconda.com/blog/windows-installer-security-fix>`_). A `security patch <https://repo.anaconda.com/miniconda/Miniconda3-uninstaller-patch-win-64-2023.07-0.exe>`_ is available for older versions.


Known issues
^^^^^^^^^^^^

* The .pkg installers may skip the "Destination Select" page after accepting the license agreement (see our `Anaconda installation instructions<https://docs.anaconda.com/free/anaconda/install/mac-os/>`_ for details)
