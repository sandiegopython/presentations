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
    ['Lorem ipsum dolor sit amet,\n', 'Consectetur adipiscing elit.\n', '\n', 'Donec a diam lectus.\n', 'Sed sit amet ipsum mauris.\n']

With List Comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: pycon

    >>> f = open("lorem.txt")
    >>> capitalized_lines = [line.capitalize() for line in f]
    >>> print capitalized_lines
    ['Lorem ipsum dolor sit amet,\n', 'Consectetur adipiscing elit.\n', '\n', 'Donec a diam lectus.\n', 'Sed sit amet ipsum mauris.\n']


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
    ['lorem ipsum dolor sit amet,\n', 'consectetur adipiscing elit.\n', 'donec a diam lectus.\n', 'sed sit amet ipsum mauris.\n']

With List Comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: pycon

    >>> f = open("lorem.txt")
    >>> non_whitespace_lines = [line for line in f if line.strip()]
    >>> print non_whitespace_lines
    ['lorem ipsum dolor sit amet,\n', 'consectetur adipiscing elit.\n', 'donec a diam lectus.\n', 'sed sit amet ipsum mauris.\n']


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
