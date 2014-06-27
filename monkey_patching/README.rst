Introduction to Monkey Patching
===============================

Monkey patching: modifying or extending code at runtime

Let's walk through some examples.

Capturing Standard Output
-------------------------

What if we want the print statement to be captured to a variable or file instead of printing to the screen?  Can we do that?

Let's try replacing ``sys.stdout`` so print doesn't output to the screen.

.. code-block:: pycon

    >>> import sys
    >>> from StringIO import StringIO
    >>>
    >>> real_stdout = sys.stdout
    >>> sys.stdout = StringIO()
    >>>
    >>> print "hello"
    >>> print "where is this output going?"
    >>>
    >>> real_stdout.write(sys.stdout.getvalue())
    hello
    where is this output going?
    >>>
    >>> sys.stdout = real_stdout
    >>>
    >>> print "is this printing out?"
    is this printing out?
    >>> print "yes it is!"
    yes it is!

What if we replace ``sys.stdout`` with something that's not a file-like object?

.. code-block::  pycon

    >>> import sys
    >>> sys.stdout = None
    >>> print "hello!"
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      AttributeError: 'NoneType' object has no attribute 'write'

Let's make a context manager to capture standard output and save it to a file!

.. code-block:: pycon

    >>> from iopatch import print_to_file
    >>>
    >>> with print_to_file('test.txt'):
    ...     print "hello!"
    ...
    >>> with open('test.txt') as f:
    ...     print f.read()
    hello!

    >>>

You can check out the implementation in the ``iopatch`` module.
