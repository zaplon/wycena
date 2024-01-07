import factory

from wycena import models


class TransactionFactory(factory.Factory):
    class Meta:
        model = models.Transaction

    address = factory.Faker('address')
    price = factory.Faker('pyfloat', min_value=500, max_value=1500)
    long = factory.Faker('pyfloat', min_value=50, max_value=55)
    lat = factory.Faker('pyfloat', min_value=20, max_value=25)
    city = factory.Faker('city')
