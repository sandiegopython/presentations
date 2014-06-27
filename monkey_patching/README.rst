
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
