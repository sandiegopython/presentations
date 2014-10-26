patch from unittest.mock
========================

By Trey Hunner

Examples of different ways to use the ``patch`` function from the ``unittest.mock`` library (Python 3.3+).  You can install `mock`_ for Python 2 support.

Files:

1. `utils.py`_: contains ``day_of_week`` function
2. `test_with_context_manager.py`_: tests written using context manager version of ``patch`` function
3. `test_with_decorators.py`_: tests written using method-level decorators
4. `test_with_class_decorators.py`_: tests written using class-level decorator
5. `test_manually.py`_: tests written by calling ``start`` and ``stop`` manually

.. _utils.py: utils.py
.. _test_with_context_manager.py: test_with_context_manager.py
.. _test_with_decorators.py: test_with_decorators.py
.. _test_with_class_decorators.py: test_with_class_decorators.py
.. _test_manually.py: test_manually.py
.. _mock: https://pypi.python.org/pypi/mock
