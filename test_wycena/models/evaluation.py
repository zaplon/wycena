import random

import factory

from wycena import models


class PhotoFactory(factory.Factory):
    class Meta:
        model = models.Photo

    url = factory.Faker('image_url')
    description = factory.Faker('sentence')
    datetime = factory.Faker('date_time_this_year')


class EvaluationFactory(factory.Factory):
    class Meta:
        model = models.Evaluation

    address = factory.Faker('address')
    type = "APARTMENT"
    price = factory.Faker('pyfloat', min_value=500, max_value=1500)
    estimated_value = factory.Faker('pyfloat', min_value=500000, max_value=2000000)
    provider = factory.Faker('name')
    phone_number = factory.Faker('phone_number')
    vision_datetime = factory.Faker('date_time_this_year')
    photos = factory.LazyFunction(lambda: PhotoFactory.create_batch(random.randint(2, 10)))
