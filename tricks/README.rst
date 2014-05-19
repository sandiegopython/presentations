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

Comparison operations can be chained in Python.

A traditional comparison between three variables:

.. code-block:: python

    if x < y and y < z:
        print "{} < {} < {}".format(x, y, z)

A chained comparison between three variables:

.. code-block:: python

    if x < y < z:
        print "{} < {} < {}".format(x, y, z)

Less Repetition
~~~~~~~~~~~~~~~

Just compare the following:

.. code-block:: python

    if h == i and i == j and j == k:
        print "h, i, j, and k are equivalent"

    if h == i == j == k:
        print "h, i, j, and k are equivalent"

Less Temporary Variables
~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes expressions are used in comparisons.  Evaluating an expression twice
can be inefficient or may lead to invalid results.

With a temporary variable to store the current time:

.. code-block:: pycon

    >>> from datetime import time, datetime
    >>>
    >>> now = datetime.now().time()
    >>> if time(8, 0) < now and now < time(17, 0):
    ...     print "It's between 8am and 5pm!"
    ...
    It's between 8am and 5pm!

Without the need for a temporary variable:

.. code-block:: pycon

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

`Tuples`_ are immutable iterable objects (like lists that can't be modified).

You can create a tuple by separating values by commas and surrounding them by parenthesis.  Examples:

.. code-block:: pycon

    >>> example_tuple = (1, 2, 3)
    >>> example_tuple
    (1, 2, 3)

You can usually leave off the parenthesis:

.. code-block:: pycon

    >>> example_tuple = 1, 2, 3
    >>> example_tuple
    (1, 2, 3)

An empty pair of parenthesis creates an empty tuple:

.. code-block:: pycon

    >>> empty_tuple = ()
    >>> empty_tuple
    ()

A single-element tuple must have a trailing comma.  Examples:

.. code-block:: pycon

    >>> single_element_tuple = 1,
    >>> single_element_tuple
    (1,)

Unpacking Iterables
~~~~~~~~~~~~~~~~~~~

Tuples, lists, strings, and dictionary are all iterables.

Python supports "multiple assignment" by unpacking iterables.

A basic example of multiple assignment:

.. code-block:: pycon

    >>> a, b, c = example_tuple
    >>> print "{} + {} = {}".format(a, b, c)
    1 + 2 = 3

A more complex example using deeper unpacking:

.. code-block:: pycon

    >>> for (i, (x, y, z)) in enumerate(locations):
    ...     print "p{}: {}, {}, {}".format(i, x, y, z)
    ...
    p0: 1, 2, 3
    p1: 3, 4, 5
    p2: 5, 6, 7

Swapping Variables
~~~~~~~~~~~~~~~~~~

Combining tuple packing with iterable unpacking allows for multiple assignment:

.. code-block:: pycon

    >>> x, y, z = 1, 2, 3

Multiple assignment can be used to swap two variables in a single line of code:

.. code-block:: pycon

    >>> x, y = y, x

Without multiple assignment we would need a temporary variable to swap values:

.. code-block:: pycon

    >>> t = x  # hold old value of x in a temporary variable
    >>> x = y
    >>> y = t


Inline if statements
--------------------

Many languages support a `ternary operator`_ (a.k.a. conditional operator).  Ternary operators are useful for replacing very simple if statements, often making them easier to read.

Traditional Examples
~~~~~~~~~~~~~~~~~~~~

A simple if statement in JavaScript:

.. code-block:: javascript

    var age = 20;
    var ticketType;
    if (age < 18) {
        ticketType = "child";
    } else {
        ticketType = "adult";
    }

Equivalent code abusing short circuit boolean operator logic:

.. code-block:: javascript

    var ticketType = age < 18 && "child" || "adult";

Equivalent code written using a traditional ternary operator:

.. code-block:: javascript

    var ticketType = age < 18 ? "child" : "adult";

That ``?:`` operator is present in C, Perl, Ruby, JavaScript and many other languages.

Python's Inline If
~~~~~~~~~~~~~~~~~~

Python supports inline if statements which work very similarly to the ternary operator.

Here's a simple if statement in Python:

.. code-block:: python

    age = 20
    if age < 18:
        ticket_type = "child"
    else:
        ticket_type = "adult"

Equivalent code abusing short circuit boolean operator logic:

.. code-block:: python

    ticket_type = age < 18 and "child" or "adult"  # Please don't do this

Equivalent code written using an inline if statement:

.. code-block:: python

    ticket_type = "child" if age < 18 else "adult"


.. _Python Shortcuts for the Python Beginner: http://maxburstein.com/blog/python-shortcuts-for-the-python-beginner/
.. _tuples: http://docs.python.org/2/library/functions.html#tuple
.. _ternary operator: https://en.wikipedia.org/wiki/%3F:
