import pdb ; pdb.set_trace()
============================

The file ``pdb_demo.py`` is an interactive demonstration of pdb usage.  The
demo will teach you how to use some of the pdb commands shown below.  To try
out this demo run it in your Python interpreter::

    python pdb_demo.py

This talk started with a demonstration of using pdb to locate a bug in a Django
model method.  A re-enactment of the demonstration is `available on ascii.io`_.

.. _available on ascii.io: http://ascii.io/a/1974

PDB Commands
------------
Below are the pdb commands I usually use.  The characters in parenthesis are
optional (so ``n`` and ``next`` to the same thing):

- s(tep)
- n(ext)
- c(ontinue)
- l(ist)
- r(eturn)

Here are some more useful commands:

- a(rgs)
- pp: pretty print
- (q)uit
- (b)reak


Introspection
-------------

Some functions that are generally useful for introspecting Python code:

- `dir`_
- `locals`_
- `globals`_

.. _dir: http://docs.python.org/2/library/functions.html#dir
.. _locals: http://docs.python.org/2/library/functions.html#locals
.. _globals: http://docs.python.org/2/library/functions.html#globals


Alternative Debuggers
---------------------

Some IDEs (PyCharm for example) have built-in Python debuggers that you can
use.  For more information on alternative debuggers and debugging in your IDE,
check out the `Python Debugging Tools`_ link below.


More Resources
--------------
- `PDB Documentation`_
- `Python Debugging with PDB`_
- `Python Debugging Tools`_


.. _PDB Documentation: file:///etc/laptop-mode 
.. _Python Debugging with PDB: http://marakana.com/s/post/423/tutorial_python_debugging_with_pdb
.. _Python Debugging Tools: http://wiki.python.org/moin/PythonDebuggingTools
