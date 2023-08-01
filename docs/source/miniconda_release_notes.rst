=======================
Miniconda Release Notes
=======================

Miniconda 23.5.2 (July 13, 2023)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User-Facing Changes
-------------------

* Conda has been updated to v23.5.2 (`conda issue 12836 <https://github.com/conda/conda/issues/12836>`_).

Available Python Versions
--------------------------

* 3.11
* 3.10
* 3.9
* 3.8



Miniconda 23.5.1 (July 12, 2023)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User-Facing Changes
-------------------

* Conda has been updated to v23.5.1 (`conda issue 12873 <https://github.com/conda/conda/issues/12873>`_).

Available Python Versions
--------------------------

* 3.11
* 3.10
* 3.9
* 3.8



Miniconda 23.5.0-3 (July 11, 2023)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User-Facing Changes
-------------------

* Conda has been updated to v23.5.0.
* OpenSSL has been updated to version 3.
* The default installer uses python-3.11.3.


Bug Fixes
---------

* Address a bug that can cause accidental file deletion with Windows uninstallers (see our `blog post <https://www.anaconda.com/blog/windows-installer-security-fix>`_). A `security patch <https://repo.anaconda.com/miniconda/Miniconda3-uninstaller-patch-win-64-2023.07-0.exe>`_ is available for older versions.


Known Issues
------------

* The .pkg installers may skip the "Destination Select" page after accepting the license agreement. See our `Anaconda installation instructions <https://docs.anaconda.com/free/anaconda/install/mac-os/>`_ for details.


Available Python Versions
--------------------------

* 3.11
* 3.10
* 3.9
* 3.8


Packages
--------

**linux-64**


* boltons 23.0.0
* brotlipy 0.7.0
* bzip2 1.0.8
* c-ares 1.19.0
* ca-certificates 2023.05.30
* certifi 2023.5.7
* cffi 1.15.1
* charset-normalizer 2.0.4
* conda 23.5.0
* conda-content-trust 0.1.3
* conda-libmamba-solver 23.5.0
* conda-package-handling 2.1.0
* conda-package-streaming 0.8.0
* cryptography 39.0.1
* fmt 9.1.0
* icu 58.2
* idna 3.4
* jsonpatch 1.32
* jsonpointer 2.1
* krb5 1.20.1
* ld_impl_linux-64 2.38
* libarchive 3.6.2
* libcurl 8.1.1
* libedit 3.1.20221030
* libev 4.33
* libffi 3.4.4
* libgcc-ng 11.2.0
* libgomp 11.2.0
* libmamba 1.4.1
* libmambapy 1.4.1
* libnghttp2 1.52.0
* libsolv 0.7.22
* libssh2 1.10.0
* libstdcxx-ng 11.2.0
* libuuid 1.41.5
* libxml2 2.10.3
* lz4-c 1.9.4
* ncurses 6.4
* openssl 3.0.9
* packaging 23.0
* pcre2 10.37
* pip 23.1.2
* pluggy 1.0.0
* pybind11-abi 4
* pycosat 0.6.4
* pycparser 2.21
* pyopenssl 23.0.0
* pysocks 1.7.1
* python 3.11.4
* readline 8.2
* reproc 14.2.4
* reproc-cpp 14.2.4
* requests 2.29.0
* ruamel.yaml 0.17.21
* setuptools 67.8.0
* six 1.16.0
* sqlite 3.41.2
* tk 8.6.12
* toolz 0.12.0
* tqdm 4.65.0
* tzdata 2023c
* urllib3 1.26.16
* wheel 0.38.4
* xz 5.4.2
* yaml-cpp 0.7.0
* zlib 1.2.13
* zstandard 0.19.0
* zstd 1.5.5

**linux-aarch64**


