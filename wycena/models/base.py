import typing

from pydantic import BaseModel

from wycena.models.enums import QueryFilterType
from wycena.settings import settings


class AddressMixin:
    street: str
    building_nr: str
    apartment_nr: int = None
    city: str


class QueryFilter(BaseModel):
    field_name: str
    filter_type: QueryFilterType
    value: str


class QueryOptions(BaseModel):
    filters: typing.List[QueryFilter] = None
    sortBy: str = None
    last_key: str = None
    pageSize: int = settings.API_PAGE_SIZE
