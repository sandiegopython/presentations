import factory
from factory import fuzzy

from fbp.people import models


# Long form way to create a factory
# Allows for the most control
class StreetFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Street

    name = fuzzy.FuzzyText(length=30)
    postal_code = factory.Sequence(lambda x: '{:05d}'.format(x))


# Simple cases can be built with the make_factory call, assuming you don't need
# anything special for post-generation. Personally I tend to prefer actual
# classes, but there's nothing wrong with make_factory
CityFactory = factory.make_factory(models.City,
                                   FACTORY_CLASS=factory.DjangoModelFactory,
                                   name=fuzzy.FuzzyText(length=25))


class AddressFactory(factory.DjangoModelFactory):
    STATES = ('CA', 'MA', 'MN', 'TX', 'TN', 'WA', 'OR')

    class Meta:
        model = models.Address
        # If it's not part of your model, make sure you exlucde it!
        exclude = ('STATES',)

    street = factory.SubFactory(StreetFactory)
    city = factory.SubFactory(CityFactory)
    state = factory.Iterator(STATES)


class PersonFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Person

    address = factory.SubFactory(AddressFactory)
    name = fuzzy.FuzzyText(length=12)
