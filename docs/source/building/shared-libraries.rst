Using shared libraries
======================

**Shared libraries** are libraries that are loosely coupled to the programs and extensions that depend on them. When loading an executable into memory, an operating system will find all dependent shared libraries and link them to the executable so that it can run. 

The major operating systems Linux, OS X, and Windows all provide a way to build executables and libraries that contain links to the shared libraries they depend on, instead of the directly linking the libraries themselves. We'll discuss Linux and OS X first, then Windows because it is quite a bit different.

Shared libraries in Linux and OS X
----------------------------------

In Linux and OS X, dynamic links are discovered in a similar manner to the way that python modules are discovered via ``PYTHONPATH``, and executables are discovered via ``PATH``.  A list of search locations is made, then the library objects are searched for in the search locations.  By default, as well as by design, the system dynamic linker does not have any special preference for the conda environment lib directories.

Both absolute links and relative links may be specified. If the links were absolute paths like ``/Users/jsmith/my_build_env`` then the library would only work on a system where that exact path exists. Therefore, relative links are preferred in conda packages.

To use relative links, we need to use a special variable in the link itself.  In Linux, the $ORIGIN variable allows you to say "relative to this file as it's being executed".  On OS X, there are ``@rpath``, ``@loader_path``, ``@executable_path``.  ``@rpath`` allows you to set relative links from the system load paths, while ``@loader_path`` is equivalent to ``$ORIGIN``, and ``@executable_path`` supports the Apple ".app" directory approach, where libraries know where they live relative to their calling application. 

Conda build uses ``$ORIGIN`` on Linux and ``@loader_path`` on Mac OS X since we install into a common root directory and can assume that other libraries will also be installed into that root.  The use of the variables allows us to build *relocatable binaries* that can be built on one person's system and sent everywhere.

On Linux, ``conda-build`` modifies any shared libraries or generated executables to use a relative dynamic link by calling the ``patchelf`` tool. On Mac OS X, the ``install_name_tool`` tool is used.

CAUTION: setting ``LD_LIBRARY_PATH`` (on Linux) or ``DYLD_LIBRARY_PATH`` (on Mac OS X) can interfere with this because the dynamic linker short-circuits link resolution by first looking at ``LD_LIBRARY_PATH``. 

For example, let's assume that you decided to install an old version of ``libcurl`` into your conda environment due to some compatibility issues with the code you're using.  Then, you set ``export LD_LIBRARY_PATH=/home/jsmith/envs/curl_env/lib``.  From now on, every program you execute in that session will favor this libcurl to your system libcurl, since it's now effectively at the "front" of the dynamic load path. 

Therefore, we discourage the inclusion of conda environment paths in ``LD_LIBRARY_PATH`` or ``DYLD_LIBRARY_PATH``.

Shared libraries in Windows
---------------------------

Windows does not have the same concept of embedding links into binaries. Here are the rules for Windows:

https://msdn.microsoft.com/en-us/library/7d83bc18.aspx

Most DLLs go into ``(install prefix)\Library\bin``. This now gets added to ``os.environ["PATH"]`` for all Python processes. 

Set ``PATH`` dynamically for your application, so that the RIGHT DLL gets found. Windows is weak in this regard, and you must manage ``PATH`` very carefully as a result.



