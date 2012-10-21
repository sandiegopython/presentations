"""Demonstrate making a context manager using ``__enter__`` and ``__exit__``"""


class FakeDatabaseConnection:

    """A fake database connection that can be opened and closed"""

    def __init__(self, name):
        self.name = name

    def open(self):
        print "Connecting to database %s" % self.name

    def close(self):
        print "Closing database %s" % self.name


class connect:

    """Context manager that handles database open/close on enter/exit"""

    def __init__(self, name):
        self.connection = FakeDatabaseConnection(name)

    def __enter__(self):
        self.connection.open()
        return self.connection

    def __exit__(self, exception_type, exception_value, traceback):
        if exception_type is not None:
            print "Uh oh:  %s" % exception_value
        self.connection.close()


# This should print:
#   Connecting to database my_favorite_db
#   Doing stuff with my_favorite_db now...
#   Closing database my_favorite_db
with connect('my_favorite_db') as db:
    print "Doing stuff with %s now..." % db.name

# This should print:
#   Connecting to database my_other_favorite_db
#   Uh oh:  FakeDatabaseConnection instance has no attribute 'undefined_method'
#   Closing database my_other_favorite_db
with connect('my_other_favorite_db') as db:
    db.undefined_method()
