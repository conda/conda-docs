===================
Conda for pip users
===================

If you've used `pip` and `virtualenv` in the past, you can use conda to perform
the operations you are used to as shown in the table below.

========================= =============================================== ===============================================
Operation                 pip command                                     conda command
========================= =============================================== ===============================================
Install a package         ``pip install $PACKAGE_NAME``                   ``conda install $PACKAGE_NAME``
Install from location     ``pip install --index-url $URL $PACKAGE_NAME``  ``conda install --channel $URL $PACKAGE_NAME``
Update a package          ``pip install --upgrade $PACKAGE_NAME``         ``conda update --name $PACKAGE_NAME``
Uninstall a package       ``pip uninstall $PACKAGE_NAME``                 ``conda remove --name $ENV_NAME $PACKAGE_NAME``
Create an environment     ``cd $ENV_BASE_DIR; virtualenv $ENV_NAME``      ``conda create --name $ENV_NAME python``
Activate an environment   ``source $ENV_BASE_DIR/$ENV_NAME/bin/activate`` ``source activate $ENV_NAME``
Deactivate an environment ``deactivate``                                  ``source deactivate``
Search available packages ``pip search $SEARCH_TERM``                     ``conda search $SEARCH_TERM``
List installed packages   ``pip list``                                    ``conda list --name $ENV_NAME``
Create requirements file  ``pip freeze``                                  ``conda list --export``
========================= =============================================== ===============================================

.. Show what files a package has installed ``pip show --files $PACKAGE_NAME``  not possible
.. Print details on an individual package ``pip show $PACKAGE_NAME``  not possible
.. List available environments   not possible   ``conda info -e``
.. #user will want to pass that through ``tail -n +3 | awk '{print $1;}'``
