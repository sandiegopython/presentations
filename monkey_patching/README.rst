
.. code-block:: pycon

    >>> import sys
    >>> from StringIO import StringIO
    >>>
    >>> sys.stdout = StringIO()
    >>>
    >>> print "hello"
    >>> print "where is output this going?"
    >>>
    >>> sys.stdout = sys.__stdout__
    >>>
    >>> print "is this printing out?"
    >>> print "yes it is!"
