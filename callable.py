"""Demonstrate creating a callable object with __call__ method"""


class NameSayer:
    def __init__(self, name):
        self.name = name

    def __call__(self, name=None):
        if name is None:
            name = self.name
        print "Hey %s!" % name


sayer = NameSayer("Fry")
sayer("Bender")  # Prints "Hey Bender!"
sayer()  # Prints "Hey Fry!"
