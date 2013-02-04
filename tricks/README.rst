Python Tricks
=============

This talk is about interesting Python syntactic sugar and built-in functions.

Most of these features:

1. Aren't taught in introductory tutorials
2. Use syntax that is different than some similar languages
3. Sometimes make code easier to understand


Inspiration
-----------

This talk was heavily inspired by Max Burstein's article
`Python Shortcuts for the Python Beginner`_.


Chained Comparisons
-------------------

Comparison operations can be chained in Python.  This means the following are equivalent::

    if x < y and y < z:
        print "{0} < {1} < {2}".format(x, y, z)
    if x < y < z:
        print "{0} < {1} < {2}".format(x, y, z)

Less Repetition
~~~~~~~~~~~~~~~

Just compare the following::

    if h == i and i == j and j == k:
        print "h, i, j, and k are equivalent"
    if h == i == j == k:
        print "h, i, j, and k are equivalent"

Less Temporary Variables
~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes expressions are used in comparisons.  Evaluating an expression twice can be inefficient or may lead to invalid results.

With a temporary variable to store the current time::

    >>> from datetime import time, datetime
    >>>
    >>> now = datetime.now().time()
    >>> if time(8, 0) < now and now < time(17, 0):
    ...     print "It's between 8am and 5pm!"
    ...
    It's between 8am and 5pm!

Without the need for a temporary variable::

    >>> from datetime import time, datetime
    >>>
    >>> if time(8, 0) < datetime.now().time() < time(17, 0):
    ...     print "It's between 8am and 5pm!"
    ...
    It's between 8am and 5pm!


Automatic Tuple Unpacking
-------------------------

Tuple Review
~~~~~~~~~~~~

`Tuples`_ are immutable iterable objects (like lists but they can't be modified).

Tuples can be created by separating values by commas and optionally surrounding them by parenthesis.  Examples::

    >>> a_tuple = 1, 2, 3
    >>> a_tuple
    (1, 2, 3)

Empty tuples can be created by an empty pair of parenthesis.  A single-element tuple must have a trailing comma.  Examples::

    >>> empty_tuple = ()
    >>> empty_tuple
    ()
    >>> single_element_tuple = 1,
    >>> single_element_tuple
    (1,)

Unpacking Iterables
~~~~~~~~~~~~~~~~~~~

Tuples, lists, strings, and dicts are all iterables.  All iterables can be automatically unpacked allowing for "multiple assignment".  Here's two examples of multiple assignment::

    >>> a, b, c = a_tuple
    >>> print "{0} + {1} = {2}".format(a, b, c)
    1 + 2 = 3
    >>>
    >>> for x, y in [(1, 2), (3, 4), (5, 6)]:
    ...     print "{0} < {1}".format(x, y)
    ...
    1 < 2
    3 < 4
    5 < 6

Swapping Variables
~~~~~~~~~~~~~~~~~~

Multiple assignment can be used to swap two variables in a single line of code.

Traditional way to swap ``x`` and ``y``::

    >>> t = x  # hold old value of x in a temporary variable
    >>> x = y
    >>> y = t

Pythonic way using multiple assignment::

    >>> x, y = y, x


Inline if statements
--------------------

Many languages support a `terenary operator`_ (a.k.a. conditional operator, inline if).  Terenary operators are useful for replacing very simple if statements, often making them easier to read.

Traditional Examples
~~~~~~~~~~~~~~~~~~~

A simple if statement in a C-like language::

    if (something()) {
        x = "something";
    } else {
        x = "nothing";
    }

Equivalent code abusing short circuit boolean operator logic

    x = something() && "something" || "nothing";

Equivalent code written using a traditional ternary operator::

    x = something() ? "something" : "nothing";

That ?: operator is in C, Perl, Ruby, JavaScript and many other languages.

Python's Inline If
~~~~~~~~~~~~~~~~~~

Python's supports inline if statements which work very similarly to the ternary operator.

This is more wordy than it needs to be::

    if something():
        x = "something"
    else:
        x = "nothing"

Equivalent code abusing short circuit boolean operator logic::

    x = something() and "something" or "nothing"  # Please DON'T do this

Equivalent code written using an inline if statement::

    x = "something" if something() else "nothing"



.. _Python Shortcuts for the Python Beginner: http://maxburstein.com/blog/python-shortcuts-for-the-python-beginner/
.. _tuples: http://docs.python.org/2/library/functions.html#tuple
.. _ternary operator: https://en.wikipedia.org/wiki/%3F:
