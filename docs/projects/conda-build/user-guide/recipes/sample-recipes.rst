==============
Sample recipes
==============

Conda offers you the flexibility of being able to build things
that are not Python related. The first 2 sample recipes,
``boost`` and ``libtiff``, are examples of non-Python libraries, meaning
they do not require Python to run or build.

* `boost <https://github.com/conda/conda-recipes/tree/main/boost>`_ is an example
  of a popular programming library and illustrates the use of selectors in a recipe.

* `libtiff <https://github.com/conda/conda-recipes/tree/main/libtiff>`_ is
  another example of a compiled library, which shows how conda can apply patches to source directories before building the package.

* `msgpack <https://github.com/conda/conda-recipes/tree/main/python/msgpack>`_,
  `blosc <https://github.com/conda/conda-recipes/tree/main/python/blosc>`_, and
  `cytoolz <https://github.com/conda/conda-recipes/tree/main/python/cytoolz>`_
  are examples of Python libraries with extensions.

* `toolz <https://github.com/conda/conda-recipes/tree/main/python/toolz>`_,
  `sympy <https://github.com/conda/conda-recipes/tree/main/python/sympy>`_,
  `six <https://github.com/conda/conda-recipes/tree/main/python/six>`_, and
  `gensim <https://github.com/conda/conda-recipes/tree/main/python/gensim>`_ are
  examples of Python-only libraries.

``gensim`` works on Python 2, and all of the others work on both Python 2 and Python 3.
