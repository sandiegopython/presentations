from django.test import TestCase

from fbp.people import models


class TestPerson(TestCase):
    def test_creation(self):
        st = models.Street.objects.create(name='Street', postal_code='12345')
        city = models.City.objects.create(name='Somewhere')
        p = models.Person.objects.create(name='blarg',
                  address=models.Address.objects.create(
                      street=st,
                      city=city,
                      state='CA'))
        assert p.pk

    def test_lots_of_people(self):
        st = models.Street.objects.create(name='Street', postal_code='12345')
        city = models.City.objects.create(name='Somewhere')
        for _ in xrange(32):
            p = models.Person.objects.create(name='blarg',
                    address=models.Address.objects.create(
                        street=st,
                        city=city,
                        state='CA'))
        assert models.Person.objects.all().count() == 32
