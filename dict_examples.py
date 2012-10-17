"""
Demonstrate examples of some magic methods using a dict object

Methods used:
* ``__str__``: method called by str function
* ``__getitem__``: method called by [] operator
* ``__getattribute__``: method called by getattr function
* ``__setitem__``: method called by [] operator used for assignment
* ``__doc__``: variable/attribute automatically assigned to docstring value
* ``__name__``: assigned to module name ("__main__" when run standalone)
"""

d = {'test key': 'test value'}

assert(str(d) == d.__str__())

assert(d['test key'] == d.__getitem__('test key'))

assert(d.keys() == ['test key'])
assert(d.keys == getattr(d, 'keys'))
assert(getattr(d, 'keys') == d.__getattribute__('keys'))

d.__setitem__('another key', 'another value')
assert(d['another key'] == 'another value')

def test_function():
    """Print hello!"""
    print "hello!"
assert(test_function.__doc__ == "Print hello!")

assert(__doc__[:29] == "\nDemonstrate examples of some")

assert(__name__ == "__main__")
