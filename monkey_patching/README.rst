
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
