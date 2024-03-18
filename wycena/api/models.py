import enum
import typing

import strawberry

from wycena import abstract_models


@strawberry.experimental.pydantic.type(model=abstract_models.Photo, all_fields=True)
class Photo:
    pass


@strawberry.enum
class PropertyType(enum.Enum):
    APARTMENT = "APARTMENT"
    HOUSE = "HOUSE"
    COMMERCIAL = "COMMERCIAL"


@strawberry.experimental.pydantic.type(model=abstract_models.Evaluation)
class Evaluation:
    id: strawberry.auto
    address: strawberry.auto
    costumer: strawberry.auto
    type: PropertyType
    phone_number: strawberry.auto
    price: strawberry.auto
    broker: strawberry.auto
    estimated_value: strawberry.auto
    vision_datetime: strawberry.auto
    photos: typing.List[Photo]
    finished: strawberry.auto
    paid: strawberry.auto
    assigned_to: strawberry.auto
    pdf: strawberry.auto


@strawberry.experimental.pydantic.type(model=abstract_models.Transaction)
class Transaction:
    id: strawberry.auto
    street: strawberry.auto
    building_nr: strawberry.auto
    apartment_nr: strawberry.auto
    city: strawberry.auto
    type: PropertyType
    long: strawberry.auto
    lat: strawberry.auto
    price: strawberry.auto
    area: strawberry.auto
    transaction_date: strawberry.auto
    district: strawberry.auto
    primary_market: strawberry.auto
    floor: strawberry.auto
    number_of_floors: strawberry.auto
    number_of_rooms: strawberry.auto


@strawberry.experimental.pydantic.type(model=abstract_models.Buyer)
class Buyer:
    id: strawberry.auto


@strawberry.experimental.pydantic.type(model=abstract_models.Broker)
class Broker:
    id: strawberry.auto


@strawberry.enum
class QueryFilterType(enum.Enum):
    EQUAL = 'EQUAL'
    GREATER_THAN = 'GREATER_THAN'
    LOWER_THAN = 'LOWER_THAN'
    IN = 'IN'


@strawberry.experimental.pydantic.input(model=abstract_models.QueryFilter)
class QueryFilter:
    value: strawberry.auto
    field_name: strawberry.auto
    filter_type: QueryFilterType


@strawberry.experimental.pydantic.input(model=abstract_models.QueryOptions)
class QueryOptions:
    filters: typing.List[QueryFilter] = None
    offset: strawberry.auto
    sort_by: strawberry.auto
    page_size: strawberry.auto
