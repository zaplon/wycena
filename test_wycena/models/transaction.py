import uuid

import factory
from factory.fuzzy import FuzzyChoice

from wycena import models
from wycena.models import PropertyType


class TransactionFactory(factory.Factory):
    class Meta:
        model = models.Transaction

    id = factory.lazy_attribute(lambda x: uuid.uuid4())
    type = FuzzyChoice(PropertyType)
    primary_market = factory.Faker('pybool')
    price = factory.Faker('pyint', min_value=500, max_value=1500)
    long = factory.Faker('pyfloat', min_value=50, max_value=55)
    lat = factory.Faker('pyfloat', min_value=20, max_value=25)
    area = factory.Faker('pyfloat', min_value=30, max_value=200)
    transaction_date = factory.Faker('date_this_year')
    floor = factory.Faker('pyint', min_value=1, max_value=15)
    number_of_floors = factory.Faker('pyint', min_value=1, max_value=15)
    number_of_rooms = factory.Faker('pyint', min_value=1, max_value=6)
    city = factory.Faker('city')
    street = factory.Faker('street_name')
    apartment_nr = factory.Faker('pyint', min_value=1, max_value=100)
    building_nr = factory.Faker('building_number')
