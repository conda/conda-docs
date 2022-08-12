# Changelog

## 3.22.0 (2022-08-02)

### Enhancements

* Created function `load_file_data` available in Jinja templates for `meta.yaml` (#4465, #4480)
* Created function `load_str_data` available in Jinja templates for `meta.yaml` (#4465, #4480)
* Support using ``--zstd-compression-level`` to control the compression of v2 style conda packages. (#4467)

### Bug fixes

* When building with Python 3.10, ``STDLIB_DIR`` and ``SP_DIR`` now refer to ``python3.10``, not the symlink ``python3.1``. (#4479)
* Reduce verbosity of urllib3 on the default log level. (#4517)
* Fixed issue identifying DSOs from sysroots when cross-compiling. (#4529)

### Docs

* Improved documentation for `load_setup_py_data` (#4465, #4480)
* Added documentation for `load_file_regex` (#4465, #4480)
* Fix prerequisites for build tutorials link. (#4478)
* Link in contributing docs. (#4532)

### Other

* Fix patch tests. (#4495)
* Added patch/m2-patch as a hard dependency. (#4495)
* Update "Artistic-2.0" license test to use a valid package. (#4516)
* Rename master branch to main. (#4515, #4531)

### Contributors

* @abrahammurciano made their first contribution in #4465/#4480
* @chrisburr
* @conda-bot
* @duncanmmacleod
* @jezdez
* @jakirkham
* @jugmac00 made their first contribution in #4478
* @kathatherine made their first contribution in #4515
* @kenodegard
* @stuarteberg
* @teake
* @travishathaway
* @pre-commit-ci[bot]



## 3.21.9 (2022-05-27)

### Enhancements

* Replace `is_dir` with `scandir` for `channel_root`. (#4273)
* Remove rpaths in `PREFIX/../` that doesn't start with `PREFIX`.
  This includes `BUILD_PREFIX`, `SRC_DIR`. Previously it was only `BUILD_PREFIX`. (#4287)
* Add `entry_points` to outputs in `FIELDS` schema. (#4389)
* Support for `setuptools` 61+. (#4430)
* Use `set` membership for faster indexing. (#4459)

### Bug fixes

* Remove rpaths that occur multiple times. (#4287)
* Enable `bdist_conda` via `entry_point` mechanism supported also by `setuptools >=60.0.0`.
  Usable via `from setuptools import setup` and `setup(distclass=conda_build.bdist_conda.CondaDistribution, ...)`. (#4368)
* Patch `setuptools`'s vendored `distutils.core` as well. (#4434)
* Resolve `conda debug` failure when a trailing slash path is provided. (#4448)
* Fix import error caused by conda 4.13.0's removal of Python 2.7 code. (#4482)

### Deprecations

* Usage of `bdist_conda` via `from distutils.core import setup` and `distclass=distutils.command.bdist_conda.CondaDistribution`,
  as that only works for `setuptools <60.0.0`. (#4368)
* Remove Python 2.7 imports removed in conda 4.13.0. (#4482)

### Other

* Move Windows tests from Azure to GitHub Actions. (#4353, #4436)
* Add pyupgrade to pre-commit. (#4374)
* Move MacOS tests from Azure to GitHub Actions. (#4412, #4436, #4455)
* Update `Makefile` for easier testing. (#4425)
* Remove unused Travis CI configs. (#4438)
* Add MyST to the documentation system and render release notes
  correctly. (#4483)

### Contributors

* @beeankha
* @conda-bot
* @dbast
* @dholth made their first contribution in https://github.com/conda/conda-build/pull/4273
* @isuruf
* @jezdez
* @jakirkham
* @kenodegard
* @remkade made their first contribution in https://github.com/conda/conda-build/pull/4425
* @rchord made their first contribution in https://github.com/conda/conda-build/pull/4353
* @travishathaway made their first contribution in https://github.com/conda/conda-build/pull/4448
* @wimglenn made their first contribution in https://github.com/conda/conda-build/pull/4434
* @pre-commit-ci[bot]



## 3.21.8 (2022-01-25)

### Enhancements

* Adds `--extra-meta key=value` option which allows users to save any specified extra metadata to `about.json`
  to e.g. store the repo-url, git-sha1 or the CI run-id a package was built from.

### Bug fixes

* Old work directories will be preserved when `croot` and `build_id` are set manually

### Other

* Separate contributor related documentation into dedicated file
* Migrating to github actions for tests
* Synced file(s) with conda/infra

### Contributors

* @Lnaden
* @jezdez
* @cjmartian
* @beeankha
* @pre-commit
* @conda-bot


## 3.21.7 (2021-11-30)

### Bug fixes

* Handle an import from the vendored auxlib library in Conda 4.11.0 better.

### Other

* cran-skeleton: more unit tests

### Contributors

* @kenodegard
* @jdblischak
* @jezdez
* @pre-commit


## 3.21.6 (2021-11-09)

### Enhancements

* Add limited support for `platform_system/sys_platform` env markers in PyPI skeleton
* cran-skeleton: Adds a flag `--no-comments` to remove the instructional comments from the recipe files.

### Bug fixes

* When checking for circular dependencies in cross-compiling mode, `build`
  requirements are ignored now.
* Make sure symlinked directories are found in `always_include_files`
* Fix pinning expressions for prerelease builds

### Contributors

* @isuruf
* @mbargull
* @kenodegard
* @jdblischak
* @dbast
* @jezdez
* @ChristofKaufmann


## 3.21.5 (2021-08-06)

### Enhancements

* Revert "Consider any file containing .yaml in its name as maybe a recipe file" (#4235)
* Support setting `build/script_env` values containing "=" (#4211)
* Drop Python 2.7 support from `setup.py` (#4202)
* Make variant configuration error message more informative (#4198)
* Ensure file globs are always sorted (#4186)
* Add preliminary support for `prelink_message` files in conda packages (#4203)

### Bug fixes

* Do not munge rpath for non Mach-O files on macOS (#4238)
* Fix Windows test file extension reported by `conda-debug` (#4224)

### Docs

* Document `build/script_env` recipe option (#4211)
* Clarify wording about selecting multiple operating systems (#4139)

### Contributors

* @chrisburr
* @gabm
* @isuruf
* @jacobtylerwalls
* @katietz
* @kenodegard
* @marcelotrevisani
* @xhochy


## 3.21.4 (2021-01-15)

### Enhancements

* Add new centos 7 distribution cleof to rpm skeleton for s390x.  (#4181)

### Bug fixes

* Fixed bug where symlinks in symlinks caused conda build to exit.  (#4180)

### Contributors

* @mingwandroid
* @beckermr
* @katietz
* @beckermr


## 3.21.3 (2021-01-11)

### Enhancements

* Fix stupid error in prefix replacement  (#4177)

### Contributors

* @mingwandroid


## 3.21.2 (2021-01-11)

## 3.21.1 (2021-01-11)

### Bug fixes

* Fix noarch: python version from version-age determination  (#4174)

### Contributors

* @mingwandroid


## 3.21.0 (2021-01-10)

### Enhancements

* `activate_in_script` defaults to true  (#4120)
* Add Setting and `build/noarch_python_build_age` and fix tests not finding packages  (#4120)
* Allow directories as `license_file` source  (#4153)
* Consider any file containing .yaml in its name as maybe a recipe file  (#4120)
* Add `weak_constrains` and `strong_constrains` `run_exports` types  (#4125)
* Issue a single command for the upload command  (#4120)
* Print `hash_inputs` after upload info  (#4120)
* Add cross-r-base for cross compiling
* Add --build-id-pat option
* macOS: Delete `build_prefix` rpaths
* Use smarter `build_number`
* Combine `default_structs` with FIELDS
* Fix conda render indent from 4 to 2
* macOS: arm64 ci/test-suite setup
* Removing more conda-forge testing deps
* Variants: Be more informative
* more verbosity in tests
* Use MacOSX10.10.sdk, not MacOS10.9.sdk in tests  (#4120)
* Warn when files have been removed from the prefix  (#4120)

### Bug fixes

* Add conda-verify to `install_conda_build_test_deps`  (#4120)
* Add flaky to testing dependencies  (#4138)
* Fix tests not finding packages
* Avoid writing to the package cache in `package_has_file` (collisions)  (#4120)
* Change `package_has_file` to refresh if out of date  (#4120)
* Ensure ~/.condarc does not leak into `testing_config`  (#4120)
* Fix applying patches to read-only files  (#4140)
* Fix auth in aboutjson  (#4137)
* Fix skeleton URLs for CentOS 6 (EOL) and various CI fixes  (#4154)
* Fix typo in cran skeleton  (#4143)
* Force `channel_targets` to be considered used  (#4120)
* Fix printing `bytes-like object is required, not 'str'` when applying patches  (#4118)
* Set "platform" in index.json to the target platform for cross-platform builds  (#4124)
* Reduce `get_rpaths_raw/patchelf` disagree warnings  (#4131)
* LIEF: Allow parsing static libs to fail  (#4149)
* pass `cache_dir` to api.build  (#4120)
* Fix symlinks to directories
* Make post-link `run_export/library_nature` determination less work when `CONDA_OFFLINE=1`
* Remove Python 2.7 from CI matrix
* Fix `test_pypi_installer_metadata` (builds against python 3.9 not 3.7)
* tests: Fix `test_render_with_python_arg_reduces_subspace`
* tests: Update python 3 from 3.5/6 to 3.9 in many
* Set numpy default to 1.16
* tests: Fix pins for `numpy_used`
* tests: CI: Win: Circumvent delayed expansion
* Install patch or m2-patch, write .sh files as binary, more Win tests
* tests: Avoid issue with coverage==5.0 on Win+Py2.7
* Assume non-revisible patches
* Add flaky marker and --strict-markers to setup.cfg
* Don't sort recipes
* Use extra `R_ARGS` and fix them
* shell check fix

### Contributors

* @mingwandroid
* @isuruf
* @mbargull
* @njalerikson
* @cjmartian
* @chrisburr
* @hugobuddel
* @kurtschelfthout


## 3.20.5 (2020-10-26)

### Enhancements

* A new feature `build/ignore_run_exports_from` which will ignore `run_exports`
* coming from a package listed in `build/ignore_run_exports_from`.  (#4114)

### Bug fixes

* Respect PEP440 ~= 'Compatible release clause'  (#4113)
* Detect amalgamated patches  (#4099)
* Handle realpath properly in unsafe patch check  (#4099)
* Force `channel_targets` to be considered used  (#4099)
* Look for git in `build_prefix` in `git_info`  (#4099)
* Fall back to shutil.copy if shutil.copy2 fails when copying patches  (#4099)
* Fix indexing by file  (#4111)
* Helper functions to extract keys  (#4088)
* Simplify `find_config_files` call  (#4086)
* Refactor `dict_of_lists_to_lists_of_dict`  (#4075)

### Contributors

* @mingwandroid
* @isuruf
* @njalerikson
* @cjmartian
* @njalerikson


## 3.20.4 (2020-10-14)

### Enhancements

* Make stats output more easily human-readable  (#4069)
* Prefer meta.yaml `build/error_overlinking` and `error_overdepending`  (#4074)
* Cleanup variant processing code  (#4075)
* Add --file option to indexing  (#4076)

### Bug Fixes

* Remove old rpath when `loader_path` is used  (#4080)
* Fix `MACOSX_DEPLOYMENT_TARGET` default for osx-arm64  (#4091)
* Rewrite `apply_patch` again  (#4092)
* Add a .* to `conditional_regex`  (#4092)

### Contributors

* @isuruf
* @njalerikson
* @cjmartian
* @mingwandroid


## 3.20.3 (2020-09-29)

### Enhancements

* Use `CONDA_PACKAGE_EXTENSIONS` (#4053)
* raise runtimeerror instead of calling sys.exit (#4062)
* Refactor `conda_build.build.get_all_replacements` (#4055)

### Bug fixes

* Do not clobber config argument in `conda_build.build.build_tree` (#4066)
* Use --dry-run to test that a patch applies. Fixes bug 4054 (#4067)
* Include `target_platform` in package build string hash (#4065)
* Fix post linking for SDKs with tapi-tbd-v4 (MacOS 11.0 and upwards) (#4048)


## 3.20.1 (2020-09-04)

### Bug fixes

* Run bash with -e in outputs too #4033
* Add target to recognized fields in `outputs` #4034
* Various overlinking fixes for Windows #4036
* variants: remove hard-coded default path for `CONDA_BUILD_SYSROOT`

### Contributors

* @mingwandroid
* @isuruf
* @mbargull


## 3.20.0 (2020-08-27)

### Enhancements

* enable Python 3.8 on Azure Pipelines (#3841)
* `which_package` can be passed `avoid_canonical_channel_name` (#3952)
* make life easier (less shell exit-y) for those who source test scripts (#3952)
* move old host env instead of deleting it when `--keep-old-work` (#3952)
* convert info.d/*.yaml to info/*.json (#3952)
* allow manual specification of which binary files to prefix replace (#3952)
* filter out '.AppleDouble' folders from recipe searches (#3952)
* re-wrote `apply_patch()` to be more robust (#3952)
* many fixes for DSO post-processing (#3952, #3953)
* add support for (limited) tbd parsing (#3953)
* Make sure packages in current repo data w/ features have versions without features (#3957)
* Check all sysroot locations for DSOs (#3969)
* More helpful error message if an empty string is passed as the hash ('md5', 'sha1' or 'sha256' fields) (#3971)
* the `GIT_DESCRIBE_HASH` variable will be available regardless of whether the sources of the recipe have a git tag or not (#3982)
* add apple silicon support (#4004, #4015)
* set `build_platform` for aid in cross compiling (#4005)
* import macho on non apple system for cross compiling (#4025)
* Add ccache as a jinja 2 function (#4026)
* Improve cpan skeleton (#4026)
* Retry moving host prefix due to Windows file locking (#4026)
* Rename ccache method from mklink to sylinks (#4028)

### Bug fixes

* `conda_build.metadata`: fixed typos in FIELDS (#3866)
* add spaces in CRAN templates (fixes #3943) (#3944)
* raise valid CalledProcessException in macho.otool (#3952)
* cache `local_output_folder` too for `get_build_index` (#3952)
* fix relocations when cross compiling (#3995)
* use `host_platform` instead of sys.platform to facilitate cross compiling (#3997)
* Fix parsing UnsatisfiableError from conda>=4.7.8 (#4001)
* allow packages to depend on themselves when cross compiling (#4011)
* set the correct `SHLIB_EXT` when cross compiling (#4013, #4021)
* inspect linkages with pyldd when not DLL/EXE files (#4019)
* Respect `no_rewrite_stdout_env` on Windows (#4026)
* Prefix replacement fixes (#4026)
* Use git am -3 when applying patches (#4026)
* Fix `env_var=val` assertion (#4026)
* Use exit /B from patch files (#4026)

### Docs

* extend docs o generating the index (#3877)
* add details to documentation of `run_constrained` (#3878)
* remove documentation on `bdist_conda` and environment variables (#3879)
* update cli help information for conda index (#3931)
* Clarify how to install conda-build (#3976)
* Add note for local package install deps (#3980)
* Clarify multiple OS selection (#3984)
* add aarch64 selector to the docs (#4003)
* add docs on `build_platform` and arm64 (#4020)

### Other

* Enable s390x support (#3949, #4030)
* Add xfail test for non-utf-8 charsets (#3972)
* Improve testing on CI (#3987, #4017, #4027)
* Allow python=3.8 for pypi skeletons (#4014)


## 3.19.3 (2020-04-13)

### Bug fixes

* load log prior to calling warn method (#3925)
* test suite fixes and prefix replacement fixes (#3932)

### Other

* Enable ppc64 support (#3921)

### Docs

* Update cli help information for conda index (#3931)

### Contributors

* @beenje
* @jjhelmus
* @mingwandroid


## 3.19.2 (2020-04-01)

### Bug fixes

* Show a warning instead of failing if a Mach-O file is prouduced by a build running on a platform other than macOS (#3912)
* Revert #3893, restores behavior of `build/binary_has_prefix_files` to that found in 3.18.12 (#3916)

### Docs

* clarified 'deletes the build environment' in concepts/recipe.rst (#3901)

### Contributors

* @jjhelmus
* @timsnyder
* @chrisburr


## 3.19.1 (2020-03-17)

### Bug fixes

* Fix issues with PREFIX detection in Windows #3899

### Other

* Change the CI trigger #3904

### Contributors

* @mingwandroid
* @marcelotrevisani
* @jjhelmus


## 3.19.0 (2020-03-10)

### Enhancements

* Keep python pinning in hashing if there is a space #3895
* ci launcher supporting python d shebangs on Windows #3894
* Allow `build/binary_has_prefix_files` to specify a list of files #3893

### Bug fixes

* Use patchelf to set RPATH by default #3897

### Contributors

* @isuruf
* @jjhelmus
* @mingwandroid


## 3.18.12 (2020-03-02)

* Keep python pinning in hashing if there is a space #3895
* ci launcher supporting python d shebangs on Windows #3894
* Allow `build/binary_has_prefix_files` to specify a list of files #3893
* Use patchelf to set RPATH by default #3897
* Prevent non-atomic writes to repodata JSON files #3833
* Audited and updated all docs with formatting, grammar, and accuracy errors.
* Docs: Removed deprecated page on features
* Fixed issue where symlinks to files that do not exist break conda build #3840

### Contributors

* @bdice
* @beckermr
* @chrisburr
* @csoja
* @guidara
* @isuruf
* @jakirkham
* @jjhelmus
* @marcelotrevisani
* @mcg1969
* @mingwandroid
* @msarahan
* @rrigdon
* @saraedum
* @sscherfke
* @zeehio


## 3.18.11 (2019-11-01)

* Update build.sh files of skeletons to be shellcheck clean including test to lint future updates.
* Corrected documentation on subpackage test requirements.
* Do not move work dir to work/work/
* fixed a missing .lower() on two `tar_xf` related util functions
* Fix `has_prefix` detection for Windows.
* `conda_build.inspect_pkg:` optimise use of fnmatch
* Do not consider .ignore files when searching with ripgrep
* Remove `N*N` `os.lstat` calls in `build_info_files_json_v1`

### Contributors

* @msarahan
* @rrigdon
* @marcelotrevisani
* @rrigdon
* @soapy1
* @dbast
* @duncanmmacleod
* @beckermr
* @seanyen
* @AndrewAnnex
* @183amir
* @njzjz


## 3.18.10 (2019-10-14)

### Enhancements

* Added the error message when an invalid pip dependency version expression is used
* Conda skeleton pypi quoting just `version`, `summary` and `description` or attributes with special characters
* Set up CI Azure pipeline for Linux
* Update cran skeleton to match supported optional licenses for license file derivation.
* Migrate Unittests to PyTest
* Update script command on conda skeleton pypi to use `{{ PYTHON }} -m pip install . -vv`
* Add a warning when a received a file on `RECIPE_PATH`
* Refactored the skeletons/pypi.py `get_package_metadata` to be more modular
* added --suppress-variables switch to hide environment variables from console output

### Bug fixes

* Fixed build of '.conda' packages enabled via `conda config --set conda_build.pkg_format 2`
* Workaround for future deprecations of the SafeConfigParser and readfp of the same module.

### Docs

* Remove bzip2 package from build toolkit description.

### Contributors
* @msarahan
* @jakirkham
* @marcelotrevisani
* @duncanmmacleod
* @kinow
* @saraedum
* @jjhelmus
* @rrigdon
* @mingwandroid
* @asford
* @timsnyder
* @mcg1969
* @kaitietz
* @stuarteberg
* @isuruf
* @dbast
* @Bezier89


## 3.18.9 (2019-07-23)

### Enhancements

* add --use-channeldata argument to conda render/build.
* Extract the part in the skeletons pypi responsible to get the package metadata to a free function.
* Creat unittests for the `get_package_metadata` (skeletons/pypi.py) and for the new functions.

### Bug fixes

* Limit threads to 61 on Windows.
* Do not use channeldata for `run_exports` unless --use-channeldata specified.
* Finalize top-level metadata if not present as an output.

### Docs

* Add 3.18.7 release notes

### Other

* Add `disable_pip` to FIELDS

### Contributors

* @rrigdon
* @jjhelmus
* @rrigdon
* @Bezier89
* @jakirkham
* @marcelotrevisani


## 3.18.8 (2019-07-18)

### Enhancements

* `license_file` can optionally be a yaml list

### Bug fixes

* fix readup of existing index.json in cache while extracting
* fix spurious post build errors/warning message
* merge channeldata from all urls

### Contributors

* @msarahan
* @rrigdon
* @jjhelmus
* @isuruf
* @ddamiani


## 3.18.7 (2019-07-09)

### Enhancements

* Update authorship for 3.18.7
* Add note on single threading for indexing during build
* Add in fallback for `run_exports` when channeldata not available
* Make pins for `current_repodata` additive - always newest, and pins are additions to that
* Limit indexing in build to using one thread
* Speed up by allowing empty `run_exports` entries in channeldata be valid results
* Bump conda-package-handling to 1.3+
* Add test for `run_exports` without channeldata
* Fallback to file-based `run_exports` if channeldata has no results
* Add Mozilla as valid license family
* Add in fallback for `run_exports` when channeldata not available
* Updated tutorials and resource documentation

### Bug fixes

* Flake8 and test fixes from pytest deprecations
* Fix in `render.py::_read_specs_from_package`
* Fix for `pkg_loc`
* Fix conda debug output being suppressed

### Contributors

* @msarahan
* @rrigdon
* @rrigdon
* @scopatz
* @mbargull
* @jakirkham
* @oleksandr-pavlyk


## 3.18.6 (2019-06-26)

### Enhancements

* package sha256 sums are includex in index.html

### Bug fixes

* fix bug where package filenames were not included in the index.html

### Contributors

* @rrigdon
* @jjhelmus


## 3.18.5 (2019-06-25)

### Bug fixes

* fix one more keyerror with missing timestamp data
* when indexing, allow .tar.bz2 files to use .conda cache, but not vice versa.  This acts as a sanity check on the .conda files.
* add `build/rpaths_patcher` to meta.yaml, to allow switching between lief and patchelf for binary mangling

### Contributors

* @mingwandroid
* @msarahan
* @csosborn


## 3.18.4 (2019-06-21)

### Enhancements

* channeldata reworked a bit to try to capture any available `run_exports` for all versions available

### Bug fixes

* make "timestamp" an optional field in conda index operations

### Contributors

* @msarahan


## 3.18.3 (2019-06-20)

### Enhancements

* Make VS2017 default Visual Studio
* Add hook for customizing the behavior of conda render
* Drop `/usr` from CDT skeleton path
* Update cran skeleton to use m2w64 compilers for windows instead of toolchain.
  The linter is telling since long: Using toolchain directly in this manner is deprecated.

### Bug fixes

* Update cran skeleton to not use toolchain for win
* fix `package_has_file` so it supports .conda files (use cph)
* fix `package_has_file` function for .conda format
* fix off-by-one path trimming in `prefix_files`
* disable overlinking checks when no files in the package have any shared library linkage
* try to avoid finalizing top-level metadata twice
* try to address permission errors on Appveyor and Azure by falling back to copy and warning (not erroring) if removing a file after copying fails
* reduce the files inspected/loaded for channeldata, so that indexing goes faster

### Deprecations

* The repodata2.json file is no longer created as part of indexing.  It was not used by anything.  It has been removed as an optimization.  Its purpose was to explore namespaces, and we'll bring its functionality back when we address that fully.

### Contributors

* @mingwandroid
* @msarahan
* @rrigdon
* @rrigdon
* @soapy1
* @mariusvniekerk
* @jakirkham
* @dbast
* @duncanmmacleod


## 3.18.2 (2019-05-26)

### Bug fixes

* speed up post-link checks
* fix activation not running during tests
* improve indexing to show status better, and fix bug where size/hashes were being mixed up between .tar.bz2 and .conda files

### Contributors

* @mingwandroid
* @msarahan
* @rrigdon


## 3.18.1 (2019-05-18)

### Enhancements

* rearrange steps in index.py to optimize away unnecessary work
* restore parallel extract and hash in index operations

### Contributors

* @msarahan


## 3.18.0 (2019-05-17)

### Enhancements

* Set `R_USER` environment variable when building R packages
* Make Centos 7 default cdt distribution for linux-aarch64
* Bump default python3 version to 3.7 for CI
* Build docs if any docs related file changes
* Add support for conda pkgv2 (.conda) format
* add creation of `current_repodata.json` - like `repodata.json`, but only has the newest version of each file
* change repodata layout to support .conda files.  They live under the "packages.conda" key and have similar subkeys to their .tar.bz2 counterparts.
* Always show display actions, regardless of verbosity level
* Ignore registry autorun for all cmd.exe invocations
* Relax default pinning on r-base for benefit of noarch R packages
* Make conda index produce `repodata_from_packages.json{,.bz2}` which contains unpatched metadata
* Use a shorter environment prefix when testing on unix-like platforms
* Prevent pip from clobbering conda installed python packages by populating `.dist_info` INSTALLER file

### Bug fixes

* Allow `build/missing_dso_whitelist` section to be empty
* Make conda-debug honor custom channels passed using -c
* Do not attempt linkages inspection via lief if not installed
* Fix all lief related regressions brought in v3.17.x
* Fix ZeroDivisionError in ELF sections that have zero entries
* `binary_has_prefix_files` and `text_has_prefix_files` now override the automatically detected prefix replacement mode
* Handle special characters properly in pypi conda skeleton
* Build recipes in order of dependencies when passed to CB as directories
* Fix `run_test` script name for recipes with multiple outputs
* Fix recursion error with subpackages and `build_id`
* Avoid mutating global variable to fix tests on Windows
* Update CRAN license test case (replace r-ruchardet with r-udpipe)
* Update `utils.filter_files` to filter out generated `.conda_trash` files
* Replace stdlib glob with utils.glob. Latter supports recursion (\*\*)

### Docs

* Updated Sphinx theme to make notes and warnings more visible
* Added tutorial on building R-language packages using skeleton CRAN
* Add 37 to the list of valid values for `CONDA_PY`
* Corrected argparse rendering error
* Added tutorials section, reorganized content, and added a Windows tutorial
* Added Concepts section, removed extraneous content
* Added release notes section
* Reorganized sections
* Clarify to use 'where' on Windows and 'which' on Linux to inspect files in PATH
* Add RPATH information to compiler-tools documentation
* Improve the documentation on how to use the macOS SDK in build scripts.
* Document `conda build purge-all`.
* Fix user-guide index
* Add example for meta.yaml
* Updated theme
* Reorganized conda-build topics, updated link-scripts

### Contributors

* @mingwandroid
* @msarahan
* @rrigdon
* @jjhelmus
* @nehaljwani
* @scopatz
* @Bezier89
* @rrigdon
* @isuruf
* @teake
* @jdblischak
* @bilderbuchi
* @soapy1
* @ESSS
* @tjd2002
* @tovrstra
* @chrisburr
* @katietz
* @hrzafer
* @zdog234
* @gabrielcnr
* @saraedum
* @uilianries
* @theultimate1
* @scw
* @spalmrot-tic


## 3.17.8 (2019-01-26)

### Bug fixes

* provide fallback from libarchive back to python tarfile handling for handling tarfiles containing symlinks on windows

### Other

* Rever support added for releasing conda-build

### Contributors

* @msarahan
* @jjhelmus
* @scopatz
* @rrigdon
* @ax3l
* @rrigdon


## 3.17.7 (2019-01-16)

### Bug fixes

* respect context.offline setting  #3328
* don't write bytecode when building noarch: python packages  #3330
* escape path separator in repl  #3336
* remove deprecated sudo statement from travis CI configuration  #3338
* fix running of test scripts in outputs  #3343
* allow overriding one key of `zip_keys` as long as length of group agrees  #3344
* fix compatibility with conda 4.6.0+  #3346
* update centos 7 skeleton (CDT) URL  #3350

### Contributors

* @iainsgillis
* @isuruf
* @jjhelmus
* @nsoranzo
* @msarahan
* @qwhelan


## 3.17.6 (2018-12-19)

### Bug fixes

* don't raise when recipe text can't be extracted if manual build string is already set  #3326

### Contributors

* @msarahan


## 3.17.5 (2018-12-14)

### Bug fixes

* fix pip build isolation / fix absence of "falsey" env vars.  Ignore only if empty string or None.  #3319
* pass-through VS20XYINSTALLDIR var (used by intel compiler to locate VS2017 installation)  #3322

### Contributors

* @jjhelmus
* @msarahan


## 3.17.4 (2018-12-12)

### Bug fixes

* fix python-3 only JSON decode error handling (make py27 compatible)  #3307
* fix too much caching in getting used vars from meta.yaml leading to inaccurate hash contents  #3311
* fix merge of build/host not being recognized before an `rm_rf` call utilized that info  #3311

### Contributors

* @Lnaden
* @msarahan


## 3.17.3 (2018-12-11)

### Bug fixes

* ignore non-native binaries in lief for now.  Cross-platform inspection still theoretically possible using subdir parameter.  #3306

### Contributors

* @msarahanl


## 3.17.2 (2018-12-11)

### Bug fixes

* fix to ignore unsatisfiable `pin_compatible` calls for packages in other outputs  #3277
* add license files to CRAN recipes generated by conda skeleton  #3284
* restrict py-lief to running on linux/macos only for now  #3291,
* fix lief operation on files that are missing dynamic section (e.g. go binaries)  #3292
* expand instructions on how to setup a dev env for conda-build  #3296
* fix file= keyword being passed to a logger call #3298
* add test for standalone DLLs with py-lief, don't error out on them  #3301
* rename windows build script runner to avoid confusion with existing bld.bat files in root dir  #3303
* fix file URL handling on Windows  #3303
* use conda's download function rather than requests directly, so that conda's proxy settings are respected  #3303
* silence patch output when output verbosity is False  #3305

### Contributors

* @bergtholdt
* @dsludwig
* @jdblischak
* @msarahan
* @nehaljwani
* @sodre


## 3.17.1 (2018-12-04)

### Bug fixes

* omit LIEF depedency on Windows until it is better tested #3288
* activate host environment #3288
* allow calls to nm to fail #3290

### Contributors

* @jjhelmus
* @msarahan
* @nehaljwani


## 3.17.0 (2018-11-28)

### Enhancements

* tell pip to not go find things on PyPI (turn off downloading)  #3109
* new "conda debug" command for creating build/host or test envs for working on recipes  #3237
* new package check: "overdepending" - warns or errors out when your run dependencies include unnecessary shared library packages  #3237
* utilize LIEF for analyzing shared object data, extending capabilities beyond pyldd  #3237

### Bug fixes

* avoid discarding build string during `pin_run_as_build` and `ensure_valid_spec`  #3264
* fix conda index's handling of packages where 'depends' key doesn't exist  #3270
* fix bad inversion assumption about pip's `PIP_NO_DEPENDENCIES` setting  #3271
* fix regex to allow for whitespace after hyphens in outputs section  #3274, #3275
* handle unicode decode fails in output rewriting  #3279
* fix merge of repodata patches that have keys that don't exist in repo  #3280

### Contributors

* @bergtholdt
* @isuruf
* @minrk
* @msarahan
* @mingwandroid
* @nehaljwani


## 3.16.3 (2018-11-21)

### Enhancements

* rewrite long prefix paths as $PREFIX, etc. for more readable build logs  #3258
* make the --output-folder switch configurable in condarc  #3265
* make the --long-test-prefix switch configurable in condarc, fix logic error with that argument  #3266

### Bug fixes

* improve robustness of indexing in face of corrupt package data #3238
* change timeouts to 900 instead of 90  #3239
* add activation to wheel bundling script  #3240
* fix PermissionError import from utils, undefined on py2.7  #3247
* fix outputs with custom build string getting hash incorrectly  #3250
* fix tests not being run on windows  #3257

### Contributors

* @Bezier89
* @gabm
* @isuruf
* @minrk
* @msarahan
* @teake
* @tomashek
* @tschoonj


## 3.16.2 (2018-10-29)

### Bug fixes

* Remove noarch binary file check (do this in conda-verify instead)  #3212
* Fix utf-8 conversion of `check_output_env`  #3213
* fix thread count when indexing causing oversubscription  #3217
* fix behavior of `try_acquire_locks` during lock contention  #3224
* fix test env creation improperly prioritizing local channel  #3229
* don't check for error when removing conda-init (in conda recipe for this repo)  #3230
* add r-impl to R package template generator  #3232
* fix creation of unix and win shell script files for noarch packages  #3236
* fix path of python interpreter used for noarch packages being tested on win, when created on linux/mac  #3236

### Contributors

* @alexandersturm
* @Bezier89
* @dsludwig
* @mandeep
* @mingwandroid
* @msarahan
* @rchateauneu
* @soapy1


## 3.16.1 (2018-10-12)

### Enhancements

* expand ~ in source paths  #3206
* Use binsort when available to sort file list in tar archives, to optimize compressibility  #3210
* allow meta.yaml's build/rpaths key to function on macOS, not just linux  #3206

### Bug fixes

* improve docs on behavior of channel arguments  #3197
* remove mention in docs about building .RPM and .DEB files.  #3199
* fix dist-info errors where dist-info files didn't match the package name  #3206
* fix some hard-coded .tar.bz2 references, to support other compression formats more readily  #3206
* batch calls to compiling .pyc files to avoid problems with maximum command length  #3206
* use `ensure_list` in processing files to be extracted  #3210
* fix KeyError that happened when a jinja2 rendering error occurred, which hid the rendering error  3211

### Contributors

* @mingwandroid
* @msarahan
* @stas00
* @teake


## 3.16.0 (2018-10-05)

### Enhancements

* incorporate libarchive to support more compression formats (adds libarchive as a package dep)  #3163
* add `build/ignore_verify_codes` key to allow recipes to ignore specific conda-verify error codes  #3179

### Bug fixes

* fix JSON string encoding error in index cache reading  #3156
* restore --variants CLI flag for specifying variants  #3168
* handle empty build section in output  #3175
* add `mro-base_impl` as something that causes mro build strings  #3163
* fix skeleton PyPI inappropriately dropping package case (needed for URLs)  #3163
* fix packages from earlier loops with multiple outputs being removed prior to later loops  #3185
* fix conda-index not removing entries from index that no longer exist on disk  #3186 #3188
* clean up tempfiles after indexing  #3187
* fix indexing of specific subdirs  #3190
* fix pypi skeleton when python constraint has no operator  #3191
* fix issues testing packages and recipe folders when done separately from build  #3192
* fix source looking for patches in wrong folder when dealing with outputs  #3194

### Contributors

* @dpryan79
* @gabm
* @mbargull
* @mingwandroid
* @msarahan
* @nehaljwani


## 3.15.1 (2018-09-18)

### Bug fixes

* sort "removed" fns in index repodata.json  #3154
* fix deps being merged instead of clobbered  #3154
* Handle corrupt packages during indexing better  #3154

### Contributors

* @msarahan


## 3.15.0 (2018-09-17)

### Enhancements

* add CLI flag (--strict-verify) to allow erroring out when conda-verify fails a package  #3135
* output text stating that the license file has been successfully found and included with a package  #3152

### Bug fixes

* allow channel auth when checking if a package is built  #3133
* If local git cache can't be updated, delete it and barf (for user to re-run)  #3136
* clean up duplicate pip requirements produced by skeleton  #3138
* replace `recipe_log.txt` file with `recipe_log.json` file (for passing recipe history along with package)  #3139
* fix decoding to str before passing package contents to JSON loading  #3140
* fix loss of "removed" section of index with every other indexing operation  #3144
* fix `update_index` used in tests to index channel, not subdir  #3145
* fix ELF sections not included in memory image of process being loaded by pyldd and giving misleading results  #3148
* fix index operations outputting debug log messages  #3151
* fix private channels showing 404 errors during test phase  #3153

### Contributors

* @Bezier89
* @gabm
* @jakirkham
* @jjhelmus
* @kalefranz
* @msarahan
* @stuarteberg
* @teake


## 3.14.4 (2018-09-11)

### Bug fixes

* fix `recipe_log.txt` not being filtered from info/files  #3134

### Contributors

* @msarahan


## 3.14.3 (2018-09-11)

### Enhancements

* add support for index patch instructions as tarballs containing subdirs  #3129
* add progress bars for indexing (using tqdm)  #3130

### Bug fixes

* fix log messages being deduplicated too much  #3130
* handle permission errors with moving files in indexing more gracefully  #3132

### Contributors

* @msarahan


## 3.14.2 (2018-09-07)

### Enhancements

* add support for a "recipe log" file.  This will be used at Anaconda to capture the commit activity of a given recipe, which will be published in the RSS feed.  #3123

### Bug fixes

* fix indexing of noarch subdir as done by conda-forge  #3120
* decode cached index files to utf-8 before reading JSON  #3121
* try to address unicode problems in `run_exports` handling  #3121
* skip over index metadata files when they are not present in a package  #3125

### Contributors

* @msarahan


## 3.14.1 (2018-09-06)

### Bug fixes

* detect and fall back to old `update_index` behavior (new is channel-wide; old is specific subdir)  #3117
* fix `CONDA_BUILD_STATE` not being set when `load_setup_py_data` gets run  #3117
* fix `channel_name` as CLI argument for conda index.  It can't be positional.  #3318

### Contributors

* @msarahan


## 3.14.0 (2018-09-04)

### Enhancements

* refactor indexing to cache more efficiently  #3091
* add `tags`, `identifiers`, and `keywords` to about section.  Tie them into channeldata.json.  #3091
* filter .la files from packages by default  #3102
* memoize `read_meta_file`  #3108

### Bug fixes

* fix --check for optionally iterable fields  #3098
* fix permission problems prior to fixing shebangs  #3101
* do not disable pip's cache directory.  Redirect it instead.  #3104
* fix usage of config in `load_setup_py_data`  #3110
* show logger message when default numpy is used, to communicate what's happening to the user  #3110

### Other

* drop python 3.4, add 3.6, 3.7 to skeleton pypi  #3103

### Contributors

* @jjhelmus
* @kalefranz
* @msarahan
* @nehaljwani
* @nsoranzo
* @ocefpaf
* @teake


## 3.13.0 (2018-08-20)

### Enhancements

* add `run_exports` and aggregated post-install metadata indexing outputs  #3060
* allow whitelisting runpath entries  #3072
* consider `*_compiler_version` entries when looping over variants (allow `*_compiler_version` to be a used variable that affects the hash)  #3084

### Bug fixes

* fix cached git info for variants  #3082
* fix linux temporary channel not being added at test time, leaving package unresolvable  #3088

### Contributors

* @msarahan
* @teake


## 3.12.1 (2018-08-06)

### Enhancements

* add the "extra" field of a package's meta.yaml file into the output package's info/about.json file  #3048
* add option to omit local channel in `is_package_build` (used by c3i)  #3051
* add pip env vars to prevent it from pulling in external dependencies when used in build scripts  #3053

### Bug fixes

* fix local channel always being top priority.  Allow user-defined channel orders where local is lower than remotes.  #3049
* Fix conda-verify import error warning showing up in --output text  #3052
* fix RPM skeleton test (point to newer CentOS repo) #3054
* fix test/files and `test/source_files` looking in the wrong place for info/recipe/parent contents (subpackages)  #3061

### Contributors

* @Bezier89
* @jakirkham
* @mikecormier
* @mingwandroid
* @msarahan


## 3.12.0 (2018-07-24)

### Enhancements

* Allow user-specified channels to come ahead of local channel  #3038
* Add schema for outputs section in FIELDS; provide method for getting rendered recipe text (to support conda-verify)  #3041
* Enable conda-verify by default when it is importable, but only print warnings by default, instead of exiting  #3042
* Add --label CLI argument to allow specifying label for uploading packages to  #3043

### Bug fixes

* fix `apply_selectors`, leading to excessive detection of used variables  #3040

### Contributors

* @CJ-Wright
* @msarahan
* @speleo3


## 3.11.0 (2018-07-20)

### Bug fixes

* improve environment marker support for pypi skeleton  #2972
* apply selectors before checking requirements, to better understand per-platform used vars  #2973
* Handle conda UnsatisfiableError causing packages to be moved to broken folder without tests actually being run on them  #2974 #2975
* use tempfiles when writing index to reduce risk of corrupt index  #2978
* handle conda index recipe info for older versions of conda-build  #2979
* allow empty `missing_dso_whitelist` in build section  #2983
* fix `host_reqs` referring to a detached list, leading to requirements/host not being modified by `run_exports`  #2987
* fix for bypassing MITM proxies based on `SSL_NO_VERIFY` env var  #2991
* add `missing_dso_whitelist` to FIELDS  #2994
* Don't skip logic in pyldd based on CB verbosity (--quiet)  #2999
* Convert empty git refs to HEAD, so that `git_url` behavior is more predictable  #3003
* set `NPY_DISTUTILS_APPEND_FLAGS=1` so the compiler package flags are respected  #3015
* fix script file renaming when converting package from win to unix  #3014
* allow fn to be omitted when using multiple url sources  #3021
* fix default config settings being shared across Config instances  #3022
* force text interpretation of CRAN DESCRIPTION files  #3020
* fix `is_no_link` to honor patterns  #3023
* fix test/requires being ignored when --no-copy-test-source-files is specified  #3027
* fix up dependencies in CRAN skeleton output  #3030 #3032

### Enhancements

* change skeleton pypi to generate recipes that use pip for install step.  Remove description.  #2972
* Set environment variable to disable pip environment isolation to prevent problems  #2972
* support multiple `exclusive_config_files`  #3022

### Docs

* Fix search order for `conda_build_config.yaml`  #3029

### Contributors

* @isuruf
* @j-hartshorn
* @kalefranz
* @mandeep
* @mbargull
* @mcg1969
* @mingwandroid
* @minrk
* @msarahan
* @nehaljwani
* @ocefpaf
* @tjd2002


## 3.10.9 (2018-06-15)

### Other

* docs are moving from the conda-docs repo into conda-build (splitting off from conda docs in general)

### Bug fixes

* fix re.escape usage for Python <3.3 #2970

### Contributors

* @mbargull
* @msarahan


## 3.10.8 (2018-06-12)

### Bug fixes

* clean up license field for pypi skeleton  #2938
* fix regex to match requirements with trailing spaces  #2948
* Check for dash in text with variants  #2949
* do not check in build prefix for overlinking when merging build and host  #2950
* utils.glob: remove unnecessary normcas, fix `test_expand_globs`  #2952
* add missing "build" fields in FIELDS schema thing  #2962

### Contributors

* @isuruf
* @mariusvniekerk
* @mbargull
* @mingwandroid


## 3.10.7 (2018-06-01)

### Enhancements

* replace glob2 by glob for py3 (speed improvement)  #2937

### Bug fixes

* Fix folder copying in test/files  #2941

### Contributors

* @mbargull
* @msarahan


## 3.10.6 (2018-05-31)

### Enhancements

* several rendering speed improvements #2925

### Bug fixes

* add regression test for #2912       #2914
* fix a file handle not being closed  #2915
* fix an incorrect syntax RuntimeError  #2920
* fix custom compiler languages not being possible  #2927
* fix OS vars not correctly respecting test prefix; add test  #2932
* fix incorrect python versions showing up in test phase paths (`SP_DIR`)  #2932
* fix test/files functionality for outputs; add test  #2934

### Contributors

* @mbargull
* @msarahan
* @nicoddemus
* @rainwoodman
* @sodre
* @tomashek


## 3.10.5 (2018-05-23)

### Enhancements

* allow '\*' as an `ignore_run_exports` value to ignore all `run_exports`  #2907

### Bug fixes

* fix handling of empty run and test requirements  #2908
* fix trailing zeroes in version numbers getting lost by yaml interpreting things as floats  #2909
* fix regression in host prefix showing up in the test phase, leading to files/executables not being where they should be  #2910
* fix handling of not-yet-available requirements  #2912
* fix `get_value` with default keyword not respecting that user-specified default  #2912

### Contributors

* @msarahan


## 3.10.4 (2018-05-20)

### Bug fixes

* fix import tests being run multiple times  #2892
* add creative commons as a license family (used to be classified OTHER)  #2893
* handle empty packages in checks for duplicated files across subpackages  #2894
* set PYTHON and other language path vars based on presence in build/host reqs, rather than binary file in either env.  Allows usage of PYTHON and friends in meta.yaml vars.  #2895
* fix entry points incorrecty pointing at build prefix (instead of host), leading to prefix replacement failing  #2895
* fix `merge_build_host` functionality.  Adding an empty host section now forces build and host to be split.  #2896

### Contributors

* @msarahan
* @scopatz


## 3.10.3 (2018-05-17)

### Enhancements

* --skip-existing applies to outputs, not just whole collections of packages.  Individual outputs that are already built will be skipped.  #2889
* add output of hash contents to what gets printed with conda render (not with --output)

### Bug fixes

* fix conda pypi skeleton checking for '~' in None values  #2880
* add /B to win exits, so that erroring out of tests does not close out of outer shells  #2881
* ensure that `merge_build_host` is updated correctly for each output #2882
* Remove several env vars from being recorded in about.json, over concerns for GDPR compliance #2883
* remove `parent_recipe` entry from recipes when recording meta.yaml for output packages, to avoid confusion over used variables #2886
* xfail `get_installed_version` for new conda and `test_build_with_activate_does_activate` when PATH is too long  #2889
* change os.rename to shutil.move so that there is a copy fallback  #2889
* fix mutability of config objects passed to test causing bizarre states of variants
* fix win style slashes in paths.json and `files` that broke things when converting a win package to unix #2891

### Contributors

* @mingwandroid
* @msarahan


## 3.10.2 (2018-05-08)

### Bug fixes

* fix downstream test not using channel list; fix exact specs in downstream testing  #2864
* add deprecation notice for `msvc_compiler` key in meta.yaml.  Explain its incompatibility with variants.  #2868
* set default cran mirror  #2868
* disallow merging of build and host prefixes when `host_subdir != build_subdir`  #2876

### Contributors

* @msarahan


## 3.10.1 (2018-05-01)

### Bug fixes

* fix handling of downstream testing when downstreams don't exist yet (e.g. bootstrapping)  #2860
* fix handling of downstream testing in tandem with --output-dir or --croot (add locations as file:// urls)  #2860
* fix improperly escaped entries in cran template.  Clean up unnecessary changes.  #2861

### Contributors

* @mingwandroid
* @msarahan


## 3.10.0 (2018-05-01)

### Enhancements

* Warn user about path conflicts during environment building for test phase  #2843
* Add conda 4.6 compatibility   #2844
* **remove conda 4.2 and earlier compatibility**  #2845
* add info to merge/copy source subdir error  #2858
* Add setup for Air Speed Velocity benchmarking  #2859

### Bug fixes

* fix python handling when python is a tuple (inner python looping)  #2854
* fix python not looping in inner packages when top-level doesn't use it.  Fix `zip_keys` handling. #2856

### Contributors

* @kalefranz
* @msarahan


## 3.9.2 (2018-04-27)

### Enhancements

* Optimizations to rendering to speed up dealing with lots of recipes  #2838 #2848

### Bug fixes

* include `folder` as a field in `source` for linting purposes  #2837
* remove merging of constraints.  Keep only the clobbering of groups of constraints by exact constraints (of which you can have only one)  #2839
* ensure u+w permissions before calling `install_name_tool`  #2840
* remove conversion of dash to underscore in `pin_run_as_build`  #2842

### Contributors

* @jakirkham
* @mingwandroid
* @msarahan


## 3.9.1 (2018-04-24)

### Bug fixes

* Revert #2831 (add license file for R packages from CRAN) due to incompatibility with package layout in defaults
* handle OrderedDict dumping to yaml better; further work on preserving dict key order in config yaml files  #2834
* consolidate cran default repo settings, respect variant setting better.  #2836
* Add `conda-build/skeleton_config_yaml` key to condarc to control which `conda_build_config.yaml` should be used to find the `cran_mirror` setting.  #2836
* Change default cran mirror from mran to cran.  #2836

### Contributors

* @mingwandroid
* @msarahan


## 3.9.0 (2018-04-24)

### Enhancements

* Add new key in test section, `downstreams` that accepts a list of package specs to test after the current package is built  #2823
* work to prevent unsafe paths in tarballs that would affect paths outside of the work dir  #2822
* simplify all constraints for a given package name to a single constraint that represents the tightest combination of them all  #2694

### Bug fixes

* fix a misnamed cran skeleton key  #2817
* Remove unused index command in rendering path  #2818
* fix loss of ordering when using `recipe_append`  #2825
* fix usage of dict for default `pin_run_as_build` data structure.  Losing ordering created noise down the line for Conda-Forge.  #2830
* fix selector regex being too greedy; reporting wrong used vars  #2832

### Contributors

* @ceball
* @isuruf
* @jamesabbott
* @jdblischak
* @mingwandroid
* @msarahan


## 3.8.1 (2018-04-16)

### Bug fixes

* fix shebang rewriting so that it only touches python[w]? shebangs  #2786
* fix a regression in ignoring python as a build-only dep being "used" and becoming a loop var #2799
* improve config log warning  #2801
* skip, but warn about failures in pyldd  #2802
* fix whitespace in multi-line help strings  #2808
* fix variables in compound selectors not getting detected as "used"  #2814

### Contributors

* @bjlittle
* @jbcrail
* @mingwandroid
* @msarahan


## 3.8.0 (2018-03-30)

### Enhancements

* Add new jinja2 function, `resolved_packages`, that can be used to pin run or
  test requirements to indirect dependencies as well as direct dependencies  #2715

### Bug fixes

* Fix R/Rscript mixup that broke usage of R env var  #2782
* Improve error message when additional modules are needed in root env in order to render a recipe  #2784
* Fix handling of `FEATURE_NOARCH`, which was adding specs that conda's solver didn't understand  #2787
* allow `license_file` to be found in either source root or recipe root (common point of confusion)  #2792
* fix `disable_pip` removing setuptools even when it was an explicit dependency.
  This was due to conda changing its string representation of MatchSpecs, and
  our regex didn't take that into account. #2793

### Contributors

* @183amir
* @msarahan


## 3.7.2 (2018-03-22)

### Enhancements

* add runpath handling to pyldd  #2768
* add lgtm.com configuration  #2772

### Bug fixes

* fix language issues with finding directory size on windows #2749 #2766  #2760
* ignore non-rendered jinja2 errors when indexing packages  #2756
* fix cran skeleton argparse errors when version flag not provided  #2751 #2759
* fix exact pinning in subpackages raising errors due to non-final output data conflicting with final top-level data  #2763
* skip `test_preferred_env` until conda more fully implements it  #2722
* Don't run `mk_relative_osx` on linux DSO's  #2768
* use Rscript to run R tests, so that console output is shown more clearly.  Only add r-base spec if neither r-base nor mro-base are already in deps.  #2764
* don't filter out .gitignore and .gitmodules when packaging  #2774
* fix `pin_*` regex that was erroneously picking up wrong usages  #2775

### Contributors

* @bilderbuchi
* @kfranz
* @m-rossi
* @mingwandroid
* @msarahan
* @wikiped


## 3.7.1 (2018-03-08)

### Enhancements

* Enable glob2.fnmatch for shared library whitelists.  Add more Frameworks to whitelist on Mac.  #2732

### Bug fixes

* Squelch yaml ScannerError when building index can't read meta.yaml in package  #2740
* Fix & simplify "hoisting" of source folders up one level  #2741
* Fix build number not getting inherited from top-level metadata  #2742
* Allow output creation environment for wheels to be activated  #2744
* Fix selector regex for finding "used" variables; was finding too much across lines.  #2745
* Ignore empty config files (don't error out on them)  #2746

### Contributors

* @mingwandroid
* @msarahan
* @neok-m4700


## 3.7.0 (2018-03-05)

### Enhancements

* raise ValueError when `pin_subpackage` is used, but no matching output is found  #2720
* Add new optional CLI argument, --extra-deps, to add test-time dependencies dynamically when splitting build and test phases (can't apply variants when phases are split)  #2724

### Bug fixes

* fix cran skeleton py2 invalid list copy syntax  #2720
* reconfigure TravisCI to test against conda master  #2720
* fix inaccurately raised problems with `pin_subpackage`  #2720
* coerce boolean values in `conda_build_config.yaml` to booleans (value.lower() == "true")  #2723
* change r skeleton cran test to a different package (nmf -> acs); nmf got removed
* fix selectors being applied before variable detection, leading to variables in selectors never being detected  #2723
* add filesize calculation to converted script files  #2727

### Contributors

* @mandeep
* @msarahan


## 3.6.0 (2018-02-28)

### Enhancements

* Allow per-output {pre,post}-{un,}link scripts  #2712
* support mro as part of the build string  #2711
* improve interpreter guessing for running output packaging scripts  #2709
* improve library overlinkage check, add support for whitelists of always-ok
  libraries to ignore. #2708
* add support for noarch: generic recipes in cran skeleton generator
* add support for using Rtools on windows when building a package from source
* add support for binary repackaging of CRAN/MRAN artifacts
* add support for cran recipes from source tarballs
* template `cran_mirror` variable in generated cran output recipes. This allows
  CRAN and MRAN to easily be switched out. Default is MRAN.  #2710

### Bug fixes

* Reverse build/host activation order, to give build executables higher
  priority. Necessary to support proper R packaging. Includes better errors for
  empty packages caused by build env python being used to install python
  packages. #2686
* Fix test scripts from subpackage outputs not being detected  #2703
* Fix sha in scripts in conversion from linux to windows packages (was not
  correctly handling hashbang addition/removal). #2713
* Speed up stat gathering, restrict it more to only build, packaging, and test
  steps (not arbitrary subprocess calls) #2714
* Check for incomplete files when inspecting links. Some files that looked like
  ELF files, but weren't, would trip up pyldd and kill the build.  #2718

### Contributors

* @jjhelmus
* @MatthieuDartiailh
* @mingwandroid
* @msarahan


## 3.5.1 (2018-02-22)

### Enhancements

* Add relative path support for `load_setup_py_data` jinja2 function  #2700

### Bug fixes

* fix hoisting of archives containing folders named same as top-level folder.  These subfolders were being removed inappropriately.  #2692
* Fall back gracefully when psutil fails to import.  Disk and total time stats still available; memory and CPU time are not when psutil is unavailable.  #2693
* Fix directory size computation not being recursive, use scandir for walk operations on py27  #2699

### Contributors

* @mariusvniekerk
* @msarahan


## 3.5.0 (2018-02-20)

### Enhancements

* Print resource statistics for each step, as well as whole.  CPU time, memory usage, disk usage.  #2685
* Record resource statistics to JSON file when `--stats-file <output_file_path>` argument is provided  #2685

### Bug fixes

* save complete parent recipe in info/recipe/parent for packages that are only outputs of a top-level package  #2687

### Contributors

* @msarahan


## 3.4.2 (2018-02-15)

### Enhancements

* allow trimming of skipped metadata in rendering to be optional (for sake of
  conda-forge rendering readme's on platforms that are skipped) #2680
* rename the build prefix prior to the test phase. This will precipitate
  failures when packages embed paths to the build prefix, which conda does not
  replace at install time. Fixing these instances is specific enough to packages
  that we do not attempt to handle it in conda-build. #2681
* add `conda_interface.get_install_version` function that facilitates checking if
  a pkg is in an env, and if so, what its version is #2682

### Bug fixes

* use lookaheads in extraction regexes to avoid capturing unwanted text  #2679

### Contributors

* @msarahan


## 3.4.1 (2018-02-08)

### Bug fixes

* fix interpretation of `zip_keys` when testing pkgs (ignore empty values)  #2673

### Contributors

* @msarahan


## 3.4.0 (2018-01-31)

### Enhancements

* implement "--exclusive-config-file" CLI flag to render & build. This file
  bypasses detection of config files in $HOME and cwd, but respects any config
  files in recipe folders. #2661
* Activate output scripts in meta.yaml ( #2667 ), but only when:
* output has a build/script entry
* output uses `{{ compiler() }}` jinja2 function in its requirements AND output extension is either .sh or .bat
* output has `build/activate_in_script` key in meta.yaml set to a truthy value AND output extension is either .sh or .bat

### Bug fixes

* fix AttributeError in overlinking check  #2650 #2651
* reorder mmap operations to fix problem with WSL  #2655
* fix numpy detection as "used" variable when using `pin_compatible` jinja2  #2659
* silence conda KeyError warnings when indexing legacy packages that don't have newer metadata files  #2656
* replace "which" with "type -P" in conda-build's internal recipe.  This avoids issues on PowerPC and with long paths.  #2664
* Error out when version computation fails in conda-build's setup.py. This will
  help prevent conda-build packages going out without valid internal versions
  being recorded (for example, when git is not installed on a build worker).
  #2665
* ignore tarcheck errors for files in the info folder that don't appear in info/files file.  Fixes inclusion of arbitrarily named readme files.  #2668
* clean up host prefix in between skeletons when using pypi's --recursive mode.  Conda otherwise throws errors on the 2nd recipe.  #2669

### Contributors

* @kfranz
* @mingwandroid
* @msarahan
* @nehaljwani
* @neok-m4700
* @steamelephant


## 3.3.0 (2018-01-23)

### Enhancements

* Issue template created for github repo  #2632
* Detect overlinking (usage of libraries that are not present in listed dependencies).
  Warn by default.  Error out with --error-overlinking flag.  Conda-build 4.0 will
  error by default.  #2635 #2647

### Bug fixes

* fix `merge_build_host` to always be used in CRAN skeletons  #2635
* fix macho filename attribute error  #2641
* reorder search through files for compatibility bounds for speed  #2638
* cache used vars based also on recipe path, to avoid overly caching results  #2643
* normalize slashes in file glob lists for explicit output file lists  #2644
* silence conda 4.4 better when using quiet operations, such as --output  #2645
* fix `pypi_url` not affecting the url of the actual skeleton output from conda skeleton pypi  #2646
* fix overly broad string matching of "None" that caused problems where None may appear
  as part of a string in meta.yaml  #2649

### Contributors

* @csoja
* @mingwandroid
* @msarahan
* @nehaljwani
* @neok-m4700


## 3.2.2 (2018-01-12)

### Enhancements

* Add CLI flag (--merge-build-host) to restore pre-3.1.4 behavior with merging build and host envs  #26260

### Bug fixes

* Check recipe/metadata skip status in more places, rather than strictly at the top-level  #2617
* fix unnecessary conforming of zip keys when distributing variants  #2618
* fix matching of unrendered output names when matching rendered names  #2618
* fix matching of partial (only used parts) of variants when lining up subpackages  #2618
* fix handling of outputs with same name as top level when considering used vars  #2618
* exclude top-level `run_exports` from applying to all outputs  #2618
* Fix linking compiler runtimes from build to host prefix (was broken by build/host prefix split in 3.1.4)  #2621
* Fix logic errors around merging build/host envs  #2623
* fix `run_exports` in outputs being overwritten  #2623

### Contributors

* @jjhelmus
* @mingwandroid
* @msarahan


## 3.2.1 (2018-01-02)

### Enhancements

* Improve "BUILD" environment variable value (especially on powerpc)  #2615
* Implement CentOS 7 ppc64le distro for conda skeleton rpm  #2615
* Improve handling of outputs that use the build/skip key to skip building  #2616

### Bug fixes

* Don't loop in all zipped keys when collecting used vars.  Leave it to consumers to decide what to do.  #2612
* Fix `run_exports` using `pin_subpackage` not applying versioning for the implicit top-level output  #2613
* Fix `run_exports` not applying to build-time environment creation for top-level recipe (as opposed to outputs)  #2613
* Fix CRAN skeleton to better use host/build envs appropriately  #2614
* fix outputs not loading hash input info from files at test time correctly, leading to incorrect hashes and unresolved packages.  #2616

### Contributors

* @mingwandroid
* @msarahan


## 3.2.0 (2017-12-21)

This release bumps the minor version to reflect the change in splitting the
build and host folders originally introduced by 3.1.4. That change has proven to
be disruptive to many users, and we felt it necessary to bump a minor version to
indicate that people should pay attention to this change. There's more info in
our docs at
https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#host

### Enhancements

* Add log messages for each source of variants, so that you know where values are coming from  #2597

### Bug fixes

* remove unnecessary looped `rm_rf` when cleaning out prefixes between outputs  #2587
* fix meta.yaml not found errors when trying to test packages built with --no-include-recipe  #2590
* fix zipped key group with single entry causing a list to be passed later for single string values  #2596
* fix incomplete change to splitting build and host envs  #2595
* fix merging of top-level requirements and output reqs when output named same as top-level  #2595
* fix handling of outputs with templates in their name (they were losing their requirements)  #2595
* fix test file copying to avoid re-provisioning source during tests  #2595
* tweak requirements regex to avoid misinterpreting python executable usage in test commands as usage of the python variant  #2595

### Contributors

* @msarahan


## 3.1.6 (2017-12-15)

### Bug fixes

* fix test files in outputs (was losing reference to absolute path of recipe)  #2584
* fix several incorrect references to `build_prefix` that needed to be `host_prefix`  #2584

### Contributors

* @msarahan


## 3.1.5 (2017-12-15)

### Enhancements

* detect "used" variables in selectors  #2581

### Bug fixes

* Cache used variables for a given output on a given target platform to avoid
  recomputing this too often. This dramatically speeds up operations relative to
  3.1.4. #2581
* fix used variable treatment of `target_platform`  #2581

### Contributors

* @msarahan


## 3.1.4 (2017-12-14)

### Enhancements

* detect "used" variables in build.sh, bld.bat and any output scripts, in
  addition to what already existed in meta.yaml. Used variables end up in the
  hash. #2576
* don't merge build and host prefixes. We used to do this when host subdir ==
  build subdir. Keep them separate, so that build tools in build prefix won't
  ever interfere with software installed to host, to be packaged.  #2579

### Bug fixes

* exclude grouped keys from `zip_keys` when computing hashes.  Only direct dependencies affect the hash.  #2573
* fix `always_include_files` usage omitting other ordinarily installed files  #2580

### Contributors

* @msarahan


## 3.1.3 (2017-12-13)

### Enhancements

* support environment variable expansion in path-related condarc settings  #2563
* speed up "fixing linking" on MacOS by ~98%  #2564
* Allow build/script and `build/script_env` entries in outputs, for simple scripts
  and for passing env vars into output scripts  #2572

### Bug fixes

* fix `run_exports` from build section not applying to host early enough and causing conflicts  #2560
* order outputs based on build, host, and run dependencies, not just run  #2561
* fix `always_include_files` when used in output sections  #2569
* add jinja2 to dependencies in setup.py (not just in conda.recipe)  #2570

### Contributors

* @akovner
* @mingwandroid
* @msarahan
* @nehaljwani
* @rlizzo
2017-12-9 3.1.2:

### Bug fixes

* fix copying of relative paths with `source_files` in test section  #2551
* fix handling of too many x's in `max_pin` field.  If more x's than actual places were present, the incrementing broke.  #2552
* refactor upstream pinning, fix extraction of outputs so that `run_exports` and `pin_compatible` work with them  #2556
* fix bug that occurred when an output had the same name as the top level recipe.  Ended up extracting wrong part of recipe with wrong regex.  #2556
* fix copying of recipe losing folder structure in the destination copy of the recipe  #2557

### Contributors

* @msarahan
* @nehaljwani


## 3.1.1 (2017-12-06)

### Bug fixes

* fix info files filters on windows  #2542
* fix icon.png files that needed to be included in the app section of recipes, for usage with Navigator  #2545
* fix package matching regex for packages with `-` in them (regex should find either `-` or `_`)  #2546
* fix detection of used variant variables within jinja2 conditionals  #2547
* fix output extraction regex (was picking up whole outputs section, not just one
  output). Also, fix top-level variables not being carried into later outputs.  #2549

### Contributors

* @jjhelmus
* @msarahan


## 3.1.0 (2017-12-05)

### Enhancements

* Speed up package inspection by optimizing package file lookup  #2535
* Simplify hashing scheme.  A hash will be added if all of these are true for any dependency:
* package is an explicit dependency in build, host, or run deps
* package has a matching entry in `conda_build_config.yaml` which is a pin to a specific version, not a lower bound
* that package is not ignored by `ignore_version`
  OR
* package uses `{{ compiler() }}` jinja2 function
  All other packages will no longer have hashes. The takeaway message is that
  hashes will appear when binary compatibility matters, but not when it doesn't.  #2537

### Bug fixes

* Allow packages to store files in info folder  #2538
* Fix `source_files` not working correctly when using test files in packages  #2539

### Contributors

* @mingwandroid
* @msarahan


## 3.0.31 (2017-11-30)

### Enhancements

* expose time and datetime modules in jinja2 context, for use in meta.yaml  #2513
* jinja: permit recipes to check for existence of a variable without erroring  #2529
* add method for getting all variant values used by a recipe, not just those variants with more than one value.  #2531

### Bug fixes

* allow `SSL_NO_PROXY` env var to disable SSL checking on proxied connections  #2505
* Fix source hoisting issues (incorrectly flattening directory structure of extracted archives)  #2507
* Fix build env for output getting lost when output name == top-level name  #2511
* add global `pin_run_as_build` for R (x.x.x) to keep legacy R pinning behavior  #2518
* Fix path conversion issues going from windows to unix  #2522
* only insert variant versions when testing runtime availability for packages that are also present in build (not just run)  #2527

### Contributors

* @anton-malakhov
* @bheklilr
* @mandeep
* @msarahan
* @stuarteberg


## 3.0.30 (2017-11-15)

### Bug fixes

* write all 'about' metadata fields out, not just select few  #2488
* fix lists getting nested during merging of configs, leading to TypeErrors  #2494
* make `always_include_files` act on `host_prefix`, not `build_prefix`  #2497
* warn users when `script_env` passes env vars through #2502
* fix build string pyXY being just pyX when input didn't have full python version  #2504

### Contributors

* @jakirkham
* @msarahan


## 3.0.29 (2017-11-10)

### Enhancements

* interpret ~= in pypi skeletons, map to compatible expressions  #2427
* add arm and ppc architectures to conda convert  #2472, #2474
* add indentation to index.json and `hash_input.json` for easier reading  #2476
* check arch in index.json for platforms other than linux, mac, win  #2478
* update cran skeletonizer for new compilers, add flags for updating, rather than replacing recipe.  #2481

### Bug fixes

* fix implicit pinning not taking effect in outputs, fix incorrect matching of hashed subpackages #2455
* exclude python from build requirements for purposes of hash computation.  This was causing recipes that used python as a build tool to build too many similar packages.  #2455
* Support `GIT_*` vars even when source folders are specified  #2477
* silence warnings about `.*` being added to vc deps  #2483
* fix non-finalized recipe being used for creating build env, resulting in too few variants in output  #2485

### Contributors

* @mandeep
* @mingwandroid
* @msarahan
* @stuarteberg


## 3.0.28 (2017-11-02)

### Enhancements

* Implement "subspace selection" - so you can reduce a larger central set of variants to some smaller subset.  Fixes --python=X.Y on windows, with its `zip_keys`.  #2466
* Update cpan skeleton  #2156
* Pass through VSXY0COMNTOOLS env vars, so they're available in activate scripts called from outputs  #2453
* Add additional index-related files for Anaconda Navigator to use  #2463
* Add back `CONDA_PY`, `CONDA_NPY`, and friends, for backcompat with conda-build-all  #2469

### Bug fixes

* Fix `build_folder` selection in dirty envs  #2445
* Fix an os.rename back to `copy_into` for cross-volume compatibility  #2451
* Clean up leftovers created by `utils.get_recipe_abspath`  #2459
* fix path globbing and filtering replacing prefix not at start of path, which broke file copying  #2468
* Don't recreate envs unnecessarily for recipes with no outputs section  #2470

### Contributors

* @jerowe
* @kalefranz
* @msarahan
* @neok-m4700
* @rendinam


## 3.0.27 (2017-10-17)

### Enhancements

* For windows error checks, assert that the errorlevel is 0, rather than GEQ 1.  Makes negative return codes fail builds.  #2442
* allow channels to be passed to the metapackage command.  Note that channels are not recorded to the package, and need to be passed at package install time, as well as metapackage creation time.  #2443

### Bug fixes

* Fix windows bits dictionary indexing incorrect type  #2441

### Contributors

* @msarahan


## 3.0.26 (2017-10-16)

### Enhancements

* Conda index now generates html index pages in addition to repodata.json  #2395
* make bash verbosity (-x flag) depend on setting of --debug flag  #2426
* pass test and build sections in any outputs through wholesale, rather than picking out individual fields from them.  #2429
* make conda-verify opt-in, rather than opt-out.  Use `--verify` cli argument or `verify` keyword to api.  #2436
* implement `requires_features` and `provides_features,` for compatibility with conda 4.4's new key-value feature  #2440

### Bug fixes

* fix `FEATURE_*` variables not working due to a type error  #2428
* fix misleading error when `download_url` present but empty  #2434
* check HTTP status code of PyPI pkg manifest request before decoding it, to improve error message  #2435
* fix 64-bit exe's showing up in 32-bit win packages due to not accounting for `host_arch` with script files  #2439
* fix hardlink-breaking bug where path was being copied instead of specific file.  Use better tempdir.  #2437

### Contributors

* @Bezier89
* @eklitzke
* @kalefranz
* @maddenp
* @msarahan
* @nehaljwani


## 3.0.25 (2017-10-06)

### Bug fixes

* unify usage of `conda_43`, learn to let the tests run.  #2424

### Contributors

* @msarahan


## 3.0.24 (2017-10-06)

### Enhancements

* add `get_used_loop_vars()` function to MetaData object, to show which loop variables are actually used by recipe  #2410
* Allow multiple file extensions for pypi skeletons, not just .tar.gz  #2412

### Bug fixes

* make build reqs equivalent to host when cross-compiling and no host section present (helps reduce need to modify python-only recipes)  #2406
* reduce logging output from filelock and conda  #2418 #2422
* Don't strip files in noarch: python when they are not known file types  #2420
* fix infinite loop when trying to build dep from found recipe, but that recipe is wrong version  #2423
* update perl used on appveyor for testing to 5.26

### Contributors

* @minrk
* @msarahan
* @nehaljwani


## 3.0.23 (2017-09-29)

### Bug fixes

* simplify handling of blank fields in CRAN metadata  #2393
* load `conda_build_config.yaml` from inside package when testing package separately from build process  #2399
* use sets instead of lists for field descriptions  #2403
* fix `noarch_python` packages getting pinned to a specific python version  #2409

### Contributors

* @Bezier89
* @CJ-Wright
* @jdblischak
* @msarahan


## 3.0.22 (2017-09-20)

### Bug fixes

* fix `filename_hashing` setting being ignored when using conda-build API  #2385
* fix relpath causing cross-drive issues on windows  #2386
* examine .a files when considering prefix replacement  #2390
* fix run/test deps check looking at `build_subdir` rather than `host_subdir` (broke cross compiling)  #2391

### Contributors

* @Bezier89
* @mingwandroid
* @msarahan


## 3.0.21 (2017-09-18)

### Bug fixes

* Fix strong `run_exports` from build being applied to host too late, running into conflicts (especially with VC features)  #2383
* crash properly when patching fails, rather than proceeding with build  #2384

### Contributors

* @msarahan


## 3.0.20 (2017-09-16)

### Bug fixes

* Never activate build or host env when building conda, so that symlinks or .bat files are never created.  #2381
* Apply "strong" `run_exports` from build section to host section, not just run section.  This is necessary for ensuring that features activated by packages in the build section are used to line up the host section also.  #2382

### Contributors

* @msarahan


## 3.0.19 (2017-09-15)

### Bug fixes

* write info/files for noarch.  Always sanity check info/files.  #2379
* fix `build_prefix` -> `host_prefix` in `write_pth`, fixes cross compiling python packages  #2380

### Contributors

* @Bezier89
* @msarahan


## 3.0.18 (2017-09-14)

### Bug fixes

* fix source hash not being verified  #2367
* fix several references to arch that should be `host_arch` to support cross compiling (win-32 on win-64, for example)  #2369, #2368
* replace recipe run requirements with contents of index.json's "depends" when testing packages  #2370
* update R and perl versions in `DEFAULT_VARIANTS`  #2373
* fix versioneer showing unknown version on windows due to --match argument  #2375
* add subdir to moved work folder dirname, to avoid clobbering when cross compiling  #2376

### Contributors

* @jjhelmus
* @mingwandroid
* @msarahan


## 3.0.17 (2017-09-12)

### Enhancements

* add `track_features` and features to output options, to allow per-output configuration of features  #2358

### Bug fixes

* Fix conda symlinks misbehaving when building conda package  #2359

### Contributors

* @msarahan


## 3.0.16 (2017-09-12)

### Enhancements

* allow env check to be bypassed when rendering (for c3i)  #2353
* provide mechanism for compiler version to be passed to compiler jinja2 function (match name with `_version`)  #2356

### Bug fixes

* use `host_subdir` instead of `build_subdir` when setting selectors  #2345
* remove downloaded files from source cache if they failed at any download step  #2349
* fix variants being merged across multiple builds due to modification of global  #2350
* disable pyldd disagrees warning output for now  #2352

### Contributors

* @mingwandroid
* @msarahan


## 3.0.15 (2017-09-04)

### Bug fixes

* fix relative paths for croot argument to CLI; test  #2335
* fix several issues with `zip_keys`  #2340
* fix output build number never applying  #2340
* fix `ensure_matching_hashes` for strong/weak `run_exports`  #2340
* fix indexing of channels, especially before testing packages  #2341
* copy wheels and unextractable files (.sh) into the workdir with their original, un-hashed filename, for simplicity in working with them.  #2343
* avoid attempting to overwrite existing files in the source cache  #2343
* avoid unsatisfiable requirement errors by adding .* to specs that lack .* or >/</>=/<=  #2344

### Contributors

* @gabm
* @msarahan


## 3.0.14 (2017-08-29)

### Bug fixes

* fix config.arch comparison being wrong data type  #2325
* fix `run_exports` handling with dict of lists  #2325
* pyldd: disambiguate java .class files from Mach-O fat files (same magic number)  #2328
* fix hash regex for downloaded files in `src_cache`  #2330
* fix `zip_keys` becoming a loop dimension when variants passed as object rather than loaded from file  #2333
* fix windows always warning about old compiler activation.  Now only warns if `{{ compiler() }}` is not used.  #2333
* Add `LD_RUN_PATH` back into Linux variables for now (may remove later, but will have deprecation cycle)  #2334

### Contributors

* @mingwandroid
* @msarahan
* @neok-m4700


## 3.0.13 (2017-08-26)

### Enhancements

* allow output build number and string to be set independently of top-level metadata  #2311
* add file hash to source cache filenames to avoid collisions  #2312
* add notion of "strong" or "weak" run exports.  Strong apply to run whether parent is in build or host.  Weak apply only if in host, or in build with no host present.  #2320

### Bug fixes

* Fix PY3K value changing from 0/1 to True/False.  Keep 0/1.
* make `work_dir` the cwd when running output bundling scripts.  It was the host prefix before now.
* start tmpdir prefixes when getting dependency versions with `_` so that conda can be one of the deps  #2321
* avoid setting empty compiler variables  #2322
* remove meaningless error with `glob_files` and `always_include_files` during env creation  #2323

### Contributors

* @msarahan


## 3.0.12 (2017-08-23)

### Enhancements

* update default `MACOSX_DEPLOYMENT_TARGET` to 10.9  #2293
* modernize `pin_depends` so that it works with conda render  #2294
* environment variable pass-throughs now respect variant (env var highest priority; variant, finally default)  #2310

### Bug fixes

* fix `run_exports` getting picked up transitively  #2298
* fix default compiler not having platform  #2300
* fix `CONDA_PY` formatting (should not have period).  `PY_VER` does have period.  #2304
* update index before testing a package, so that that package is conda-installable.  #2308
* update index after moving a package after test failure, so that the index is current.  #2308
* fix --output-folder not being respected by --output preview of output path  #2309

### Contributors

* @mingwandroid
* @msarahan


## 3.0.11 (2017-08-17)

### Enhancements

* set BUILD environment variable (triplet used by cross-compiling)  #2285
* respect condarc `cache_dir` setting for changing the source cache dir location #2278
* run selectors before returning meta.yaml extractions  #2284

### Bug fixes

* fix CRAN skeleton field truncation with ; characters  #2274
* Warn about overlapping files in subpackages within a recipe  #2275
* fix --override-channels not taking effect  #2277
* fix double-activation on Windows for cross compiling  #2280
* fix variant entry duplication with zipped keys  #2280
* fix folder hoisting when folder name in archive matches package name  #2281
* fix test env showing old cached packages when test env has actually been removed  #2282
* fix source code not being present for render when source necessary for render and more than one variant  #2283
* fix `binary_relocation` not allowing lists of files  #2288
* fix incorrect python (or none at all) being used for pyc compilation with python only in host reqs  #2290

### Contributors

* @dsludwig
* @jdblischak
* @jjhelmus
* @mingwandroid
* @msarahan


## 3.0.10 (2017-08-11)

### Enhancements

* Provide variant variables for use in selector expressions  #2258

### Bug fixes

* fix ordering of recipe elements in skeletonized pypi recipes  #2230
* Trim empty variant sections (due to selectors) prior to zipping keys  #2258
* Don't set blank env vars in build scripts  #2259
* Fix testing with recipe paths  #2262
* add newlines to test scripts  #2265
* Fix render command not considering provided channels  #2267
* fix `get_value` being hardcoded to only first entry  #2268
* fix setting target (target platform) in output section causing tarcheck validation error  #2271
* don't add setuptools to runtime dependencies in skeletonized pypi recipes (only build)  #2272

### Contributors

* @chaubold
* @msarahan
* @mwcraig
* @neok-m4700
* @ratstache
* @stuarteberg


## 3.0.9 (2017-08-02)

### Enhancements

* store test files specifed by `test/source_files` directly in packages.  This allows testing of packages that do not include recipes.  Recommendation: make subpackages for large data files.  #2232
* add new syntax to `get_value` for accessing list items, such as multiple sources  #2247
* add independently configurable source cache path (--cache-dir)  #2249
* add `PKG_HASH` env var, available in meta.yaml.  Use this to put the package hash where you want it in your custom build/string field in meta.yaml.  #2250

### Bug fixes

* Fix test python using incorrect metadata config object, and then using wrong prefix  #2226
* Allow testing multiple conda packages or folders at once with wildcard CLI arguments  #2227
* Fallback path for `ruamel_yaml` to ruamel.yaml  #2233
* raise exception when both build/script in meta.yaml and build script (build.sh/bld.bat) are provided  #2238
* Fix unclosed file handle when loading setup.py data #2242
* Fix 'path' source with multiple source  #2247
* improve compatibility with conda 4.4  #2248
* remove hash from manually-specified build/string fields.  Use new `PKG_HASH` env var instead.  #2250
* fix windows activate scripts getting included in windows packages  #2251
* ignore feature records in index for 'conda inspect'  #2253
* fix variant handling when variants affect the downloaded source (need re-extract, re-parse with new source at each step)  #2254

### Contributors

* @Bezier89
* @jjhelmus
* @kalefranz
* @msarahan
* @mandeep
* @mingwandroid
* @stuarteberg


## 3.0.8 (2017-07-20)

### Bug fixes

* Fix internal conda-build recipe to include missing setuptools and not use pip  #2221
* Try to avoid downloading anything until we absolutely need it for rendering or build  #2222
* Fix regexes that were leading to unsatisfiable dependencies, especially with perl  #2222
* Tweak internal recipe to include more git info; adjust regex accordingly for this practice #2223

### Contributors

@msarahan


## 3.0.7 (2017-07-20)

### Enhancements

* Rewrite skeleton pypi template; match conda-forge standard  #2205

### Bug fixes

* Remove entry point links to avoid write-through to root envs  #2209
* Properly insert variant versions for x.x in outputs (not just parent recipe)  #2210
* Relax version constraints for lua and R in default variant  #2213
* fix test of package directly using wrong config object  #2214
* Don't check test env satisfiability when --no-test is passed  #2218
* Iron out prefix when noarch as host env.  Was creating separate build/host envs inappropriately.  #2219
* Fix skipping finalization with finalize=False (for c3i speedup).  #2219
* Fix implicit variant looping - wasn't keeping track of "used variables" that are used implicitly.  #2219

### Contributors

* @mandeep
* @mwcraig
* @msarahan


## 3.0.6 (2017-07-14)

### Bug fixes

* Find git more intelligently, because `build_prefix` isn't always on PATH  #2196
* Fix up assorted RPM skeleton issues  #2196
* Fix and test "numpy x.x" recipes  #2198
* Fix and test --skip-existing.  Ensure that it also works with --croot.  #2200
* Fix and test "python x.x" recipes  #2201
* Fix inappropriate insertion of variant versions that led to conflicts (for example, numpy)  #2202

### Contributors

* @mingwandroid
* @msarahan


## 3.0.5 (2017-07-12)

### Bug fixes

* Fix --skip-existing (was not matching output-dir/croot locations correctly)  #2192
* Fix numpy x.x getting .* appended, resulting in unsatisfiable numpy  #2193

### Contributors

* @msarahan


## 3.0.4 (2017-07-11)

### Bug fixes

* Don't symlink conda when building conda (clobbers actual scripts)  #2167
* Fix pyldd following links  #2170
* Preserve mode bit on noarch python bin/Scripts files  #2171
* remove logging output showing up with --output option #2174
* Fix `CONDA_*` variables without .  #2176
* pass croot to extraction (file path length issue on win)  #2178
* fix uncorrect unpacking of tuples with --skip-existing  #2179
* Fix priority of setup.cfg over setup.py  #2180
* Remove overly aggressive removal of test prefix at end of test phase  #2182
* Fix upper bound increment to account for pre-release versions (alpha, beta, rc, etc.)  #2183

### Contributors

* @jjhelmus
* @mingwandroid
* @msarahan


## 3.0.3 (2017-07-07)

### Bug fixes

* fix loss of setup.cfg reading due to bad merge  #2163
* avoid error when attempting to sort list, and that list consists of dicts  #2163

### Contributors

* @msarahan


## 3.0.2 (2017-07-06)

### Enhancements

* Add `SSL_CERT_FILE` and `REQUESTS_CA_BUNDLE` env vars to passed-through variables  #2142
* Sort several package aspects for package reproducibility  #2143 #2149 #2154
* Add glob2 dependency to allow recursive globs in fields specifying filenames/paths  #2146
* Add conda skeleton rpm for creating recipes to repackage RPMs as conda packages  #2147
* Improve error messaging when git describe fails due to lack of annotated tags  #2158

### Bug fixes

* drop setup.py data that is not JSON serializable  #2141
* enhance support for recipes containing unicode or non-ascii characters in meta.yaml  #2148
* CRAN skeleton: allow some keys to be blank without throwing exceptions  #2153
* Fix incorrect arguments passed to pyldd (use keywords)  #2160
* fix incorrect distribution of variants when more than one variant key matched  #2161

### Contributors

* @aburgm
* @dougalsutherland
* @dhirschfeld
* @mandeep
* @MatthieuDartiailh
* @mingwandroid
* @msarahan
* @nehaljwani


## 2.1.17 (2017-06-30)

### Bug fixes

* Fix `disable_pip` removing packages even when they are explicit dependencies  #2129
* Remove any pyc files for entry point scripts that pip may have created #2134
* Ignore unserializable data when reading setup.py data  #2141

### Contributors

* @mandeep
* @msarahan


## 3.0.1 (2017-06-29)

This release includes all changes to the 2.1.x branch up to and including the 2.1.16 release.

### Enhancements

* Raise errors prior to build if any run or test deps are unsatisfiable  #2102
* Add skeleton function for RPM packages, to be used for things like Xorg  #2109
* Improve test coverage of workdir removal  #2111 #2112
* Match variants in `conda_build_config.yaml` with dep names (implicit jinja2 version spec) #2124

### Bug fixes

* fix reference to cc.subdir (it is just subdir)  #2015
* fix failing test when using `filename_hashing=False` (non-existent json file)  #2087
* fix dependencies specified to conda-convert not being added  #2090
* fix `disable_pip` removing packages even when they are explicit recipe deps #2129
* fix `pin_compatible` jinja2 function not respecting `lower_bound` as None correctly  #2138

### Contributors

* @jakirkham
* @mandeep
* @mingwandroid
* @msarahan
* @neok-m4700


## 2.1.16 (2017-06-23)

### Enhancements

* add CLI flag and condarc setting to disable --force for anaconda upload  #2047
* add `doc_source_url` to allowed fields in about section  #2048
* add a second pass for getting information from setup.py that is performed in
  the build environment, so that version-specific logic in setup.py should work.
  #2071
* add semicolons to print statements in test files to avoid errors with Perl.  #2012 #2089
* pass through more CPU-specific environment variables on windows  #2072
* pass through DISPLAY environment variable on Linux  #2098
* Improve `conda_interface` for better conda 4.4 and later 4.3.x releases  #2113
* skeleton pypi & lua: replace legacy noarch syntax with conda 4.3 style  #2120
* Restore --keep-old-work flag: works like --dirty to leave your build intermediaries, but does not reuse build folders like --dirty.  #2119
* Speed up and fix-up conda-convert  #2116 #2123

### Bug fixes

* fix test/imports with multiple language entries  #1967
* add missing six dependency in conda recipe for conda-build  #2063
* fix dependency addition when converting packages  #2091
* don't set `build_id` in test phase when --no-build-id is given #2100
* fix handling of string literals not being lists in test requirements from setup.py #2107

### Contributors

* @aburgm
* @AndresGuzman-Ballen
* @gqmelo
* @isuruf
* @kalefranz
* @mandeep
* @mingwandroid
* @msarahan
* @nehaljwani
* @nsoranzo
* @timsnyder
* @vinjana


## 3.0.0 (2017-05-23)

These release notes are an aggregation of all older pre-releases of conda-build
3.0.0. All changes from 2.1.15 and below have been incorporated.

### Breaking changes

* Support for post-build metadata (`__conda_version__.txt` and the like) has been removed.
* `pin_downstream` has been renamed to `run_exports`  #1911
* `exclude_from_build_hash` has been renamed to `ignore_version`  #1911
* Package signing and verification have been removed, to follow their removal from conda 4.3.  #1950

### Enhancements

* greatly extended Jinja2 templating capabilities  #1585
* record environment variables at top of build.sh, similar to what is done with bld.bat in win.  #1765
* use symlinks when copying to improve performance  #1867
* load setup.cfg data in `load_setup_py_data`  #1878
* calculate checksum and simplify cran skeleton  #1879
* Check that files are executable when finding them #1899
* use `rm_rf` to remove prefixes for more cleanliness and better speed  #1915
* add support for multiple sources in one meta.yaml  #1929
* allow `exact` keyword for `pin_compatible` jinja2 function  #1929
* allow selectors in variant `conda_build_config.yaml` files  #1937
* Avoid duplicate recreation of package index.  Speedup of 0-50%, depending on how extensively the recipe uses Jinja2 features.  #1954
* Allow per-subpackage specification of target subdir  #1961
* Add basic environment marker support to conda skeleton pypi  #1984
* allow about section for each subpackage  #1987
* add support for optional dependencies (conda 4.4)  #2001
* fix windows entry point exe's for unicode  #2045
* allow strings for `pin_run_as_build` values (e.g. x.x) rather than just dictionaries  #2042
* add meta.yaml entry to override `run_exports` pins  #2073
* add several condarc entries that can be used to control conda-build behavior  #2074
* add new pyldd tool and use it when ldd/otool fail   #2082
* Allow configuration of conda-build's loggers by logging configuration files.  Default to debug,info going to stdout, warn,error going to stderr.  #2078
* rename work dir before tests, rather than removing it, so that build intermediates can be inspected if tests fail.  #2078

### Bug fixes

* fix symlinks to folders in packaging  #1775
* fix detection of patch level when maxlevel=0  #1796
* properly copy permissions when extracting zip files  #1855
* Add more important Windows environment variables to the test environment  #1859, #1863
* remove build and test envs after each packaging step, to avoid unsatisfiable errors  #1866
* remove version pins from requirements added by `run_test` files (again avoid unsatisfiable errors)  #1866
* fix prefix file detection picking up too many files due to env recreation  #1866
* fix missing `r_bin,` make `run_test.r` scripts work  #1869
* fix R's binary path on Windows  #1870
* remove tab completion on CLI for compatibility with conda 4.4  #1795
* reduce scope of git try/except block so that `GIT_FULL_HASH` is available, even if tags are not  #1873
* Fix "compiler" jinja2 looping, so that it is respected in subpackages #1874
* Fix license family comparison - case matching  #1875
* Fix inspect linkages when multiple packages contain a library  #1884
* avoid unnecessary computation of hashing  #1888
* fix python imports not being run in test phase  #1896
* fix path omission in paths.json for noarch packages  #1895
* standardize entry point script template to match pip  #1908
* fix cleanup happening even when build fails  #1909
* fix bin/conda getting included in conda-build release tarballs  #1913
* fix mmap/file problems on virtualbox shared folders  #1914
* Correct rendering with --dirty flag if recipe name appears as substring of another's name  #1931
* don't set language env vars (PERL, R, LUA, PYTHON) when those packages are not installed  #1932
* exclude language env vars from variant being set  #1944
* Fix cleanup of folders in outer variant loop - was causing incorrect packages on 2nd variant in windows builds  #1950
* Remove variant functionality from `bdist_conda`.  Its split packaging approach is incompatible.  #1950
* Fix import of `_toposort` from conda, reroute through `conda_interface`  #1952
* Match folder substrings more intelligently, for finding previous builds with --dirty  #1953
* Fix type error with --skip-existing and some conda recipes (Conda-build's internal conda.recipe was one).  #1956
* Fix non-python packages creating python tests where they should not have  #1967
* Don't add python.app to run reqs multiple times  #1972
* Fix incorrect removal of cc in `conda_interface.py`  #1971
* Fix ORIGIN replacement - trailing slash was messing things up  #1982
* Pipe stdin when calling subprocess, in hopes of getting better ctrl-c handling with conda.  #1986
* Ensure that lock files are removed after build exit (or crash) to avoid permission errors on central installs  #2002
* Process line endings in bytes mode rather than text mode  #2035
* add a warning to `find_recipe` when multiple meta.yaml files are found (bioconda style)  #2040
* When applying patches, try 3 line ending options on the patch: 1. unchanged; 2. convert patch to unix line endings; 3. convert patch to windows line endings.  #2052
* fix empty `target_platform` variant entry leading to empty builds  #2056
* fix host activation for cross-capable recipes  #2060
* fix handling of circularity in subpackages #2065
* fix subdir handling for subdirs with more than one - character  #2066
* Install build and host deps when using cross-capable recipe on strictly native (not cross) build  #2070
* reduce verbosity of git error messages that people never care about  #2075
* hash only direct inputs of subpackages, rather than all files.  This limits creation of identical packages with similar hashes.  #2079

### Contributors

* @abretaud
* @evhub
* @groutr
* @jjhelmus
* @kalefranz
* @ma-ba
* @mandeep
* @mingwandroid
* @minrk
* @msarahan
* @pkgw
* @pwwang
* @rolando
* @stuarteberg
* @tatome
* @ukoethe
* @waltonseymour
* @wulmer


## 3.0.0rc1 (2017-05-23)

These release notes are an aggregation of all older pre-releases of conda-build
3.0.0, plus changes since 3.0.0rc0. All changes from 2.1.15 and below have been
incorporated.

### Breaking changes

* Support for post-build metadata (`__conda_version__.txt` and the like) has been removed.
* `pin_downstream` has been renamed to `run_exports`  #1911
* `exclude_from_build_hash` has been renamed to `ignore_version`  #1911
* Package signing and verification have been removed, to follow their removal from conda 4.3.  #1950

### Enhancements

* greatly extended Jinja2 templating capabilities  #1585
* record environment variables at top of build.sh, similar to what is done with bld.bat in win.  #1765
* use symlinks when copying to improve performance  #1867
* load setup.cfg data in `load_setup_py_data`  #1878
* calculate checksum and simplify cran skeleton  #1879
* Check that files are executable when finding them #1899
* use `rm_rf` to remove prefixes for more cleanliness and better speed  #1915
* add support for multiple sources in one meta.yaml  #1929
* allow `exact` keyword for `pin_compatible` jinja2 function  #1929
* allow selectors in variant `conda_build_config.yaml` files  #1937
* Avoid duplicate recreation of package index.  Speedup of 0-50%, depending on how extensively the recipe uses Jinja2 features.  #1954
* Allow per-subpackage specification of target subdir  #1961
* Add basic environment marker support to conda skeleton pypi  #1984
* allow about section for each subpackage  #1987
* add support for optional dependencies (conda 4.4)  #2001
* fix windows entry point exe's for unicode  #2045
* allow strings for `pin_run_as_build` values (e.g. x.x) rather than just dictionaries  #2042

### Bug fixes

* fix symlinks to folders in packaging  #1775
* fix detection of patch level when maxlevel=0  #1796
* properly copy permissions when extracting zip files  #1855
* Add more important Windows environment variables to the test environment  #1859, #1863
* remove build and test envs after each packaging step, to avoid unsatisfiable errors  #1866
* remove version pins from requirements added by `run_test` files (again avoid unsatisfiable errors)  #1866
* fix prefix file detection picking up too many files due to env recreation  #1866
* fix missing `r_bin,` make `run_test.r` scripts work  #1869
* fix R's binary path on Windows  #1870
* remove tab completion on CLI for compatibility with conda 4.4  #1795
* reduce scope of git try/except block so that `GIT_FULL_HASH` is available, even if tags are not  #1873
* Fix "compiler" jinja2 looping, so that it is respected in subpackages #1874
* Fix license family comparison - case matching  #1875
* Fix inspect linkages when multiple packages contain a library  #1884
* avoid unnecessary computation of hashing  #1888
* fix python imports not being run in test phase  #1896
* fix path omission in paths.json for noarch packages  #1895
* standardize entry point script template to match pip  #1908
* fix cleanup happening even when build fails  #1909
* fix bin/conda getting included in conda-build release tarballs  #1913
* fix mmap/file problems on virtualbox shared folders  #1914
* Correct rendering with --dirty flag if recipe name appears as substring of another's name  #1931
* don't set language env vars (PERL, R, LUA, PYTHON) when those packages are not installed  #1932
* exclude language env vars from variant being set  #1944
* Fix cleanup of folders in outer variant loop - was causing incorrect packages on 2nd variant in windows builds  #1950
* Remove variant functionality from `bdist_conda`.  Its split packaging approach is incompatible.  #1950
* Fix import of `_toposort` from conda, reroute through `conda_interface`  #1952
* Match folder substrings more intelligently, for finding previous builds with --dirty  #1953
* Fix type error with --skip-existing and some conda recipes (Conda-build's internal conda.recipe was one).  #1956
* Fix non-python packages creating python tests where they should not have  #1967
* Don't add python.app to run reqs multiple times  #1972
* Fix incorrect removal of cc in `conda_interface.py`  #1971
* Fix ORIGIN replacement - trailing slash was messing things up  #1982
* Pipe stdin when calling subprocess, in hopes of getting better ctrl-c handling with conda.  #1986
* Ensure that lock files are removed after build exit (or crash) to avoid permission errors on central installs  #2002
* Process line endings in bytes mode rather than text mode  #2035
* add a warning to `find_recipe` when multiple meta.yaml files are found (bioconda style)  #2040
* When applying patches, try 3 line ending options on the patch: 1. unchanged; 2. convert patch to unix line endings; 3. convert patch to windows line endings.  #2052
* fix empty `target_platform` variant entry leading to empty builds  #2056

### Contributors

* @abretaud
* @evhub
* @groutr
* @jjhelmus
* @kalefranz
* @ma-ba
* @mandeep
* @mingwandroid
* @minrk
* @msarahan
* @pkgw
* @pwwang
* @rolando
* @stuarteberg
* @tatome
* @ukoethe
* @wulmer


## 3.0.0rc0 (2017-05-16)

These release notes are an aggregation of all older pre-releases of conda-build 3.0.0, plus changes since 3.0.0beta1.  All changes from 2.1.13 and below have been incorporated.

### Breaking changes

* Support for post-build metadata (`__conda_version__.txt` and the like) has been removed.
* `pin_downstream` has been renamed to `run_exports`  #1911
* `exclude_from_build_hash` has been renamed to `ignore_version`  #1911
* Package signing and verification have been removed, to follow their removal from conda 4.3.  #1950

### Enhancements

* greatly extended Jinja2 templating capabilities  #1585
* record environment variables at top of build.sh, similar to what is done with bld.bat in win.  #1765
* use symlinks when copying to improve performance  #1867
* load setup.cfg data in `load_setup_py_data`  #1878
* calculate checksum and simplify cran skeleton  #1879
* Check that files are executable when finding them #1899
* use `rm_rf` to remove prefixes for more cleanliness and better speed  #1915
* add support for multiple sources in one meta.yaml  #1929
* allow `exact` keyword for `pin_compatible` jinja2 function  #1929
* allow selectors in variant `conda_build_config.yaml` files  #1937
* Avoid duplicate recreation of package index.  Speedup of 0-50%, depending on how extensively the recipe uses Jinja2 features.  #1954
* Allow per-subpackage specification of target subdir  #1961
* Add basic environment marker support to conda skeleton pypi  #1984
* allow about section for each subpackage  #1987
* add support for optional dependencies (conda 4.4)  #2001

### Bug fixes

* fix symlinks to folders in packaging  #1775
* fix detection of patch level when maxlevel=0  #1796
* properly copy permissions when extracting zip files  #1855
* Add more important Windows environment variables to the test environment  #1859, #1863
* remove build and test envs after each packaging step, to avoid unsatisfiable errors  #1866
* remove version pins from requirements added by `run_test` files (again avoid unsatisfiable errors)  #1866
* fix prefix file detection picking up too many files due to env recreation  #1866
* fix missing `r_bin`, make `run_test.r` scripts work  #1869
* fix R's binary path on Windows  #1870
* remove tab completion on CLI for compatibility with conda 4.4  #1795
* reduce scope of git try/except block so that `GIT_FULL_HASH` is available, even if tags are not  #1873
* Fix "compiler" jinja2 looping, so that it is respected in subpackages #1874
* Fix license family comparison - case matching  #1875
* Fix inspect linkages when multiple packages contain a library  #1884
* avoid unnecessary computation of hashing  #1888
* fix python imports not being run in test phase  #1896
* fix path omission in paths.json for noarch packages  #1895
* standardize entry point script template to match pip  #1908
* fix cleanup happening even when build fails  #1909
* fix bin/conda getting included in conda-build release tarballs  #1913
* fix mmap/file problems on virtualbox shared folders  #1914
* Correct rendering with --dirty flag if recipe name appears as substring of another's name  #1931
* don't set language env vars (PERL, R, LUA, PYTHON) when those packages are not installed  #1932
* exclude language env vars from variant being set  #1944
* Fix cleanup of folders in outer variant loop - was causing incorrect packages on 2nd variant in windows builds  #1950
* Remove variant functionality from `bdist_conda`.  Its split packaging approach is incompatible.  #1950
* Fix import of `_toposort` from conda, reroute through `conda_interface`  #1952
* Match folder substrings more intelligently, for finding previous builds with --dirty  #1953
* Fix type error with --skip-existing and some conda recipes (Conda-build's internal conda.recipe was one).  #1956
* Fix non-python packages creating python tests where they should not have  #1967
* Don't add python.app to run reqs multiple times  #1972
* Fix incorrect removal of cc in `conda_interface.py`  #1971
* Fix ORIGIN replacement - trailing slash was messing things up  #1982
* Pipe stdin when calling subprocess, in hopes of getting better ctrl-c handling with conda.  #1986
* Ensure that lock files are removed after build exit (or crash) to avoid permission errors on central installs  #2002

### Contributors

* @abretaud
* @evhub
* @groutr
* @jjhelmus
* @kalefranz
* @ma-ba
* @mingwandroid
* @msarahan
* @pkgw
* @pwwang
* @stuarteberg
* @tatome
* @ukoethe
* @wulmer


## 2.1.13 (2017-05-10)

### Bug fixes

* fix missing argument to `get_site_packages` function; add test coverage  #2009
* pin codecov on appveyor to 2.0.5 for now  #2009
* fix lock removal (just don't create locks for temporary directories)  #2009

### Contributors

* @msarahan


## 2.1.12 (2017-05-09)

### Bug fixes

* Clean up lock files for temporary directories also

### Contributors

* @msarahan


## 2.1.11 (2017-05-09)

### Enhancements

* add libgcc to build dependencies for R skeleton recipes that require compilation  $1969

### Bug fixes

* fix entry points, test commands, test imports from top-level recipe from applying to subpackages  #1933
* fix `preferred_env` in index.json  #1941
* do not add python.app to `run_reqs` multiple times  #1981
* Fix $ORIGIN replacement from extra trailing slash  #1981
* Remove error when `_license` package exists in folder where `conda index` is called  #2005
* fix `STDLIB_DIR` so that it is always defined (based on python version in configuration)  #2006
* Clean up lock files after builds complete or fail to avoid permission errors  #2007

### Contributors

* @johanneskoester
* @kalefranz
* @mingwandroid
* @msarahan


## 3.0.0beta1 (2017-04-25)

### Breaking changes

* Package signing and verification have been removed, to follow their removal from conda 4.3.  #1950

### Enhancements

* Avoid duplicate recreation of package index.  Speedup of 0-50%, depending on how extensively the recipe uses Jinja2 features.  #1954

### Bug fixes

* Fix cleanup of folders in outer variant loop - was causing incorrect packages on 2nd variant in windows builds  #1950
* Remove variant functionality from `bdist_conda`.  Its split packaging approach is incompatible.  #1950
* Fix import of `_toposort` from conda, reroute through `conda_interface`  #1952
* Match folder substrings more intelligently, for finding previous builds with --dirty  #1953
* Fix type error with --skip-existing and some conda recipes (Conda-build's internal conda.recipe was one).  #1956

### Contributors

* @kalefranz
* @msarahan
* @rendinam


## 3.0.0beta0 (2017-04-20)

### Breaking changes

* `pin_downstream` has been renamed to `run_exports`  #1911
* `exclude_from_build_hash` has been renamed to `ignore_version`  #1911

### Enhancements

* use `rm_rf` to remove prefixes for more cleanliness and better speed  #1915
* add support for multiple sources in one meta.yaml  #1929
* allow `exact` keyword for `pin_compatible` jinja2 function  #1929
* allow selectors in variant `conda_build_config.yaml` files  #1937

### Bug fixes

* fix mmap/file problems on virtualbox shared folders  #1914
* Correct rendering with --dirty flag if recipe name appears as substring of another's name  #1931
* don't set language env vars (PERL, R, LUA, PYTHON) when those packages are not installed  #1932
* exclude language env vars from variant being set  #1944

### Contributors

* @mingwandroid
* @msarahan
* @rendinam


## 2.1.10 (2017-04-17)

### Enhancements

* Inspect linkages will now warn when multiple packages contain the same library  #1884, #1921

### Bug fixes

* Fix bin/conda getting included in packages that also had entry point scripts or binaries starting with 'conda'  #1923
* Fix empty `create_env`, for compatibility with conda 4.4  #1924
* Adapt to Conda's new MatchSpec implementation  #1927
* Fix unbound local variables when --no-locking option used.  #1928
* Don't set language env vars (PERL, R, LUA, etc.) when packages for those languages are not installed  #1930

### Contributors

* @jjhelmus
* @kalefranz
* @msarahan


## 3.0.0alpha2 (2017-04-05)

### Breaking changes

* Support for post-build metadata (`__conda_version__.txt` and the like) has been removed.

### Enhancements

* use symlinks when copying to improve performance  #1867
* load setup.cfg data in `load_setup_py_data`  #1878
* calculate checksum and simplify cran skeleton  #1879

### Bug fixes

* fix R's binary path on Windows  #1870
* remove tab completion on CLI for compatibility with conda 4.4  #1795
* reduce scope of git try/except block so that `GIT_FULL_HASH` is available, even if tags are not  #1873
* Fix "compiler" jinja2 looping, so that it is respected in subpackages #1874
* Fix license family comparison - case matching  #1875
* Fix inspect linkages when multiple packages contain a library  #1884
* avoid unnecessary computation of hashing  #1888
* fix python imports not being run in test phase  #1896
* fix path omission in paths.json for noarch packages  #1895

### Contributors

* @abretaud
* @groutr
* @jjhelmus
* @kalefranz
* @ma-ba
* @mingwandroid
* @msarahan


## 2.1.9 (2017-04-04)

### Enhancements

* calculate checksum and simplify cran skeleton  #1879
* backport usage of symlinks for speed from master branch  #1881

### Bug fixes

* fix import tests not being run, test this functionality  #1897

### Contributors

* @isuruf
* @jjhelmus
* @johanneskoester
* @msarahan


## 2.1.8 (2017-03-24)

### Enhancements

* use symlinks when copying files from files sources to improve performance  #1867

### Bug fixes

* reset build folder for each built package (fixes building multiple recipes in one command)  #1842
* wrap copy of `test/source_files` so that errors don't prevent a successful build  #1843
* Restore permissions when extracting from zipfiles  #1855
* pass through several Windows-specific environment variables  #1859, #1862
* python 2 os.environ string type compatibility fix  #1861
* fix indentation breaking perl package testing  #1872
* reduce scope of git try/except block so that `GIT_FULL_HASH` is available even if tags are not.  #1873
* fix license family comparison, especially for public-domain  #1875
* Remove python header being added to all `run_test.*` files  #1876

### Contributors

* @abretaud
* @jjhelmus
* @mingwandroid
* @msarahan
* @stuertz
* @wulmer


## 3.0.0alpha1 (2017-03-23)

### Bug fixes

* remove build and test envs after each packaging step, to avoid unsatisfiable errors  #1866
* remove version pins from requirements added by `run_test` files (again avoid unsatisfiable errors)  #1866
* fix prefix file detection picking up too many files due to env recreation  #1866
* fix missing `r_bin`, make `run_test.r` scripts work  #1869

### Contributors

* @msarahan


## 3.0.0alpha0 (2017-03-22)

This is a complete revolution in the dynamic rendering capabilities of conda-build.  More information is in the docs PR at https://github.com/conda/conda-docs/pull/414.  There will be a blog post soon, perhaps coupled with a screencast.

### Enhancements

* greatly extended Jinja2 templating capabilities  #1585
* record environment variables at top of build.sh, similar to what is done with bld.bat in win.  #1765

### Bug fixes

* fix symlinks to folders in packaging  #1775
* fix detection of patch level when maxlevel=0  #1796
* properly copy permissions when extracting zip files  #1855
* Add more important Windows environment variables to the test environment  #1859, #1863

### Contributors

* @jjhelmus
* @kalefranz
* @mingwandroid
* @msarahan
* @pkgw
* @stuarteberg
* @ukoethe
* @wulmer


## 2.1.7 (2017-03-14)

### Enhancements

* pass WINDIR env var through on Windows  #1837
* make long test prefix an option (default disabled)  #1838

### Bug fixes

* monkeypatch `ensure_use_local` to avoid conda-build import clobbering conda CLI arguments  #1834
* Fix context `conda_build` attr error with older conda  #1813
* Fix legacy noarch shebang replacement code to account for long prefix paths #1813
* properly initialize 'system' key in linkage inspecting #1839
* backport try mmap from master #1764
* fix wheel output not respecting --output-folder CLI argument #1838
* catch csv dialect sniffing error, try to fallback to to `excel_tab`.  Might work? #1840

### Contributors

* @kalefranz
* @mcs07
* @msarahan


## 2.1.6 (2017-03-08)

### Enhancements

* tests on linux/mac now use 255-character prefix when creating test environment  #1799
* allow test/imports for R and lua packages #1806

### Bug fixes

* Fix case comparison in `license_family.py`  #1761
* Fix symlinked folders not being included in packages  #1770
* Fix extraction of tarballs containing unicode filenames  #1779, #1804
* fix unicode in delimiter for noarch `py_file_map`  #1789
* Clean up conda interface #1791
* Confine conda-build 2.1.x to conda >4.1,<=4.3  #1792
* fix detection of patch strip level when maxlevel = 0  #1796
* fix attribute error in exception handling for missing dependencies  #1800
* fix osx `python_app` test for python 3.6  #1801
* don't die when unicode found in patch files  #1802
* clarify error messaging when git is not found  #1803
* fix shebangs in entry point scripts using legacy `noarch_python` #1806
* fix test environment variables being set to build prefix values #1806
* fix inspect linkages breaking due to conda index keys changing to different objects in conda 4.3  #1810

### Contributors

* @gbrener
* @kalefranz
* @msarahan
* @pkgw
* @stuertz


## 2.1.5 (2017-02-20)

### Enhancements

* don't crash on unknown selector.  Warn, but evaluate as False.  #1753
* allow default conda packaging behavior for split package whose name matches top-level name, but lacks both `files` and `script` entry.  #1758

### Bug fixes

* unify license family text with Anaconda-Verify  #1744
* apply post-processing to each split package, not just to post-build prefix files.  #1747
* provide fallback lock directory in user's home folder.  Allows central installs.  #1749
* fix quoting for test paths.  Allows croot with spaces.  #1750
* fix pypi skeleton recursion #1754
* fix assertion error about leading period when Jinja2 variables have default values  #1757
* set default twine target to pypitest to avoid accidental uploads  #1758

### Contributors

* @gabm
* @msarahan


## 2.1.4 (2017-02-07)

### Enhancements

* Allow relative paths for --croot option #1736

### Bug fixes

* Rename `package_metadata.json` file to link.json to more accurately reflect contents #1720
* Fix converted packages from unix to Windows having broken entry points #1721
* Fix an infinite loop when creating the test environment failed #1739
* Fix conda 4.3 incompatibility with --pin-depends option #1740

### Contributors

* @gabm
* @kalefranze
* @msarahan


## 2.1.3 (2017-01-31)

### Enhancements

* Add --extra-specs to conda skeleton.  Use when a package needs to be available in the temporary env that parses setup.py to make the skeleton.  #1697
* Allow wheels as a source format  #1700
* Allow github urls as CRAN skeleton sources  #1710

### Bug fixes

* exclude package/name field from `uses_vcs_in_{meta,build}` checks #1696
* Fix conda convert wrt info/paths.json (for conda 4.3 compatibility)  #1701
* update cpan skeleton to use newer API url, fix conda exception handling #1704
* update R default version to 3.3.2  #1707
* fix attribute error on exception handling (better fix on the way)  #1709
* fix `bundle_conda` removing project files when conda recipe was in the source tree, and utilized relative paths  #1715
* fix glob trying to interpret filenames that look like glob patterns  #1717

### Contributors

* @ElliotJH
* @jerowe
* @kalefranz
* @mingwandroid
* @minrk
* @msarahan
* @rainwoodman


## 2.1.2 (2017-01-20)

### Enhancements

* iron out compatibility with conda 4.3 #1667
* pytest improvements for a cleaner CI experience #1686 #1687

### Bug fixes

* Avoid trailing semicolon in `MSYS2_ARG_CONV_EXCL` variable setting #1651
* filter .git directories more strictly (keep x.git folders, not .git) #1657
* fix 404's killing CPAN skeleton with newer conda versions #1667
* use pythonw to run tests on OSX when `osx_is_app` is defined in meta.yaml #1669
* ignore obnoxious `.DS_Store` files when packaging  #1670
* fix --source argument to download source specified in meta.yaml #1671
* fix slashes in file prefix replacement on Windows #1680
* fix multiple source url fallbacks (handle CondaHTTPErrors) #1683
* fix bizarre encoding errors on Windows with projects that embed binary in setup files #1685
* fix CPAN JSON file encoding issue on windows #1688
* revise retry when conda is missing files from a package #1690

### Contributors

* @dfroger
* @kalefranz
* @mingwandroid
* @msarahan
* @nicoddemus
* @pkgw


## 2.1.1 (2017-01-12)

### Bug fixes

* Fix package conversion consistency, wrt entry points #1609
* Fix about.json contents regarding development versions of conda/conda-build #1625
* Fix Appveyor for testing against source branches of conda #1628
* Raise exception when SRC_DIR is used in tests, but meta.yaml has no `test/source_files` entry.  `SRC_DIR` points at test work folder at test time, for minimal needed changes to recipes - just add `test/source_files` entry with desired files.  #1630
* Fix features list not allowed to be None in `bdist_conda` #1636
* Fix undefined reference to locks in `copy_into` #1637
* Fix version comparison in cpan skeleton #1638
* Add dependency on beautifulsoup4 and chardet to better support strangely encoded text files.  #1641
* Fix not-yet-fully-rendered versions starting with . from raising exception #1644
* Consolidate `_check_call` and `check_call_env` in utils.  Fix coercion to string that was missing in latter.  #1645

### Contributors

* @gomyhr
* @jakirkham
* @kalefranz
* @msarahan


## 2.1.0 (2017-01-02)

(includes changes since 2.0.12, including those already listed under 2.1.0beta1)

### Enhancements

* Consolidate package metadata from extra.json and noarch.json into `package_metadata.json` #1535 #1539
* finalize paths.json, (formerly files.json), which supersedes the older separate files for tracking file data #1535
* Support output of multiple packages from one recipe #1576
* Support output of wheels #1576
* Add `--prefix-length` to conda-build.  This allows one to set the prefix length manually.  It should be used sparingly, preferring creation of a temporary folder on non-encrypted locations, and setting `--croot` to that temporary folder.  #1579
* Add `--no-prefix-length-fallback` option to conda-build, to fail builds that encounter short prefixes, rather than falling back to the short prefix #1579
* Change CRAN-skeleton to follow conda-forge style #1596
* Allow relative paths to files in source/url field #1614

### Bug fixes

* Rework locks to be more robust #1540
* Call `make_hardlink_copy` on Windows to prevent conda failures #1575
* Delete the work folder before running the test suite.  Exposes faulty links to source files more easily.  #1581
* Add support for Python 3.6 in selector expressions #1592
* Don't try to compile pyc files when python is not installed in the build env #1593
* Fix a function call leading to corrupted meta.yaml output #1589
* Fix logger to be package-local.  Fixes logger output not showing up.  #1583
* Disallow leading periods in package version  #1594
* Fix reference to undefined `need_source_download` #1595
* Disallow - in feature names, to avoid conflicts with conda's handling of package names #1600
* Remove help text about passing multiple --python options or "all" - this has been broken for some time.  Replacement coming in 3.0.0.  #1610
* Fix clobbering of `no_link` variable.  #1611
* Fix index when --output-folder is specified #1613
* Fix `python_d.exe` incompatibility with conda 4.3 #1615

### Contributors

* @asmeurer
* @hajs
* @johanneskoester
* @kalefranz
* @mingwandroid
* @msarahan
* @mwiebe
* @soapy1


## 2.1.0beta1 (2016-12-20)

### Enhancements

* Consolidate package metadata from extra.json and noarch.json into `package_metadata.json` #1535 #1539
* finalize paths.json, (formerly files.json), which supersedes the older separate files for tracking file data #1535
* Support output of multiple packages from one recipe #1576
* Support output of wheels #1576
* Add `--prefix-length` to conda-build.  This allows one to set the prefix length manually.  It should be used sparingly, preferring creation of a temporary folder on non-encrypted locations, and setting `--croot` to that temporary folder.  #1579
* Add `--no-prefix-length-fallback` option to conda-build, to fail builds that encounter short prefixes, rather than falling back to the short prefix #1579
* Change CRAN-skeleton to follow conda-forge style #1596

### Bug fixes

* Rework locks to be more robust #1540
* Call `make_hardlink_copy` on Windows to prevent conda failures #1575
* Delete the work folder before running the test suite.  Exposes faulty links to source files more easily.  #1581
* Add support for Python 3.6 in selector expressions #1592
* Don't try to compile pyc files when python is not installed in the build env #1593
* Fix a function call leading to corrupted meta.yaml output #1589
* Fix logger to be package-local.  Fixes logger output not showing up.  #1583
* Disallow leading periods in package version  #1594
* Fix reference to undefined `need_source_download` #1595
* Disallow - in feature names, to avoid conflicts with conda's handling of package names #1600

### Contributors

* @asmeurer
* @hajs
* @johanneskoester
* @kalefranz
* @mingwandroid
* @msarahan
* @mwiebe
* @soapy1


## 2.0.12 (2016-12-12)

### Enhancements

* Whitelist, rather than hardcode, `MACOSX_DEPLOYMENT_TARGET.`  Default to 10.7  #1561
* Allow local relative paths to be passed as channel arguments #1565

### Bug fixes

* Keep `CONDA_PATH_BACKUP` as allowed variable in build/test env activation.  Necessary to make deactivation work correctly.  #1560
* Define nomkl selector when `FEATURE_NOMKL` environment variable is not set #1562
* Move test removal of packaged recipe until after test completes #1563
* Allow `source_files` in recognized meta.yaml fields #1572

### Contributors

* @jakirkham
* @mingwandroid
* @msarahan


## 2.0.11 (2016-11-28)

### Enhancements

* Further develop and update files.json #1501
* New command line option: `--output-folder` allows moving artifact after build (to facilitate CI) #1538
* support globs in `ignore_prefix_files`, `has_prefix_files`, `always_include_files`, `binary_has_prefix_files` #1554
* decouple `ignore_prefix_files` from `binary_relocation`; make `binary_relocation` also accept a list of files or globs #1555

### Bug fixes

* rename `short_path` key in files.json to `path` #1501
* allow `!` in package version (used in epoch) #1542
* don't compute SHA256 for folders #1544
* fix merge check for dst starting with src #1546
* use normpath when comparing utils.relative (fixes git clone issue) #1547
* disallow softlinks for conda (>=v.4.2) in conda-build created environments #1548

### Contributors

* @mingwandroid
* @msarahan
* @soapy1


## 2.0.10 (2016-11-14)

### Bug fixes

* Fix backwards incompatibility with conda 4.1 #1528

### Contributors

* @msarahan


## 2.0.9 (2016-11-11)

### Enhancements

* break build string construction out into standalone function for external usage (Concourse CI project) #1513
* add conda-verify support.  Defaults to enabled.  Adds conda-verify as runtime requirement.
*

### Bug fixes

* handle creation of intermediate folders when filenames provided as `build/source_files` arguments #1511
* Fix passing of version argument to pypi skeleton arguments #1516
* break symlinks and copy files if symlinks point to executable outside of same path (fix RPATH misbehavior on linux/mac, because ld.so follows symlinks) #1521
* specify conda executable name more specifically when getting about.json info.  It was not being found in some cases without the file extension.  #1525

### Contributors

* @jhprinz
* @msarahan
* @soapy1


## 2.0.8 (2016-11-03)

### Enhancements

* Support otool -h changes in MacOS 10.12 #1479
* Fix lists of empty strings created by `ensure_list` (patches failing due to empty patch list) #1493
* Improved logic to guess the appropriate `license_family` to add to package's index. This improves filtering. #1495 #1503
* Logic for the `license_family` is now shared between open-source conda-build, and proprietary cas-mirror packages. #1495 #1503

### Bug fixes

* Centralize locks in memory to avoid lock timeouts within a single process #1496
* fix overly broad regex in detecting whether a recipe uses version control systems #1498
* clarify error message when extracting egg fails due to overlapping file names #1500
* fix regression where subdir was not respecting non-x86 arch (values other than 32 or 64) #1506

### Contributors

* @caseyclements
* @minrk
* @msarahan


## 2.0.7 (2016-10-24)

### Enhancements

* populate `SHLIB_EXT` environment variable.  For example, .so, .dll, .dylib file extensions use this for their native ending.  #1478

### Bug fixes

* fix metapackage not going through api, thus not showing output file path.  #1470
* restore script exe creation on Windows.  These are for standalone scripts installed by distutils or setuptools in setup.py.  #1471
* fix noarch value propagation from meta.yaml to config.  Was causing noarch to not be respected in some cases.  #1472
* fix calls to subprocess not converting unicode to str  #1473
* restore `detect_binary_files_with_prefix` behavior - in particular, respect it when false.  # 1477

### Contributors

* @jschueller
* @mingwandroid
* @msarahan


## 2.0.6 (2016-10-13)

### Bug fixes

* fix erroneous import that was only compatible with conda 4.2.x #1460

### Contributors

* @msarahan


## 2.0.5 (2016-10-13)

### Enhancements

* Add new jinja function for extracting information from files with regular expressions #1443

### Bug fixes

* Quote paths in activation of build and test envs #1448
* Fix source re-copy (leading to IOError) with test as a separate step #1452
* Call conda with an absolute path when gathering metadata for package about.json #1455
* Don't strictly require conda-env to be present for about.json data #1455
* Fix version argument to skeletons not being respected #1456
* Fix infinite recursion when missing dependency is either r or python #1458

### Contributors

* @bryanwweber
* @msarahan


## 2.0.4 (2016-10-07)

### Enhancements

* Add `build/skip_compile_pyc` meta.yaml option.  Use to skip compilation on pyc files listed therein.  #1169
* Add build environment metadata to about.json (conda, conda-build versions, channels, root pkgs) #1407
* Make subdir member of config a derived property, so that setting platform or bits is more direct #1427
* Use subprocess call to windows del function to clear .trash folder, rather than conda.  Big speedup. #1438

### Bug fixes

* fix regression regarding 'config' in pypi skeleton for recipes with entry points #1430
* don't load setup.py data when considering entry points (use only info from meta.yaml) #1431
* fall back to trying to copy files without attributes or metadata if those fail #1436
* Fix permissions on packaged files to be user and group writable, and other readable. #1437
* fix conda develop not respecting python version of target environment #1440

### Contributors

* @mingwandroid
* @msarahan


## 2.0.3 (2016-09-27)

### Enhancements

* add support for noarch: python #1366

### Bug fixes

* convert popen args to bytestrings if unicode #1413
* Fix perl file access error on win skeleton cpan #1414
* Catch patchelf failures in post #1418
* fix path walking in `get_ext_files` #1422

### Contributors

* @mingwandroid
* @msarahan
* @soapy1


## 2.0.2 (2016-09-27)

### Enhancements

* Consider all recipes when printing output paths with --output #1332
* Lay groundwork for noarch packages with different types allowed (not just `noarch_python`) #1334
* Improve setting RPATH on Linux - handle relative paths better #1336
* Add GPL as a license family #1340
* Skip fixing rpath for files listed in `ignore_prefix_files` #1345
* Uniformly use conda's `rm_rf` function, not `move_to_trash` #1355
* Add support for alternate PKGINFO files.  Adds pkginfo dependency.  #1353
* Add --croot argument to conda build CLI, to specify build root folder #1358
* Do not index pkgs folder #1381 #1388
* Assert that merge destination is not a subdir of source, to avoid recursion problems #1396
* add UUID to token upload test to avoid race condition that caused intermittent CI failure #1392
* Roll `source.get_dir` into `config.work_dir`, to avoid confusion.  #1400
* Improve locking in several places #1405 #1408

### Bug fixes

* Fix `guess_license_family` to have LGPL -> LGPL, not public domain #1336
* Restore standard behavior with `__pycache__` folder and pyc files #1333
* Fix `pyver_re` to not catch python-* packages #1342
* Fix erroneous file argument to logging call #1344
* Fix convert unix -> win  not creating entry point py scripts #1348
* Remove pytest timeout for tests.  It is responsible for intermittent CI test crashes.  #1351
* Fix retrieval of `CONDA_NPY` setting (only --numpy flag was being respected) #1356
* Fix --no-build-id argument to conda build that was note being respected #1359
* Fix handling of recipe folder specifications coming out blank or . #1360 #1391
* Handle conda 4.2 exceptions better for LinkErrors and PaddingErrors, better support OpenSSL custom prefix replacement #1362
* Fix indentation error leading to skip-existing not working #1364
* Fix skeletonize not passing arguments from CLI #1384 #1387 #1406
* Check if file exists before trying to use stat on it.  Might avoid mmap errors.  #1389
* Fix no include recipe option when input is metadata (as opposed to recipe file path) #1398
* Normalize slashes in examining files in tarfiles (always forward slashes) #1404

### Contributors

* @gabm
* @jakirkham
* @johanneskoester
* @mingwandroid
* @msarahan
* @mwcraig
* @soapy1
* @sooneecheah
* @yoavram


## 2.0.1 (2016-09-06)

### Enhancements

* Add `disable_pip` build option to disable conda's automatic add of pip/setuptools #1311
* Add numpy to pypi env creation if it is imported in setup.py #1289
* Improve compatibility with conda >=4.2 regarding prefixes that are too short #1323
* Delete .pyo files prior to compiling pyc files.  They are considered harmful.  #1328
* Add `conda build purge-all` command that cleans out built packages and build folders #1329

### Bug fixes

* Use `source.get_dir` instead of config.workdir for `source_files` (was one level too low) #1288
* Import setuptools in windows.py to apply vc9-finding monkeypatch #1290
* Fix convert not updating subdir in index.json #1297
* Update post-build deprecation warning to state 3.0 as release for removal #1298
* Create pkgs folder if it does not exist #1299
* Fix `warn_on_old_conda_build` to ignore non-final release versions (alpha/beta/rc) #1303 #1315
* Remove coercion of pycache folder into flat pyc files #1304
* Fix metadata retrieval in `bdist_conda` #1308
* Add supplemental removal of cached packages when conda does not fully remove them #1309
* Simplify updating the package index #1309
* Straighten out when metadata member config is used, relative to config argument #1311
* Catch prefix length errors with OpenSSL's custom prefix replacement program #1312
* Replace all colons with `_` in git mirror folders to avoid Windows path errors #1322
* Fix missing file contents in converted packages.  Test.  #1325

### Contributors

* jakirkham
* mingwandroid
* msarahan


## 2.0.0 (2016-08-29)

Notes here are a consolidation of all changes between 1.21.14 and 2.0.0.

### Enhancements

* Increase placeholder path to 255 bytes (affects only Linux/Mac. Packages need to be rebuilt to support longer embedded paths) #877
* Configuration is local, passed via config argument.  No more global config.  #953
* Created Python API in `conda_build/api.py` #953
* Separate build folders per-build to allow parallelism #953
* Add locking to allow safe parallelism #953
* Add build flag to turn off separate build folders (--no-build-id) #953
* Much greater test coverage across all modules #953
* Add `CONDA_BUILD_STATE` variable that reflects RENDER, BUILD, or TEST state of build #1232
* Add support for `HG_` variables in meta.yaml templates (for hg repos) #207 #1234
* Add `source_files` test argument in meta.yaml to copy files from source into test #1237
* add a numpy.distutils patch to jinja templating, so that fortran projects using numpy can also use jinja2 (thanks @bladwig1) #1252
* Ensure that the build environment is on PATH during all tooling and testing #1256
* Make failure due to pip requirements in meta.yaml clearer #1279
* Allow API to accept either paths to meta.yaml files or MetaData objects, for better compatibility #1281
* Implement tests to verify api stability #1283
* Add build/noarch to recipe metadata.  Use for truly platform independent packages - same folder in every install. #1285

### Bug fixes

* Fix error converting linux to win packages due to python version mismatch #481
* Fix infinite loop that occurred with circular dependencies being built #953
* Improve test data structures to allow profiling with pytest-profiling #953
* Fix version sorting in pypi skeleton generator #1238
* improve backwards compatibility* prefix build and test envs with `_`, so that conda can be installed in them #1242
* fix `bdist_conda`; add smoke test for it to Travis #1243
* fix windows entry points (duplicate bad logic) #1246
* fix inspect entry point in embedded conda.recipe #1251
* create build environment before looking for VCS in it.  #1253
* fix a deadlock with recursive environment creation on encountering packages with short prefixes #1257
* with conda commands #1259
* only compile pyc files if python is in the build prefix # 1261
* remove exception catch-all in build CLI, to show actual errors more #1262
* specify full paths to activate scripts to avoid PATH conflicts with virtualenv #1266
* clean up remnants of pipbuild #1267
* remove pyc files from any `source_files` arguments to test in meta.yaml (avoid `__file__` errors) #1272
* copy files and folders when breaking hardlinks (rather than renaming) to avoid cross-filesystem errors #1273
* add Scripts folder to prepended binary paths searched on Windows #1276
* update `MACOSX_DEPLOYMENT_TARGET` hard-coded value to 10.7 (better fix soon) #1278
* disallow backslashes in meta.yaml fields describing paths (e.g. `always_include_files`) #1280
* prevent `GIT_*` env vars from containing newlines #1282
* restore prefix-lengths inspect command (lost in merging) #1283

### Restructuring

* CLI scripts have been gutted and moved to `conda_build/cli`.  Content from them is in
  `conda_build`, in scripts without `main_` prefix.  #953
* Skeleton generators have been broken out of `main_skeleton.py`, and consolidated into
  `conda_build/skeletons`.  The contents of this folder are examined at runtime for pluggability.  #953

### Contributors

* @bladwig1
* @brentp
* @heather999
* @jakirkham
* @mingwandroid
* @msarahan
* @melund
* @pigmej

### Testers

* @dsludwig
* @ericdill
* @jakirkham
* @mingwandroid
* @pitrou
* @srossross


## 2.0.0beta4 (2016-08-26)

### Bug fixes

* improve backwards compatibility with conda commands #1259
* only compile pyc files if python is in the build prefix # 1261
* remove exception catch-all in build CLI, to show actual errors more #1262
* specify full paths to activate scripts to avoid PATH conflicts with virtualenv #1266
* clean up remnants of pipbuild #1267
* remove pyc files from any `source_files` arguments to test in meta.yaml (avoid `__file__` errors) #1272
* copy files and folders when breaking hardlinks (rather than renaming) to avoid cross-filesystem errors #1273
* add Scripts folder to prepended binary paths searched on Windows #1276
* update `MACOSX_DEPLOYMENT_TARGET` hard-coded value to 10.7 (better fix soon) #1278

### Contributors

* @dsludwig (testing)
* @ericdill (testing)
* @jakirkham (testing)
* @mingwandroid (testing)
* @msarahan
* @pitrou (testing)
* @srossross (testing)


## 2.0.0beta3 (2016-08-23)

### Enhancements

* add a numpy.distutils patch to jinja templating, so that fortran projects using numpy can also use jinja2 (thanks @bladwig1) #1252

### Bug fixes

* prefix build and test envs with `_`, so that conda can be installed in them #1242
* fix `bdist_conda`; add smoke test for it to Travis #1243
* fix windows entry points (duplicate bad logic) #1246
* fix inspect entry point in embedded conda.recipe #1251
* create build environment before looking for VCS in it.  #1253
* fix a deadlock with recursive environment creation on encountering packages with short prefixes #1257

### Contributors

* @bladwig1
* @ericdill (testing)
* @jakirkham
* @mingwandroid (testing)
* @msarahan


## 2.0.0beta2 (2016-08-22)

This release includes all current (1.21.14) changes made to the 1.21.x series.

### Enhancements

* Configuration is local, passed via config argument.  No more global config.  #953
* Created Python API in `conda_build/api.py` #953
* Separate build folders per-build to allow parallelism #953
* Add locking to allow safe parallelism #953
* Add build flag to turn off separate build folders (--no-build-id) #953
* Much greater test coverage across all modules #953
* Add `CONDA_BUILD_STATE` variable that reflects RENDER, BUILD, or TEST state of build #1232
* Add support for `HG_` variables in meta.yaml templates (for hg repos) #207 #1234
* Add `source_files` test argument in meta.yaml to copy files from source into test #1237

### Bug fixes

* Fix error converting linux to win packages due to python version mismatch #481
* Fix infinite loop that occurred with circular dependencies being built #953
* Improve test data structures to allow profiling with pytest-profiling #953
* Fix version sorting in pypi skeleton generator #1238

### Restructuring

* CLI scripts have been gutted and moved to `conda_build/cli`.  Content from them is in
  `conda_build`, in scripts without `main_` prefix.  #953
* Skeleton generators have been broken out of `main_skeleton.py`, and consolidated into
  `conda_build/skeletons`.  The contents of this folder are examined at runtime for pluggability.  #953

### Contributors

* @melund
* @msarahan
* @pigmej


## 1.21.14 (2016-08-18)

### Bug fixes

* fix pyc compilation when egg files/folders are present #1225

### Contributors

* @msarahan


## 1.21.13 (2016-08-18)

### Enhancements

* use git -am when applying git patches, so that patches better retain git history #1222
* allow relatively pathed git submodules #1222
* add `guess_license_family` to pypi skeleton generator #1222

### Bug fixes

* fix typo in convert.py

### Contributors

* @mingwandroid
* @msarahan


## 1.21.12 (2016-08-17)

### Enhancements

* Whitelist the `CPU_COUNT` environment variable. #1149
* Add tool for examining prefix length in existing packages #1195
* Add a conda interface layer for better compatibility with conda 4.2 #1200 #1203 #1206
* Document how to run tests #1205
* Update default versions for R (3.3.1) and Perl (5.20.3) builds #1220

### Bug fixes

* Don't compile .py files in executable locations.  Compile one at a time.  #1186
* Don't force download if vcs is used as a source #1212
* Break hardlinks as a post-install step.  Hard links can cause problems at package install time.  #1215
* Make environment variables used by conda in environment creation always be bytestrings #1216 #1219

### Contributors

* @jakirkham
* @kalefranz
* @msarahan


## 1.21.11 (2016-08-06)

### Bug fixes

* Correct logic for printout of meta.dist determination #1174
* Attempt to use `src_dir` instead of `WORK_DIR` for directory creation #1175
* Fix escaping problem with `PY_VCRUNTIME_REDIST` setting #1172
* Set build prefix for win by path, not name #1172
* Quote INCLUDE and LIB env var settings for win better #1172
* Fix pypi skeleton package search #1181

### Contributors

* @msarahan
* @pelson


## 1.21.10 (2016-08-02)

### Bug fixes

* Compile files ending with .py, not py.  #1163
* Move root logger to entry points, to not interfere with conda #1164 #1166
* Use setuptools entry points, rather than pre-defined scripts #1165
* Always use the long build prefix to avoid confusion #1168

### Contributors

* @mingwandroid
* @msarahan


## 1.21.9 (2016-08-01)

### Bug fixes

* Add debug option that shows conda output during build.  Hide output otherwise.  #1159
* Add regression test for conda metapackage command, fix missing token and user args. #1160
* Create croot (conda-bld) folder if missing before locking in render and skeleton. #1161

### Contributors

* @msarahan


## 1.21.8 (2016-07-31)

### Bug fixes

* Fix --source argument to build - was building when should only download source.  #1152
* Don't try to create work folder when it exists (but is empty) #1153
* Fix a logic error with `need_source_download` not existing #1148

### New Things

* Don't exit on compileall failure #1146
* Add `CONDA_BUILD_RENDERING` environment variable that is set during recipe rendering #1154
* Change pyc compilation to only affect files that would be packaged (not all of site-packages).  Compile pyc files on py3.  #1155
* Rename `load_setuptools` to `load_setup_py_data` (keep `load_setuptools` for compat; but show warning) #1156
* Test that condarc channels are respected in build #1157

### Contributors

* @daler
* @minrk
* @msarahan


## 1.21.7 (2016-07-22)

### Bug fixes

* Add test of requirements.txt parsing for runtime requirements #1127
* Set `PY_VCRUNTIME_REDIST` for VS 2015+, so that DLL linkage is used #1129
* Use os.path.normpath in `find_lib` #1132
* Fix path prepending in test (use only PATH, and use consolidated code) #1135
* Add dist split for channel names #1136
* Provide fallback path to render recipe when build environment is necessary for rendering #1140
* Sort package versions coming from PyPI for skeleton #1141

### Contributors

* @mingwandroid
* @msarahan


## 1.21.6 (2016-07-14)

### New Things

* Allow pass-through of setup.py options in conda skeleton pypi #680
* Allow specification of pinning numpy in conda skeleton pypi #680
* Support PEP420 namespace packages (don't barf on existing folders.)  Do barf on existing files.  #1074

### Bug fixes

* Fix handling of quotes in selectors #1104
* Fix `load_setuptools` in jinja context.  Problem was incorrect cwd in function. #1106
* Make Win activate script file extensions explicit #1107
* Warn users on failed git repo info failure, rather than crash #1108
* Remove killing MSBuild.exe at end of win build.  Remove psutil dependency.  #1109
* Prepend PATH before creating env, to ensure post-link script success.  #1115, #1118
* Make Python tests drop out on failure appropiately on win  #1122
* Make hyphenation consistent with `include_recipe` in meta.yaml  #1124
* Use full path of test env when activating #1125

### Contributors

* @ikalev
* @msarahan
* @mwcraig


## 1.21.5 (2016-07-07)

### Bug fixes

* Make --skip-existing respect remote channels (s3, file, anaconda.org) #1102
* Reduce `always_include_files` glob fail exit to a warning #1101
* Fail more gracefully when finding a vcs executable fails #1100
* Add better error when PyPI fails with XMLRPC.  Add tests for published examples. #1098
* Fix lack of 'call' in windows test activate script that was terminating tests early #1097
* Take newest version from PyPI when creating skeleton #1092
* Fix unicode encoding error in conda skeleton pypi #1092
* Support PEP420 namespace packages (write into existing folders,
   but raise error rather than overwrite existing files. #1090
* Fix an error where an intermediate None value broke jinja2 rendering #1088
* Add missing support for `include_recipe` in meta.yaml #1085

### Contributors

* @ikalev
* @msarahan


## 1.21.4 (2016-07-05)

### Bug fixes

* Choose newest Pypi skeleton version; fix unicode encoding in pypi metadata #1092
* Add Numpy 1.11 to `all_versions` dict for autocompletion #1078
* Fix MSVC 3.3/3.4 builds when Win7SDK not installed #1072
* Fix an error with build number, when build number is None or otherwise invalid #1088

### Known issues

* Environment activation requires conda >=4.1.6.  The activate.bat script does not look in the right place for the activate.d folder.
* The test suite on Linux and Mac fails the python-build, python-run, and python-build-run tests, because an errant `__conda-version__.txt` file is somehow present.  It is not clear where it comes from, and each of these tests pass when run individually.  If you have mysterious issues, and you use `__conda-version__.txt` or files like it, please file an issue.

### Contributors

* @adament
* @aleksey
* @ikalev
* @msarahan


## 1.21.3 (2016-06-27)

### Bug fixes

* Fix a regression in Windows, where a compiler was a hard requirement, and was not always showing up, anyway.  #1049
Contributors:
* @msarahan


## 1.21.2 (2016-06-24)

### Bug fixes / Improvements

* revert some MSVC activation logic to still call vcvarsall directly in build script
* fix Windows testing for binary prefix replacement (not done on win)
* Add a warning message when conda-build can't create an environment due to unsatisfiable dependencies
* Improve notion of whether a recipe uses a VCS in its metadata, or in its build

### Known issues

* Environment activation on Windows will not work until Conda 4.1.4 is released.  The activate.bat script does not look in the right place for the activate.d folder.
* The test suite on Linux and Mac fails the python-build, python-run, and python-build-run tests, because an errant `__conda-version__.txt` file is somehow present.  It is not clear where it comes from, and each of these tests pass when run individually.  If you have mysterious issues, and you use `__conda-version__.txt` or files like it, please file an issue.

### Contributors

* @msarahan
* @patricksnape


## 1.21.1 (2016-06-22)

### Bug fixes / Improvements

* Simplify MSVC activation, using distutil's existing logic #1036
* Correctly interpret paths returned from git on windows, trying cygpath, falling back to conda regex #1037
* Fix ability to disable anaconda upload in condarc #1043
* Change environment activation to call activation in scripts, rather than having Python store variables #1044

### Contributors

* @msarahan
* @mwcraig
* @patricksnape


## 1.21.0 (2016-06-15)

### New stuff

* Add `FEATURE_` environment variables for MKL, opt and debugging #978
* add info/about.json file that contains the "about" section of meta.yaml #941
* allow `--dirty` flag to be passed to `conda build` command. Skips
  download, and provides DIRTY environment variable in build scripts. #973
* Add msys2 paths to build and test environments #979
* add new x86 and `x86_64` selectors for Intel platforms #986
* keep original meta.yaml in recipe folder of package; create meta.yaml.rendered in recipe folder.  Neither exist when recipe not included.  #1004
* add `ignore_prefix_files` key to build in meta.yaml. Can ignore list of files,
  or True to ignore all prefix files. #1008 #1009
* Automatically determine patch strip level #1011

### Bug fixes/Improvements

* Lightened requirement that x.x be defined in both build and runtime sections.  #650
* Remove info/recipe.json from build conda packages.  Superseded by info/recipe/meta.yaml.rendered.  #781
* Search for single and double backslashes when finding files that need prefix replacement #962
* Track undefined jinja variables and use them to decide whether to download source #964
* handle patches with p0 or p1 #969, #1011, #1020
* only set os.environ for non-None variables #981
* Don't use long prefixes on windows #985
* Fix missing encoding argument #987
* Respect proxy variables more appropriately #989
* Search packages on PyPI, rather than listing them all.  Should avoid some timeout errors there. #991
* Fix unix-style paths returned from git on Windows preventing relative paths from providing Jinja2 metadata #995
* improve logic handling "dirty" downloading.  Always download when not dirty.  #995
* Fix post-build variables when no build section existed in original meta.yaml #999
* Activate `_build` and `_test` environments approriately, rather than manipulating PATH directly #1002
* Don't clone git submodules until after first checkout #1025
* Move `check_install` over from conda.install #1027

### Deprecations

* `__conda_version__.txt` and other post-build methods of altering the build
  string are marked as deprecated. Prefer Jinja2 templates where possible.
  Create issues if this breaks your work.

### Contributors

* @filmor
* @ilanschnell
* @jschueller
* @mingwandroid
* @msarahan
* @pelson
* @stuarteberg
* @whitequark


## 2.0.0beta (2016-06-05)

### Compatibility breaks

* Increase placeholder path to 255 bytes (affects only Linux/Mac.  Packages need to be rebuilt to support longer embedded paths) #877

### Bug fixes/Improvements

* Respect proxy variables more appropriately #989
* Fix post-build variables when no build section existed in original meta.yaml #999
* Fix unix-style paths returned from git on Windows preventing relative paths from providing Jinja2 metadata #995
* improve logic handling "dirty" downloading.  Always download when not dirty.  #995
* Search packages on PyPI, rather than listing them all.  Should avoid some timeout errors there. #991
* Lightened requirement that x.x be defined in both build and runtime sections.  #650
* Search for single and double backslashes when finding files that need prefix replacement #962
* Fix missing encoding argument #987
* Don't use long prefixes on windows #985
* only set os.environ for non-None variables #981
* Track undefined jinja variables and use them to decide whether to download source #964
* handle patches with p0 or p1 #969

### New stuff

* Add `FEATURE_` environment variables for MKL, opt and debugging #978
* add new x86 and `x86_64` selectors for Intel platforms #986
* add info/about.json file that contains the "about" section of meta.yaml #941
* Add msys2 paths to build and test environments #979
* allow `--dirty` flag to be passed to `conda build` command.  Skips download, and provides DIRTY environment variable in build scripts.  #973

### Contributors

* @filmor
* @heather999
* @ilanschnell
* @jschueller
* @mingwandroid
* @msarahan
* @pelson
* @stuarteberg
* @whitequark


## 1.20.3 (2016-05-13)

### Enhancements

* use posix metapackage for cran skeleton packaging (#956)

### Bug fixes

* fix output of package paths (extra output was breaking tools).  Add tests. (#950)
* change default of `no_download_source` in build.py (for compatibility with conda-build-all) (#950)
* fix regression in [] being confused for selectors (#957)


## 1.20.2 (2016-05-13)

### Enhancements

* added --token and --user flags to pass corresponding information to anaconda upload (#921)
* added conda render command that outputs a fully-rendered meta.yaml to either stdout, or to file (with --file) (#908)
* support source checkout tools specified in meta.yaml. If source checkout fails at the rendering phase, source checkout and rendering are re-done after the build environment is created. (#843, #946)
* fn is now optional when a URL specifies a filename. (#942)
* CRAN skeleton generator now uses MSYS2 for Windows support (#942)
* conda build & conda render both recursively look for meta.yaml (support conda-forge feedstock submodules) (#908)
* Whitelist MAKEFLAGS environment variable. Setting this outside conda build should take effect in your build. Parallelize on \*nix by adding -j here, instead of `-j${CPU_COUNT}` in your build.sh. This helps on CI's, where `CPU_COUNT` is not always well-behaved. (#917)
* Run `python_d` executable on windows when debug feature is active (#724)
* add conda build flag --keep-old-work that temporarily moves your last build, then moves it back after completion. For debugging, when more than one package is involved. (#833)
* Allow selectors in imported jinja templates (#739)

### Bug fixes

* fixed several instances wherein --skip-existing did not work (#897, #945)
* Fully render recipe before outputting build string  * fixes empty spots where `GIT_*` info should have been (#923)
* Add MSYS2 path conversion filters to avoid issues with Win 7.1 SDK (#900)
* Address PyPI's change of URL format (#922,
* Fix invalid gcc "-m 32" flag (#916)
* Fix empty section (due to selectors) handling regression (#919)
* Fix regression in handling of VS2008 Pro (not Express + VC for Python 2.7). It is important to at least try to run vcvarsall.bat. (#913)
* Fix CPAN skeleton generator (handle missing sections better) (#912)
* Make test/requires versions match build/requires without additional pinning (#907)
* Remove hard-coded CYGWIN path from conda-build's custom PATH (#903)
* Source is downloaded before testing, fixing an issue where if build machine and some other test machine had different source, strange things happened. (#946)
* Fix regression with Python 3.x fixing shebangs (#892)
* Fix conda inspect crashes by using conda-meta info rather than filenames or dist names for package info (#947)

### Other

* restore AppVeyor testing for Windows builds (#864)
* Build py3.5 on Appveyor (#938)
* PEP8 cleanup; use flake8 rather than pyflakes (#938)
* limited scope of project locking to avoid lock conflicts between build and rendering (#923)
* set up anaconda.org build infrastructure (#924)
* on Windows, environment variables are written to the temporary bld.bat in the source work folder. (#933)


## 1.20.1 (2016-04-21)

* fix source/path and `GIT_*` issues, #801
* fix invalid assertion, #855
* environ.py refactor/clenup, #856
* Better messaging for yaml parsing errors, #862
* fix typo, #863
* make `CONDA_PY` and `CONDA_NPY` available in build.sh, #837
* execute source fetchers (e.g., git, hg) in the `_build` environment, #843
* use memory map rather than read() to reduce memory usage, #866
* fix svn url on Windows in checkout tool test, #867
* fix empty files bug, #869
* improve Visual Studio logic, #861
* add files in order of increasing size to improve access times to tar, #870
* `VS_YEAR`, `VS_VERSION`, `VS_MAJOR` and `CMAKE_GENERATOR` environment variables, #872


## 1.20.0 (2016-03-25)

* support for Lua as a built-in language (Alex Wiltschko), #719
* allow additional keys in "about" section, #831
* fix Examples directory in `noarch_python`, #838
* revert OS X SIP fix, part of #808, #844
* fixed race condition between removal and creation of `tmp_dir` on win, #847


## 1.19.2 (2016-03-10)

* silence some errors when subprocessing git #790
* fixes conda skeleton cran under python3 #817
* fixes some bugs introduced with the #808 otools refactor, #821, #825
* fixes #818 conda-build 1.19.1 breaks C compilation, #825
* actually fix #807 recurisive builds after conda 4.0 release, #826
* fixes #820 crash when building from a git repo on Windows, #824


## 1.19.1 (2016-03-09)

* Environment variables defined in the 'script_env' build section of
  the meta.yaml file were previously assigned the value '<UNDEFINED>'
  if not found in the environment. Now they are left unset and a
  warning is raised instead, #763.
* fix printing of NumPy 1.10 in help message, #776
* add -m32 to CFLAGS and CXXFLAGS for multilib gcc, #775
* fixes `CYGWIN_PREFIX` for drive letters other than C:, #788
* fixes for noarch package building on Windows, #799
* work-arounds for System Integrity Protection on OS X El Capitan, #808
* fix recurisive builds after conda 4.0 release, #813


## 1.19.0 (2016-01-29)

* normalize unicode in conda skeleton cran, #681
* use /bin/sh on openbsd, #707
* fail early during patching
* use symlinks=True in copytree() for SVN sources, #665
* support entry points with dots (to suppoer classes), #690
* deprecate conda pipbuild in favor of conda skeleton. #710
* fix Win references to PipBuild scripts, #723
* allow git shallow clones, #604
* remove broken license file detection code, `about/license_file`
  expects filename now
* allow pinning dependencies when building a package, #741
* fix to restore building for multiple python versions on Windows, #744
* fix building (git unrelated things) when git is not installed, #745
* enable tab completion for the packages argument of the conda inspect
  commands, #748


## 1.18.2 (2015-11-19)

* move path prepending to function for uniformity, #601
* improve yaml loading, #603
* allow jinja2 templates to be located in current conda environment, #578
* fix `NPY_VER` for versions >= 1.10 (Should be '1.10', not '1.1.0'), #660
* create jinja2 environment with 'strict' mode for undefined values, #661
* add a method to shell out and execute a command through subprocess, #621


## 1.18.1 (2015-10-16)

* allow config system to handle versions with have more than a single digit
  in the minor version, #626
* fix None encoding bug, #614
* add missing Python version when adding Python to test specs
* add features to build string
* improve yaml loading (you don't have to quote version numbers anymore, eg.
  if the version is 3.1), #603


## 1.18.0 (2015-10-01)

* develop options `--build_ext`, `--clean_build_ext`, #512
* fix directory not existing when using --no-include-recipe option
* add support for multiple rpaths on OS X to conda inspect
* don't add 'np' to build string when package depends on numpy, but not
  a specific version
* be more explicit when numpy version is included in dependency specs, #573
* correctly remove egg directories on Windows, #536
* add new option `msvc_compiler` to build section for forcing MSVC compiler
  version
* add new command conda inspect channels --test-installable
* fix a Unicode issue with conda skeleton cpan
* when auto-adding python spec to execute `run_test.py`, don't require a
  specific version
* add uninstall option to conda develop
* give a better error message in skeleton pypi for packages with invalid
  urls
* don't try to test skipped recipes
* don't exit on a skipped recipe
* recursively build packages from unsatisfiable install hints
* make recursive building work better with --skip-existing
* update `CONDA_R` to 3.2.2
* fix encoding issues with `git_info` on Windows
* test Python 3.5 in Travis CI
* add support for absolute rpaths on Linux


## 1.17.0 (2015-08-24)

* quote set calls in bld.bat
* use the trash on Windows when deleting environments, see #521
* improve documentation in `noarch_python` source
* rename 'binstar' -> 'anaconda', see #519
* allow blank sections in meta.yaml, see #533
* add --no-include-recipe option to conda-build, see #535
* add ability to add license file in info/license.txt, see #545
* don't recursively build recipes more than once, #538
* .git can be a file, #537


## 1.16.0 (2015-07-30)

* handle trailing slashes in package names in conda skeleton cran
* Cygwin git now works correctly.
* the prefix itself is now included in the PATH in the test script on
  Windows (previously it was just the Scripts directory)
* by default, recipes that runtime depend on numpy will no longer depend on
  an explicit version of numpy. The old behavior is still available by
  setting the `CONDA_NPY` environment variable or using conda build --numpy
* add py35 variable to selector namespace
* improve conda-meta untracked files error message
* fix conda build --help in Python 2
* add `conda_build.sub_commands` object which is a list of conda sub-commands


## 1.15.0 (2015-07-22)

* fix conda skeleton cran --update-outdated --output-dir .
* add argcomplete completers for recipes, --python, --numpy, --R, CRAN
  packages (with conda skeleton cran), and PyPI packages (with conda
  skeleton pypi)
* conda develop now relinks object files on OS X (#490)
* allow a glob for always-include-files
* allow an extra section in meta.yaml, with free-form content (#483)
* don't echo environment variables when building on Windows (#274)
* add conda build --skip-existing
* show default in help for conda skeleton --output-dir
* add --update-outdated option to conda skeleton cran
* skeleton: fix `noarch_python` option when `build_comment` is "#"
* don't allow to build a package with the conda-meta directory
* automatically remove a package of the recipe itself if it is installed as
  a build dependency
* allow 'extra' key in meta.yaml, see #483
* move echo command in Windows build, see #274
* add regex to always included files, see #484
* add strings in `conda.config.non_x86_linux_machines`, e.g. "ppc64le",
  as selector variables (renames armv6 to armv6l)


## 1.14.1 (2015-06-29)

* add --size option to change RSA modulus length when generating RSA key
  pairs (defaults to 2048 bit)
* make use of `Crypto.Signature.PKCS1_PSS` module, see #469
* update default for `CONDA_R` to 3.2.0
* manually install dependencies of recommended R packages in the
  build.sh, #457
* fix issues when git commits have non-ASCII characters, #458
* catch tarfile.ReadError in conda index, #460


## 1.14.0 (2015-06-16)

* add support for signing packages, and indexing them, #430
* removing `LIBRARY_PATH` and `INCLUDE_PATH` build environment variables on
  Unix, they where originally added in #228, but are causing problem for
  some people and are not really necessary
* don't rename meta.yaml to meta.yaml.orig in the recipe that is copied into
  built packages
* handle links to libraries that exist in multiple places better on OS X
* add --no-remove option to conda index
* various fixes for --python, --numpy, --perl, and --R
* various cleanups for the command documentation
* fix conda skeleton pypi --pypi-url
* don't add the module name to the import tests in conda skeleton pypi
* add --groupby option to conda inspect linkages
* fix some incorrect "not found" instances from conda inspect linkages on OS
  X
* don't include versions with restrictions in the build string
* don't fail if conda-build cannot be found for the version check
* remove special logic if the username on Windows is "builder"
* conda skeleton pypi: add --noarch-python
* fix issue with filenames with spaces in conda convert
* place noarch packages in the noarch directory
* handle `tests_require` in conda skeleton pypi
* pipbuild: don't check if package already exists
* skeleton pypi: remove --no-download option
* add noarch option to pipbuild
* add ability to sign packages


## 1.13.0 (2015-05-19)

* skeleton pypi: fail better for packages with bad urls
* fix summary in `bdist_conda`
* fix compiling pyc files in Python 3
* convert: correctly set the subdir key in the metadata
* add --git-tag to skeleton cran
* include LANG in the build environment
* export proxy environment variables
* fix conda skeleton cran --cran-url
* set `CONDA_DEFAULT_ENV` in the build environment
* fix conda index -c
* correctly extract .tar.Z files
* avoid infinite loops in conda skeleton pypi --recursive
* add --all to conda inspect linkages and conda inspect objects
* add --manual-url to skeleton pypi
* fix issue where 'conda index' with old packages would create bad metadata
* resolve circular dependencies in conda-skeleton (#409)
* use versioneer 0.14 (#385)
* `always_include_files` errors out (exits) on files that aren't there (#387)
* automatically lowercase the package name in `bdist_conda` (see
  aplpy/aplpy#259)


## 1.12.1 (2015-04-28)

* fix regression in `always_include_files` that causes build failure (#386)


## 1.12.0 (2015-04-10)

* correctly fix egg directories that are part of the package
* use the --force-rpath flag to patchelf
* update `MACOSX_DEPLOYMENT_TARGET` to 10.6
* fix running tests for Python packages whose version differs from the
  version in conda
* fix some Python 3 issues with pipbuild
* don't allow packages to depend on themselves
* allow to use the r- prefix in conda skeleton cran
* make recommended r packages depend on r-base in skeleton cran
* new post-build logic on OS X. All libraries on OS X now include `LC_RPATH`,
  which points to the environment lib directory, and use and install name
  using @rpath
* don't set `DYLD_FALLBACK_LIBRARY_PATH` in cran recipes (the new `LC_RPATH`
  logic on OS X makes this unnecessary)
* fix conda build --build-only when the long build prefix is used
* make conda inspect linkages work on OS X
* don't hide the traceback for maximum recursion depth exceeded errors
* add conda inspect objects, for inspecting object files in packages
  (OS X only)
* add --untracked flag to conda inspect linkages
* build R packages against a specific version of R
* decompress .tar.z files
* add support for GitHub urls in conda skeleton cran


## 1.11.0 (2015-03-05)

* add `script_env` key in build section of meta.yaml file, which is a list
  of environment variable names which are made available in the build
  script.  If a variable is listed here, but is not in the environment,
  the value '<UNDEFINED>' is assigned.
* Handle OSError in conda index
* Fix how the PATH environment variable is set on Windows
* Remove the work directory earlier in the build
* Give a helpful error message for dependencies like "python >= 2.7"
* Add `CYGWIN_PREFIX` environment variable on Windows
* Handle list requires in skeleton pypi
* Correctly fail if the Windows bld.bat exits 1
* Give a better error message if no urls can be found for a package
* Add `__main__` to allow python -m `conda_build`
* %R% is now set to R.exe instead of R.bat on Windows
* Write the build script to the source directory for build/script instead of
  the recipe directory.
* Handle non-directories in `copy_into` (avoids an OSError, #332)
* Halt the build on YAML error without jinja2
* Clone git sources with the --recursive option
* Add --channel and --override-channels to conda build. -c is changed to
  mean --channel instead of --check.
* Add --check-md5 flag to conda index
* Look for vcvarsall.bat from the Microsoft Visual C++ Compiler for Python 2.7
* Use PyPi XMLRCP client search in order to ignore case for PyPi package
  names in pipbuild


## 1.10.2 (2015-02-10)

* don't set the `GIT_*` environment variables when the source is not a git repo
* skeleton cran: add extra metadata from CRAN to the recipe
* skeleton pypi: fix there not being a fragment in a url
* don't match comment only lines as selectors


## 1.10.1 (2015-02-06)

* greatly improved ability to create `noarch_python` packages, #317
* added 'subdir' key to info/index.json
* allow url to be a list or urls, which are tried until one works
* use quotes instead of !!str for versions from the conda skeleton commands
* add conda skeleton cran to generate recipes for packages from CRAN
* add support for adding a readme to a recipe
* add a --quiet option to conda convert


## 1.10.0 (2015-01-15)

* automatically convert absolute symlinks to paths in the build prefix to
  relative ones.
* error if there are symlinks to the source directory.
* use the placeholder prefix in text files rather than the build prefix
* allow non-Python packages to be converted to other platforms with conda
  convert
* new command conda inspect for inspecting packages. The only subcommand so
  far is conda inspect linkages, which shows the dynamic linkages of the
  shared object files on Linux.
* correctly handle Unix style `has_prefixes` on Windows
* run the tests in Binstar build
* only modify egg directories that are part of the package being built
* don't exclude .dylib files from prefix replacement
* ability to build noarch packages
* allow specifying files to always include
* fix for building dependencies in some cases
* print the correct thing for binary files detected with a prefix


## 1.9.1 (2014-11-18)

* set PYTHONNOUSERSITE=1 while running build scripts
* conda index: add error if they try to mix their packages into Anaconda
  channel
* fix building recipes with local git urls in Windows
* warn if conda-build is out of date


## 1.9.0 (2014-10-22)

* adapt tests for Windows
* don't use the long build prefix if the short build prefix is already long
* support rewriting library load path for libraries that are in
  subdirectories of lib/ on OS X
* allow `git_rev` as a valid key in 'source', which is identical in behavior
  to `git_branch` and `git_tag` (all checkout the given revision)
* also grab the full HEAD sha1 and shove it into the environmental
  variable `GIT_FULL_HASH`
* automatically detect text prefix files
* add `detect_binary_files_with_prefix` flag to meta.yaml to automatically
  detect binary files with the prefix and add them to
  `binary_has_prefix_files`
* fix `git_info` when the author or commit message contains Unicode characters
* allow to pass a url to skeleton pypi
* add `NPY_VER` environment variable
* fix conda convert --show-imports
* give better error message when encountering a corrupt tarfile in conda
  index
* print{ some more helpful information about what is going on at the
  beginning of a build
* allow source/path in the meta.yaml to specify a path to the source (which
  can be relative to the recipe directory)
* support xz files in Python 3 without requiring unxz
* put spaces after skeleton pypi comments
* correctly detect when to preserve the egg directory and depend on
  setuptools in skeleton pypi
* set `LIBRARY_PATH` and `INCLUDE_PATH` when building on Unix
* allow selectors to have text after them if they are in a comment
* add `CPU_COUNT` environment variable to the build


## 1.8.2 (2014-09-19)

* add substantially more tests
* add ability to set additional rpath directories using build/rpaths
* patch command on windows no-longer takes the --binary option
* fix post processing so that name-space packages can be 'flattened' into
  a single directory
* don't remove the .svn directory when doing a svn checkout


## 1.8.1 (2014-09-03)

* `has_prefix` paths must always use /, even on Windows
* fix bug in Windows Python 2
* add .travis.yml
* allow recipes to use requirements.txt
* fix building a package that has Mach-O stub files
* fix recursive package building
* handle empty data size in pypi
* allow an explicitly set empty version string


## 1.8.0 (2014-08-22)

* add ability to convert Golke's Windows packages into conda
  packages, use "conda convert <Gohlke>.exe".  See also:
  http://www.lfd.uci.edu/~gohlke/pythonlibs/
* handle spaces on Windows better
* add croot to the module level of `conda_build.config` for backwards
  compatibility
* changed extra long prefix for building to `_placehold...`


## 1.7.1 (2014-08-20)

* add --all-extras flag to skeleton pypi
* automatically use the long or short build prefix as needed
* fix to allow specification of full major.micro.minor for numpy, python,
  and perl (only add the build string if it is an exact major.minor or
  major.minor.patch version. If it is an inequality, it is not added)


## 1.7.0 (2014-08-05)

* better `install_requires` parsing for skeleton pypi
* the build environment from conda-build is now called `_build___...`
  This is so that recipes with `binary_has_prefix_files` build against a
  sufficiently long prefix.
* don't overwrite the input file in convert
* fix a bug related to the `prefix_files.txt` file
* show the download bytes in human form in skeleton pypi
* make patchelf error message clearer
* fix some issues with the git describe environment variables
* improve shebang line modifications with python.app
* show the download bytes in human form in skeleton pypi


## 1.6.1 (2014-07-29)

* fix an issue building with a git repository in Python 3


## 1.6.0 (2014-07-29)

* don't fail on MachO stub files on OS X
* add some git describe related environment variables when the source is a
  git repository
* add --python and --numpy flags to conda build, which do the same thing as
  setting `CONDA_PY` and `CONDA_NPY`
* allow a . in `CONDA_PY` and `CONDA_NPY`
* correctly catch RuntimeError
* fix an issue building some packages on Windows
* make skeleton pypi --recursive work with versioned dependencies
* some additional type checking for meta.yaml
* always include numpy in skeleton pypi


## 1.5.0 (2014-07-03)

* add `bdist_conda`
* fix features and `track_features`
* detect files with the build prefix automatically on Windows


## 1.4.0 (2014-07-01)

* fix skeleton pypi behind a proxy
* add `binary_has_prefix_files,` which does a binary prefix replacement
* fix skeleton pypi on Windows
* allow the `git_url` to be a relative path to the recipe directory


## 1.3.5 (2014-06-04)

* the yaml script tag was only written if build.sh already existed,
  see issue #105
* use `tests_require` to fill in test requirements in the setuptools
  template, see issue #107


## 1.3.4 (2014-06-02)

* add --build-only and --post flags to conda-build
* add conda convert -p all
* allow to set `__conda_buildnum__.txt` and `__conda_buildstr__.txt`, analogous
  to `__conda_version__.txt`


## 1.3.3 (2014-04-28)

* add SHA256 support for downloaded source
* conda convert now creates platform directories, like
  `win-32/converted_package.tar.bz2`
* allow to specify the version of python, numpy, or perl in the meta.yaml
  (it will ignore the `CONDA_PY`, `CONDA_NPY`, or `CONDA_PERL`, respectively, in
  this case)


## 1.3.2 (2014-04-15)

* allow changing conda-bld directory (which is by default <root>/conda-bld
  when the conda root is not writable, and ~/conda-bld otherwise), to be
  changed by `CONDA_BLD_PATH` environment variable or conda-build: root-dir:
  in condarc file
* add `build/has_prefix_files`
* remove broken `conda-build/build_dest`
* fix build in Windows Python 2
* add --quiet option to conda-build
* add check for characters in package name dependencies
* add .class to the object file extension blacklist
* removed `build/no_softlink` in favor of `build/no_link` with list of glob
  syntax


## 1.3.1 (2014-03-25)

* add conda metapackage command
* fix recursive conda building when dependencies are nested more than one
  level deep.
* fix build in Windows Python 2
* fix skeleton pypi for packages whose setup.py has `__future__` imports
* add conda pipbuild command which uses a simple recipe based on pip
  install to build a conda package
* fix skeleton pypi and pipbuild when package data does not have classifiers
* add a basic conda develop command
* add the --recursive option to conda skeleton pypi
* conda skeleton pypi no longer asks about single line licenses
* conda skeleton pypi now queries pypi case insensitively
* conda skeleton pypi now works in a different conda environment. This
  avoids anything bad that might happen when trying to get the metadata from
  the package from messing up the root environment.
* conda skeleton pypi now patches distribute directly. This is more robust
  than trying to insert a patch into setup.py, as was done previously.
* allow to set the version post-build by writing a `__conda_version__.txt`
  file to the source directory.
* add ability to skip binary relocation step by
  setting `build/binary_relocation: False` in meta.yaml


## 1.3.0 (2014-03-14)

* add skeleton for CPAN Perl packages, issue #53. Unlike
  the PyPI skeleton, it supports a --recursive option to
  also generate the recipes for all of the dependencies of
  a given module/distribution
* add support for `run_test.pl` and Perl import tests when
  building Perl packages
* add `CONDA_PERL` environment variable support for
  determining which version of Perl to build packages for.
  Unlike `CONDA_PY`, this must include the full version with
  periods (e.g., 5.18.2)
* automatically build packages for dependencies if the recipe is
  present in the current working directory
* fix a number of Python 3 compatibility issues, issue #59
* work with source files with uppercase suffixes
* switch from chrpath to patchelf on Linux, issue #57
* don't use hard-coded msvc path
* sort import tests from skeleton pypi


## 1.2.1 (2014-02-25)

* added `conda-build/build_dest` option to condarc


## 1.2.0 (2014-02-13)

* make sure `WORK_DIR` exists
* use MSVC 2010 for Python 3
* include the summary with conda skeleton pypi
* fix object detection on Python 3
* update default `CONDA_NPY` to 18


## 1.1.0 (2014-02-06)

* add ability to use templates in conda recipes
* remove fallback to <root>/conda-recipes, i.e. conda-build always
  expects the full path to the recipe
* export PKG Build Number
* add pre-link to package, when it is found in recipe
* allow to add `run_test.sh` or `run_test.bat`, which will be run automatically
  during the test phase.
* Test commands from the test/commands section of meta.yaml are run from
  bash on Linux and OS X and batch on Windows (previously they were run
  using Python's subprocess).
* all environment variables from the build process are available during the
  tests, except with the build prefix replaced with the test prefix.


## 1.0.0 (2014-01-24)

* initial release
* includes conda-build, conda-convert, conda-index, conda-skeleton
* depends on new conda version 3
* add license to info/index.json object
