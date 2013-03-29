List Comprehensions
===================

These are list comprehension examples that were demoed during the San Diego
Python Users Group on Mar 28, 2013.  A list of related topics and relevant
links is included at the end of this file.


Example: capitalizing lines in a file
---------------------------------------
You have a list of lines from a file and you want to capitalize the first
letter of every line.

Without List Comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: pycon

    >>> f = open("lorem.txt")
    >>> capitalized_lines = []
    >>> for line in f:
    ...     capitalized_lines.append(line.capitalize())
    ...
    >>> print capitalized_lines
    ['Lorem ipsum\n', 'Dolor sit\n', '\n', 'Consectetur\n', 'Adipiscing\n']


 Alternately using map:

 .. code-block:: pycon

    >>> f = open("lorem.txt")
    >>> capitalized_lines = map(lambda x: x.capitalize(), f)
    >>> print capitalized_lines
    ['Lorem ipsum\n', 'Dolor sit\n', '\n', 'Consectetur\n', 'Adipiscing\n']

With List Comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: pycon

    >>> f = open("lorem.txt")
    >>> capitalized_lines = [line.capitalize() for line in f]
    >>> print capitalized_lines
    ['Lorem ipsum\n', 'Dolor sit\n', '\n', 'Consectetur\n', 'Adipiscing\n']


Example: filtering out empty lines
------------------------------------
You have a list of lines from a file and you want to return only lines that
contain actual stuff (non-whitespace characters).

Without List Comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: pycon

    >>> f = open("lorem.txt")
    >>> non_whitespace_lines = []
    >>> for line in f:
    ...     if line.strip():
    ...         non_whitespace_lines.append(line)
    ...
    >>> print non_whitespace_lines
    ['lorem ipsum\n', 'dolor sit\n', 'consectetur\n', 'adipiscing\n']


 Alternately (using filter):

 .. code-block:: pycon

    >>> f = open("lorem.txt")
    >>> non_whitespace_lines = filter(lambda x: x.strip(), f)
    >>> print non_whitespace_lines
    ['lorem ipsum\n', 'dolor sit\n', 'consectetur\n', 'adipiscing\n']

With List Comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: pycon

    >>> f = open("lorem.txt")
    >>> non_whitespace_lines = [line for line in f if line.strip()]
    >>> print non_whitespace_lines
    ['lorem ipsum\n', 'dolor sit\n', 'consectetur\n', 'adipiscing\n']


Example: filtering a dictionary
---------------------------------
You have a dictionary and you want to filter out empty values.

Without List Comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: pycon

    >>> properties = {
    ...     'name': "John Jaques",
    ...     'phone': "",
    ...     'email': "john@example.com",
    ... }
    >>> non_empty = {}
    >>> for k, v in properties.items():
    ...     if v:
    ...         non_empty[k] = v
    ...
    >>> print non_empty
    {'name': 'John Jaques', 'email': 'john@example.com'}

With List Comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: pycon

    >>> properties = {
    ...     'name': "John Jaques",
    ...     'phone': "",
    ...     'email': "john@example.com",
    ... }
    >>> non_empty = dict([(k, v) for k, v in properties.items() if v])
    >>> print non_empty
    {'name': 'John Jaques', 'email': 'john@example.com'}


Example: find average distance between points
---------------------------------------------
You have two lists of points (X-Y coordinates) which are pairs of start points
and end points.  The first start point coresponds with the first end point, the
second to the second, and so on.  You want to calculate the average distance
between coresponding points.

Without List Comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: pycon

    >>> from math import sqrt
    >>> total_distance = 0
    >>> starts = [(6, 4), (9, 7), (4, 7), (9, 9)]
    >>> ends = [(8, 6), (9, 5), (2, 7), (3, 2)]
    >>> for i in range(len(starts)):
    ...     u, v = starts[i]
    ...     x, y = ends[i]
    ...     total_distance += sqrt((u - x) ** 2 + (v - y) ** 2)
    ...
    >>> average_distance = total_distance / len(starts)
    >>> print average_distance
    4.01199289551

Alternately:

.. code-block:: pycon

    >>> from math import sqrt
    >>> total_distance = 0
    >>> starts = [(6, 4), (9, 7), (4, 7), (9, 9)]
    >>> ends = [(8, 6), (9, 5), (2, 7), (3, 2)]
    >>> for (u, v), (x, y) in zip(starts, ends):
    ...     total_distance += sqrt((u - x) ** 2 + (v - y) ** 2)
    ...
    >>> average_distance = total_distance / len(starts)
    >>> print average_distance
    4.01199289551

With List Comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: pycon

    >>> from math import sqrt
    >>> starts = [(6, 4), (9, 7), (4, 7), (9, 9)]
    >>> ends = [(8, 6), (9, 5), (2, 7), (3, 2)]
    >>> differences = [((u - x), (v - y)) for (u, v), (x, y) in zip(starts, ends)]
    >>> distances = [sqrt(x * x + y * y) for x, y in differences]
    >>> average_distance = sum(distances) / len(starts)
    >>> print average_distance
    4.01199289551

Alternately:

.. code-block:: pycon

    >>> from math import sqrt
    >>> starts = [(6, 4), (9, 7), (4, 7), (9, 9)]
    >>> ends = [(8, 6), (9, 5), (2, 7), (3, 2)]
    >>> distances = [sqrt((u - x) ** 2 + (v - y) ** 2)
    ...             for (u, v), (x, y) in zip(starts, ends)]
    >>> average_distance = sum(distances) / len(starts)
    >>> print average_distance
    4.01199289551


References
----------

Below are links to resources referenced in the talk.

- `Code Like a Pythonista: List comprehensions & Generator Expressions`_
- `Look Like a Native`_
- `Iterables, Iterators, and Generators: Part 1`_
- `Expanding, Unpacking, or Splatting`_

.. _Code Like a Pythonista\: List comprehensions & Generator Expressions: http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#list-comprehensions
.. _Expanding, Unpacking, or Splatting: http://pynash.org/2013/03/13/unpacking.html
.. _Look Like a Native: http://nedbatchelder.com/text/iter.html
.. _Iterables, Iterators, and Generators\: Part 1: http://excess.org/article/2013/02/itergen1/
