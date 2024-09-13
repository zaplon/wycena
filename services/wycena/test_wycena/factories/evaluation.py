import random

import factory
from factory.alchemy import SQLAlchemyModelFactory

from wycena.db import models


class PhotoFactory(SQLAlchemyModelFactory):
    class Meta:
        model = models.Photo
        sqlalchemy_session_persistence = "commit"

    url = factory.Faker('image_url')
    description = factory.Faker('sentence')
    datetime = factory.Faker('date_time_this_year')


class EvaluationFactory(SQLAlchemyModelFactory):
    class Meta:
        model = models.Evaluation
        sqlalchemy_session_persistence = "commit"

    address = factory.Faker('address')
    type = "APARTMENT"
    price = factory.Faker('pyfloat', min_value=500, max_value=1500)
    estimated_value = factory.Faker('pyfloat', min_value=500000, max_value=2000000)
    broker = factory.Faker('name')
    phone_number = factory.Faker('phone_number')
    vision_datetime = factory.Faker('date_time_this_year')
    photos = factory.LazyFunction(lambda: PhotoFactory.create_batch(random.randint(2, 10)))
