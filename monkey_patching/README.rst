Introduction to Monkey Patching
===============================

By Trey Hunner

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


Mock
----

`Mock`_ is a cool tool that can help you monkey patch things.

When writing a test for our ``day_of_week`` function, we probably want to make sure it always returns the correct date in a variety of situations (not just for today's date).

Let's force the ``today`` method on the ``date`` class in our ``utils`` module to return June 22, 2014 all the time.

.. code-block:: pycon

    >>> from mock import patch
    >>> from datetime import date
    >>>
    >>> from utils import day_of_week
    >>>
    >>> with patch('utils.date') as fake_date:
    ...     fake_date.today.return_value = date(2014, 6, 22)
    ...     print day_of_week()  # Should print Sunday
    ...
    Sunday
    >>> print day_of_week()  # Should print today's day of week
    Thursday


Warning!
--------

Changing code at runtime may be dangerous.  Monkey patching can sometimes help a lot while testing, but use it in production code only with extreme caution.
