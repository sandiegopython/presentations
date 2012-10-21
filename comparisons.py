"""
Demonstrate usage of magic comparison methods

Methods used:
    * ``__eq__``: used for ``==`` (returns True iff equal to given object)
    * ``__ne__``: used for ``!=`` (returns True iff not equal to given object)
    * ``__lt__``: used for ``<`` (returns True iff less than given object)
    * ``__gt__``: used for ``>`` (returns True iff greater than given object)
    * ``__le__``: used for ``<=``
    * ``__gt__``: used for ``>=``
    * ``__cmp__``: used for all comparison operators at once
"""


class Doppelganger:
    """An object which is "equal" to everything"""
    def __eq__(self, other):
        return True

ditto = Doppelganger()
assert(ditto == 42)
assert(ditto == [1, 2])
assert(ditto == True)
assert(ditto == False)
assert(ditto == None)


class CheeseGreater:
    """An object which is "greater than" everything"""
    def __gt__(self, other):
        return True

grater = CheeseGreater()
assert(grater > 4)
assert(grater > {'a': 1})
assert(grater > None)


class Vaccuum:
    """An object which always evaluates as "zero" or "empty\""""
    def __nonzero__(self):
        return False

hoover = Vaccuum()
assert(not hoover)
assert(bool(hoover) is False)


class Contrarian:

    """An object which returns "False" for any comparison"""

    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return False

    def __lt__(self, other):
        return False

    def __gt__(self, other):
        return False

    def __le__(self, other):
        return False

    def __ge__(self, other):
        return False

two_year_old = Contrarian()
assert(not two_year_old != 2)
assert(not two_year_old == 2)
assert(not two_year_old < 2)
assert(not two_year_old > 2)
assert(not two_year_old <= 2)
assert(not two_year_old >= 2)
assert(not two_year_old == two_year_old)


class Event:

    """An event which can be ordered by date and place name alphabetically"""

    def __init__(self, date, place):
        self.date = date
        self.place = place

    def __cmp__(self, other):
        return cmp(self.date, other.date) or cmp(self.place, other.place)


from datetime import date
party1 = Event(date(2012, 10, 30), "Bill's pre-Halloween party")
party2 = Event(date(2012, 10, 31), "Meg's Halloween party")
party3 = Event(date(2012, 10, 31), "Sam's Halloween party")
assert(party1 < party2)
assert(party2 < party3)
assert(party1 < party2 < party3)