* boltons 23.0.0
* brotlipy 0.7.0
* bzip2 1.0.8
* c-ares 1.19.0
* ca-certificates 2023.05.30
* certifi 2023.5.7
* cffi 1.15.1
* charset-normalizer 2.0.4
* conda 23.5.0
* conda-content-trust 0.1.3
* conda-libmamba-solver 23.5.0
* conda-package-handling 2.1.0
* conda-package-streaming 0.8.0
* cryptography 39.0.1
* fmt 9.1.0
* icu 68.1
* idna 3.4
* jsonpatch 1.32
* jsonpointer 2.1
* krb5 1.20.1
* ld_impl_linux-aarch64 2.38
* libarchive 3.6.2
* libcurl 8.1.1
* libedit 3.1.20221030
* libev 4.33
* libffi 3.4.4
* libgcc-ng 11.2.0
* libgomp 11.2.0
* libmamba 1.4.1
* libmambapy 1.4.1
* libnghttp2 1.52.0
* libsolv 0.7.22
* libssh2 1.10.0
* libstdcxx-ng 11.2.0
* libuuid 1.41.5
* libxml2 2.10.3
* lz4-c 1.9.4
* ncurses 6.4
* openssl 3.0.9
* packaging 23.0
* pcre2 10.37
* pip 23.1.2
* pluggy 1.0.0
* pybind11-abi 4
* pycosat 0.6.4
* pycparser 2.21
* pyopenssl 23.0.0
* pysocks 1.7.1
* python 3.11.4
* readline 8.2
* reproc 14.2.4
* reproc-cpp 14.2.4
* requests 2.29.0
* ruamel.yaml 0.17.21
* setuptools 67.8.0
* six 1.16.0
* sqlite 3.41.2
* tk 8.6.12
* toolz 0.12.0
* tqdm 4.65.0
* tzdata 2023c
* urllib3 1.26.16
* wheel 0.38.4
* xz 5.4.2
* yaml-cpp 0.7.0
* zlib 1.2.13
* zstandard 0.19.0
* zstd 1.5.5

**linux-ppc64le**


* boltons 23.0.0
* brotlipy 0.7.0
* bzip2 1.0.8
* c-ares 1.19.0
* ca-certificates 2023.05.30
* certifi 2023.5.7
* cffi 1.15.1
* charset-normalizer 2.0.4
* conda 23.5.0
* conda-content-trust 0.1.3
* conda-libmamba-solver 23.5.0
* conda-package-handling 2.1.0
* conda-package-streaming 0.8.0
* cryptography 39.0.1
* fmt 9.1.0
* icu 58.2
* idna 3.4
* jsonpatch 1.32
* jsonpointer 2.1
* krb5 1.20.1
* ld_impl_linux-ppc64le 2.38
* libarchive 3.6.2
* libcurl 8.1.1
* libedit 3.1.20221030
* libev 4.33
* libffi 3.4.4
* libgcc-ng 11.2.0
* libgomp 11.2.0
* libmamba 1.4.1
* libmambapy 1.4.1
* libnghttp2 1.52.0
* libsolv 0.7.22
* libssh2 1.10.0
* libstdcxx-ng 11.2.0
* libuuid 1.41.5
* libxml2 2.10.3
* lz4-c 1.9.4
* ncurses 6.4
* openssl 3.0.9
* packaging 23.0
* pcre2 10.37
* pip 23.1.2
* pluggy 1.0.0
* pybind11-abi 4
* pycosat 0.6.4
* pycparser 2.21
* pyopenssl 23.0.0
* pysocks 1.7.1
* python 3.11.4
* readline 8.2
* reproc 14.2.4
* reproc-cpp 14.2.4
* requests 2.29.0
* ruamel.yaml 0.17.21
* setuptools 67.8.0
* six 1.16.0
* sqlite 3.41.2
* tk 8.6.12
* toolz 0.12.0
* tqdm 4.65.0
* tzdata 2023c
* urllib3 1.26.16
* wheel 0.38.4
* xz 5.4.2
* yaml-cpp 0.7.0
* zlib 1.2.13
* zstandard 0.19.0
* zstd 1.5.5

**linux-s390x**


