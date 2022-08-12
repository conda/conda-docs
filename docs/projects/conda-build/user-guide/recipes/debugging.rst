=======================
Debugging conda recipes
=======================

Recipes are something that you'll rarely get exactly right on the first try.
Something about the build will be wrong, and the build will break. Maybe you
only notice a problem during tests, but you need more info than you got from the
tests running in conda-build. Conda-build 3.17.0 added the subcommand, ``conda
debug``, that is designed to facilitate the recipe debugging process.

Fundamentally, debugging is a process of getting into or recreating the
environment and set of shell environment variables that conda-build creates
during its build or test processes. This has been possible for a very long
time---you could observe the build output, figure out where the files from your
build were placed, navigate there, and finally, activate the appropriate environment(s).
Then you might also need to set some environment variables manually.

What ``conda debug`` does is to create environments for you and provide you
with a single command line that you can copy/paste to enter a debugging
environment.

Usage
-----

The ``conda debug`` command accepts 1 of 2 kinds of inputs: a recipe folder or
a path to a built package.

If a path to a recipe folder is provided, ``conda debug`` creates the build and host
environments. It provisions any source code that your recipe specifies. It
leaves the build-time scripts in the work folder for you.  When complete, ``conda debug`` prints something like this:

.. code-block:: bash

    ################################################################################
    Build and/or host environments created for debugging.  To enter a debugging environment:

    cd /Users/UserName/miniconda3/conda-bld/debug_1542385789430/work && source /Users/UserName/miniconda3/conda-bld/debug_1542385789430/work/build_env_setup.sh

    To run your build, you might want to start with running the conda_build.sh file.
    ################################################################################

If a path to a built package is provided, ``conda debug`` creates the test
environment. It prepares any test files that the recipe specified. When complete, ``conda debug`` prints something like this:

.. code-block:: bash

    ################################################################################
    Test environment created for debugging.  To enter a debugging environment:

    cd /Users/UserName/miniconda3/conda-bld/conda-build_1542302975704/work && source /Users/UserName/miniconda3/conda-bld/conda-build_1542302975704/work/build_env_setup.sh

    To run your tests, you might want to start with running the conda_test_runner.sh file.
    ################################################################################


Next steps
----------

Given the output above, you can now enter an environment to start debugging.
Copy paste from your terminal and go:

.. code-block:: bash

   cd /Users/UserName/miniconda3/conda-bld/debug_1542385789430/work && source /Users/UserName/miniconda3/conda-bld/debug_1542385789430/work/build_env_setup.sh

This is where you'll hopefully know what build commands you want to run to help
you debug. Every build is different so your experience will vary. However,
if you have no idea at all, you could probably start by running the appropriate
build or test script, as mentioned in the output. If you do this, remember that
these scripts might be written to exit on error, which may close your shell
session. It may be wise to only run these scripts in an explicit subshell:

.. code-block:: bash

    bash conda_build.sh
    bash conda_test_runner.sh


Complications with multiple outputs
-----------------------------------

Multiple outputs effectively give the recipe many build phases to consider. The
``--output-id`` argument is the mechanism to specify which of these should be
used to create the debug envs and scripts. The ``--output-id`` argument accepts
an fnmatch pattern. You can match any part of the output filenames. This really
only works for conda packages, not other output types, such as wheels, because
conda-build can't currently predict their filenames without actually carrying
out a build.

For example, our `NumPy recipe <https://github.com/AnacondaRecipes/numpy-feedstock/blob/master/recipe/meta.yaml>`_ has multiple outputs.
If we wanted to debug the NumPy-base output, we would specify it with a command like:

.. code-block:: bash

   conda debug numpy-feedstock --output-id="numpy-base*"

If you have a matrix build, you may need to be more specific:

.. code-block:: bash

    Specified --output-id matches more than one output (['/Users/msarahan/miniconda3/conda-bld/debug_1542387301945/osx-64/numpy-base-1.14.6-py27h1a60bec_4.tar.bz2', '/Users/msarahan/miniconda3/conda-bld/debug_1542387301945/osx-64/numpy-base-1.14.6-py27h8a80b8c_4.tar.bz2', '/Users/msarahan/miniconda3/conda-bld/debug_1542387301945/osx-64/numpy-base-1.14.6-py36h1a60bec_4.tar.bz2', '/Users/msarahan/miniconda3/conda-bld/debug_1542387301945/osx-64/numpy-base-1.14.6-py36h8a80b8c_4.tar.bz2', '/Users/msarahan/miniconda3/conda-bld/debug_1542387301945/osx-64/numpy-base-1.14.6-py37h1a60bec_4.tar.bz2', '/Users/msarahan/miniconda3/conda-bld/debug_1542387301945/osx-64/numpy-base-1.14.6-py37h8a80b8c_4.tar.bz2']).  Please refine your output id so that only a single output is found.

You could either reduce your matrix by changing your ``conda_build_config.yaml``, or making a simpler one and passing it on the CLI, or by using the CLI to reduce it.

.. code-block:: bash

   conda debug numpy-feedstock --output-id="numpy-base*" --python=3.6 --variants="{blas_impl: openblas}"

.. code-block:: bash

    Specified --output-id matches more than one output (['/Users/UserName/miniconda3/conda-bld/debug_1542387443190/osx-64/numpy-base-1.14.6-py36h28eea48_4.tar.bz2', '/Users/UserName/miniconda3/conda-bld/debug_1542387443190/osx-64/numpy-base-1.14.6-py36ha711998_4.tar.bz2']).  Please refine your output id so that only a single output is found.

However, this is still not enough as our matrix includes two BLAS implementations, MKL and OpenBLAS.

Further reduction:

.. code-block:: bash

   conda debug numpy-feedstock --output-id="numpy-base*" --python=3.6 --variants="{blas_impl: 'openblas'}"

Cleanup
-------

Debugging folders are named in a way that the ``conda build purge`` command will
find and clean up. If you use the -p/--path CLI argument, conda-build will not
detect these and you'll need to manually clean up yourself. ``conda build
purge-all`` will also remove previously built packages.

Quirks
------

You can specify where you want the root of your debugging stuff to go with the
-p/--path CLI argument. The way this works is that conda-build treats that as
its "croot" where packages get cached as necessary, as well as potentially
indexed. When using the --path argument, you may see folders like "osx-64" or
other platform subdirs in the path you specify. It is safe to remove them or
ignore them.
