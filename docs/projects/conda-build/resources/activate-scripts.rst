================
Activate scripts
================

Recipes are allowed to have activate scripts
which will be sourced or called when the environment is activated.
It is generally recommended to avoid using activate scripts when
another option is possible because people do not always activate
environments the expected way and these packages may then misbehave.

When using them in a recipe, feel free to name them activate.bat,
activate.sh, deactivate.bat, and deactivate.sh in the recipe.
The installed scripts are recommended to be prefixed by the package
name and a separating -.

Below is some sample code for Unix and
Windows that will make this install process easier.

In ``build.sh``:

.. code-block:: Bash

    # Copy the [de]activate scripts to $PREFIX/etc/conda/[de]activate.d.
    # This will allow them to be run on environment activation.
    for CHANGE in "activate" "deactivate"
    do
        mkdir -p "${PREFIX}/etc/conda/${CHANGE}.d"
        cp "${RECIPE_DIR}/${CHANGE}.sh" "${PREFIX}/etc/conda/${CHANGE}.d/${PKG_NAME}_${CHANGE}.sh"
    done

In ``build.bat``:

.. code-block:: bat

    setlocal EnableDelayedExpansion

    :: Copy the [de]activate scripts to %PREFIX%\etc\conda\[de]activate.d.
    :: This will allow them to be run on environment activation.
    for %%F in (activate deactivate) DO (
        if not exist %PREFIX%\etc\conda\%%F.d mkdir %PREFIX%\etc\conda\%%F.d
        copy %RECIPE_DIR%\%%F.bat %PREFIX%\etc\conda\%%F.d\%PKG_NAME%_%%F.bat
        :: Copy unix shell activation scripts, needed by Windows Bash users
        copy %RECIPE_DIR%\%%F.sh %PREFIX%\etc\conda\%%F.d\%PKG_NAME%_%%F.sh
    )
