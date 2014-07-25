from django.test import TestCase

import factory
import pytest

from fbp.people import models

from . import factories


class TestPerson(TestCase):
    def test_create_person(self):
        factories.PersonFactory(name='Bob')
        assert models.Person.objects.filter(name='Bob').count() == 1

    def test_LOTS_OF_PEOPLE(self):
        factories.PersonFactory.create_batch(size=32)
        assert models.Person.objects.all().count() == 32


class TestFactories(object):
    # Get me all the Factory classes from my factories module
    # with a bit of name and type checking thrown in.
    FACTORIES = [getattr(factories, f)
                 for f in dir(factories)
                 if 'Factory' in f
                    and issubclass(getattr(factories, f),
                                   factory.DjangoModelFactory)]

    @staticmethod
    @pytest.mark.django_db
    def check_basic_creation(my_factory):
        my_factory()
        assert my_factory._meta.model.objects.all().count() == 1

    def test_default_creation(self):
        for my_factory in self.FACTORIES:
            yield self.check_basic_creation, my_factory