* boltons 23.0.0
* brotlipy 0.7.0
* bzip2 1.0.8
* c-ares 1.19.0
* ca-certificates 2023.05.30
* certifi 2023.5.7
* cffi 1.15.1
* charset-normalizer 2.0.4
* conda 23.5.0
* conda-content-trust 0.1.3
* conda-libmamba-solver 23.5.0
* conda-package-handling 2.1.0
* conda-package-streaming 0.8.0
* cryptography 39.0.1
* fmt 9.1.0
* icu 68.1
* idna 3.3
* jsonpatch 1.32
* jsonpointer 2.1
* krb5 1.20.1
* ld_impl_linux-s390x 2.38
* libarchive 3.6.2
* libcurl 8.1.1
* libedit 3.1.20221030
* libev 4.33
* libffi 3.4.2
* libgcc-ng 11.2.0
* libgomp 11.2.0
* libmamba 1.4.1
* libmambapy 1.4.1
* libnghttp2 1.52.0
* libsolv 0.7.22
* libssh2 1.10.0
* libstdcxx-ng 11.2.0
* libuuid 1.41.5
* libxml2 2.10.3
* lz4-c 1.9.4
* ncurses 6.4
* openssl 3.0.9
* packaging 23.0
* pcre2 10.37
* pip 23.1.2
* pluggy 1.0.0
* pybind11-abi 4
* pycosat 0.6.4
* pycparser 2.21
* pyopenssl 23.0.0
* pysocks 1.7.1
* python 3.11.4
* readline 8.2
* reproc 14.2.4
* reproc-cpp 14.2.4
* requests 2.29.0
* ruamel.yaml 0.17.21
* setuptools 67.8.0
* six 1.16.0
* sqlite 3.41.2
* tk 8.6.12
* toolz 0.12.0
* tqdm 4.65.0
* tzdata 2023c
* urllib3 1.26.16
* wheel 0.38.4
* xz 5.4.2
* yaml-cpp 0.7.0
* zlib 1.2.13
* zstandard 0.19.0
* zstd 1.5.5

**osx-64**


* boltons 23.0.0
* brotlipy 0.7.0
* bzip2 1.0.8
* c-ares 1.19.0
* ca-certificates 2023.05.30
* certifi 2023.5.7
* cffi 1.15.1
* charset-normalizer 2.0.4
* conda 23.5.0
* conda-content-trust 0.1.3
* conda-libmamba-solver 23.5.0
* conda-package-handling 2.1.0
* conda-package-streaming 0.8.0
* cryptography 39.0.1
* fmt 9.1.0
* icu 58.2
* idna 3.4
* jsonpatch 1.32
* jsonpointer 2.1
* krb5 1.20.1
* libarchive 3.6.2
* libcurl 8.1.1
* libcxx 14.0.6
* libedit 3.1.20221030
* libev 4.33
* libffi 3.4.4
* libiconv 1.16
* libmamba 1.4.1
* libmambapy 1.4.1
* libnghttp2 1.52.0
* libsolv 0.7.22
* libssh2 1.10.0
* libxml2 2.10.3
* lz4-c 1.9.4
* ncurses 6.4
* openssl 3.0.9
* packaging 23.0
* pcre2 10.37
* pip 23.1.2
* pluggy 1.0.0
* pybind11-abi 4
* pycosat 0.6.4
* pycparser 2.21
* pyopenssl 23.0.0
* pysocks 1.7.1
* python 3.11.4
* python.app 3
* readline 8.2
* reproc 14.2.4
* reproc-cpp 14.2.4
* requests 2.29.0
* ruamel.yaml 0.17.21
* setuptools 67.8.0
* six 1.16.0
* sqlite 3.41.2
* tk 8.6.12
* toolz 0.12.0
* tqdm 4.65.0
* tzdata 2023c
* urllib3 1.26.16
* wheel 0.38.4
* xz 5.4.2
* yaml-cpp 0.7.0
* zlib 1.2.13
* zstandard 0.19.0
* zstd 1.5.5

