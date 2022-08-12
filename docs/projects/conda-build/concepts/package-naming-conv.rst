==========================
Package naming conventions
==========================

To facilitate communication and documentation, conda observes the
package naming conventions listed below.

.. _package_name:
.. index::
    pair: terminology; package name
    seealso: name; package name

Package name
============

The name of a package, without any reference to a particular
version. Conda package names are normalized and they may contain
only lowercase alpha characters, numeric digits, underscores,
hyphens, or dots. In usage documentation, these are referred to
by ``package_name``.

.. _package_version:
.. index::
    pair: terminology; package version
    seealso: name; package version

Package version
===============

A version number or string, often similar to ``X.Y`` or
``X.Y.Z``, but it may take other forms as well.

.. _build_string:
.. index::
    pair: terminology; build string
    seealso: name; build string

Build string
============

An arbitrary string that identifies a particular build of a
package for conda.  It may contain suggestive mnemonics, but
these are subject to change, and you should not rely on it or try
to parse it for any specific information.

.. _canonical_name:
.. index::
    pair: terminology; canonical name
    seealso: name; canonical name

Canonical name
==============

The package name, version, and build string joined together by
hyphens---name-version-buildstring. In usage documentation, these
are referred to by ``canonical_name``.

.. _filename:
.. index::
    pair: terminology; filename

Filename
========

Conda package filenames are canonical names, plus the suffix
``.tar.bz2`` or ``.conda``.

The following figure compares a canonical name to a filename:

.. figure:: ../img/conda_names.png
   :align:  center

   Conda package naming

|

Conda supports both ``.conda`` and ``.tar.bz2`` package extensions. The ``.conda``
format is generally smaller and more efficient than ``.tar.bz2`` packages.
Read our `blog post <https://www.anaconda.com/understanding-and-improving-condas-performance/>`_
about it to learn more.

The build string is created as the package is built. Things that
contribute to it are the variants specified either by the command
line or the configuration from the ``conda_build_config.yaml``, and the
build number in the recipe. If there are no variants,
then the build string is the build number that is specified in the recipe.

.. _package_spec:
.. index::
    pair: terminology; package specification
    seealso: package spec; package specification

Package specification
=====================

A package name together with a package version---which may be
partial or absent---joined by an equal sign.

EXAMPLES:

* ``python=2.7.3``
* ``python=2.7``
* ``python``

In usage documentation, these are referred to by ``package_spec``.
