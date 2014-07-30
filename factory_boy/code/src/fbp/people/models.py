from django.db import models


# And now for a highly contrived example
# Please don't ever define your addresses this way.
class Street(models.Model):
    name = models.CharField(max_length=128)
    postal_code = models.CharField(max_length=10)

    class Meta:
        unique_together = (('name', 'postal_code'),)


class City(models.Model):
    name = models.CharField(max_length=32)


class Address(models.Model):
    street = models.ForeignKey(Street)
    city = models.ForeignKey(City)
    state = models.CharField(max_length=2)

    @property
    def postal_code(self):
        return self.street.postal_code


class Person(models.Model):
    name = models.CharField(max_length=128)
    address = models.ForeignKey(Address)