**osx-arm64**


* boltons 23.0.0
* brotlipy 0.7.0
* bzip2 1.0.8
* c-ares 1.19.0
* ca-certificates 2023.05.30
* certifi 2023.5.7
* cffi 1.15.1
* charset-normalizer 2.0.4
* conda 23.5.0
* conda-content-trust 0.1.3
* conda-libmamba-solver 23.5.0
* conda-package-handling 2.1.0
* conda-package-streaming 0.8.0
* cryptography 39.0.1
* fmt 9.1.0
* icu 68.1
* idna 3.4
* jsonpatch 1.32
* jsonpointer 2.1
* krb5 1.20.1
* libarchive 3.6.2
* libcurl 8.1.1
* libcxx 14.0.6
* libedit 3.1.20221030
* libev 4.33
* libffi 3.4.4
* libiconv 1.16
* libmamba 1.4.1
* libmambapy 1.4.1
* libnghttp2 1.52.0
* libsolv 0.7.22
* libssh2 1.10.0
* libxml2 2.10.3
* lz4-c 1.9.4
* ncurses 6.4
* openssl 3.0.9
* packaging 23.0
* pcre2 10.37
* pip 23.1.2
* pluggy 1.0.0
* pybind11-abi 4
* pycosat 0.6.4
* pycparser 2.21
* pyopenssl 23.0.0
* pysocks 1.7.1
* python 3.11.4
* python.app 3
* readline 8.2
* reproc 14.2.4
* reproc-cpp 14.2.4
* requests 2.29.0
* ruamel.yaml 0.17.21
* setuptools 67.8.0
* six 1.16.0
* sqlite 3.41.2
* tk 8.6.12
* toolz 0.12.0
* tqdm 4.65.0
* tzdata 2023c
* urllib3 1.26.16
* wheel 0.38.4
* xz 5.4.2
* yaml-cpp 0.7.0
* zlib 1.2.13
* zstandard 0.19.0
* zstd 1.5.5

**win-64**


* boltons 23.0.0
* brotlipy 0.7.0
* bzip2 1.0.8
* ca-certificates 2023.05.30
* certifi 2023.5.7
* cffi 1.15.1
* charset-normalizer 2.0.4
* colorama 0.4.6
* conda 23.5.0
* conda-content-trust 0.1.3
* conda-libmamba-solver 23.5.0
* conda-package-handling 2.1.0
* conda-package-streaming 0.8.0
* console_shortcut_miniconda 0.1.1
* cryptography 39.0.1
* fmt 9.1.0
* idna 3.4
* jsonpatch 1.32
* jsonpointer 2.1
* libarchive 3.6.2
* libcurl 8.1.1
* libffi 3.4.4
* libiconv 1.16
* libmamba 1.4.1
* libmambapy 1.4.1
* libsolv 0.7.22
* libssh2 1.10.0
* libxml2 2.10.3
* lz4-c 1.9.4
* menuinst 1.4.19
* openssl 3.0.9
* packaging 23.0
* pcre2 10.37
* pip 23.1.2
* pluggy 1.0.0
* powershell_shortcut_miniconda 0.0.1
* pybind11-abi 4
* pycosat 0.6.4
* pycparser 2.21
* pyopenssl 23.0.0
* pysocks 1.7.1
* python 3.11.4
* reproc 14.2.4
* reproc-cpp 14.2.4
* requests 2.29.0
* ruamel.yaml 0.17.21
* setuptools 67.8.0
* six 1.16.0
* sqlite 3.41.2
* tk 8.6.12
* toolz 0.12.0
* tqdm 4.65.0
* tzdata 2023c
* urllib3 1.26.16
* vc 14.2
* vs2015_runtime 14.27.29016
* wheel 0.38.4
* win_inet_pton 1.1.0
* xz 5.4.2
* yaml-cpp 0.7.0
* zlib 1.2.13
* zstandard 0.19.0
* zstd 1.5.5
