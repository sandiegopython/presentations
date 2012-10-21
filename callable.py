"""Demonstrate creating a callable object with ``__call__`` method"""


class NameSayer:

    """An object which can be called just like a function"""

    def __init__(self, name):
        self.name = name

    def __call__(self, name=None):
        if name is None:
            name = self.name
        print "Hey %s!" % name


sayer = NameSayer("Fry")
sayer.__call__("Bender")  # Prints "Hey Bender!"
sayer.__call__()  # Prints "Hey Fry!"
sayer("Bender")  # Prints "Hey Bender!"
sayer()  # Prints "Hey Fry!"
