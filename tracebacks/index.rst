Reading Python Tracebacks
=========================

By Trey Hunner


Say we have some code
---------------------

It's a command-line tool for generating random names:

.. code-block:: bash

    $ names
    Jack Hill
    $ names
    Robert Zwilling
    $ names
    Mignon Gulke
    $ names
    Donna Walton
    $ names
    Elena Cameron


And it's broken
---------------

.. code-block:: bash

    $ names
    Traceback (most recent call last):
    File "/home/trey/.virtualenvs/names/bin/names", line 9, in <module>
        load_entry_point('names==0.3.0.post1', 'console_scripts', 'names')()
    File "/home/trey/repos/python/names/names/main.py", line 6, in main
        print(get_full_name())
    File "/home/trey/repos/python/names/names/__init__.py", line 43, in get_full_name
        return "{0} {1}".format(get_first_name(gender), get_last_name())
    File "/home/trey/repos/python/names/names/__init__.py", line 35, in get_first_name
        return get_name(FILES['first:%s' % gender]).capitalize()
    File "/home/trey/repos/python/names/names/__init__.py", line 23, in get_name
        selected = random() * 90
    TypeError: 'module' object is not callable

.. rst-class:: build

Now we need to learn about tracebacks.


Read from the bottom-up
-----------------------

The last line in the traceback is the most important.

.. code-block:: bash

    $ names
    ...
    TypeError: 'module' object is not callable

This last line is in the format::

    ExceptionClass: a descriptive message that might be helpful

.. note::

    The last line tells us the exception that was raised and any message included with the exception that might give us a hint as to what went wrong.

    This line tells us the exception class that was raised and often gives us a message with specifics about the error that occurred.


Call Stack
----------

All the other lines in the traceback represent the call stack.

The call stack works like this:

- When entering a function: push a frame onto the stack
- When exiting a function: pop a frame off of the stack
- Each frame records the currently executing code

.. note::

    To understand the rest of the traceback, we need to understand the call stack.  Here's a quick explanation.


A Visual Demonstration
----------------------

.. figure:: /_static/call_stack.png

.. note::

    The process of building up the stack requires us to trace through our code in the same way the Python runtime would.


Most Recent Call Last
---------------------

Let's look at the first line in our traceback::

    Traceback (most recent call last):

This means the last line of the traceback represents the most recent stack frame in our call stack (the function we're in right now).

.. note::

    Basically this means we should read the stack trace from the bottom-up also.


Reading the call stack
----------------------

.. code-block:: bash

    $ names
    Traceback (most recent call last):
    File "/home/trey/.virtualenvs/names/bin/names", line 9, in <module>
        load_entry_point('names==0.3.0.post1', 'console_scripts', 'names')()
    File "/home/trey/repos/python/names/names/main.py", line 6, in main
        print(get_full_name())
    File "/home/trey/repos/python/names/names/__init__.py", line 43, in get_full_name
        return "{0} {1}".format(get_first_name(gender), get_last_name())
    File "/home/trey/repos/python/names/names/__init__.py", line 35, in get_first_name
        return get_name(FILES['first:%s' % gender]).capitalize()
    File "/home/trey/repos/python/names/names/__init__.py", line 23, in get_name
        selected = random() * 90
    TypeError: 'module' object is not callable

Let's translate this into English

.. note::

    In english:

    1. Our exception is ``TypeError`` and the error was ``'module' object is not callable``
    2. We're currently in the ``get_name`` function in our ``names/__init__.py`` module on **line 23**
    3. The function that called ``get_name`` was ``get_first_name`` in the same module on **line 35**
    4. That was called from ``get_full_name`` on **line 43**
    5. That was called from ``main`` on **line 6**
    6. That was called from some ``bin/names`` file in our virtualenv directory on **line 9**

    So the second-to-last lines in the traceback looks like it's probably where our problem lies.  That's line 23 on our __init__.py file.


Identifying the Problem
-----------------------

.. code-block:: python

    from __future__ import unicode_literals
    from os.path import abspath, join, dirname
    import random

    # ...

    def get_name(filename):
        selected = random() * 90  # Here's the problem line
        with open(filename) as name_file:
            for line in name_file:
                name, _, cummulative, _ = line.split()
                if float(cummulative) > selected:
                    return name
        return ""

It looks like we're called the ``random`` module instead of the ``random.random`` function.


Solving the Problem
-------------------

.. code-block:: python

    from __future__ import unicode_literals
    from os.path import abspath, join, dirname
    import random

    # ...

    def get_name(filename):
        selected = random.random() * 90  # We fixed it
        with open(filename) as name_file:
            for line in name_file:
                name, _, cummulative, _ = line.split()
                if float(cummulative) > selected:
                    return name
        return ""

In Summary
----------

- The last line of the traceback tells the exception that was raised
- The rest of the lines in our traceback show us the current state of our call stack
- In general, the last couple lines of the traceback are the most important
- **Read tracebacks from the bottom-up**
