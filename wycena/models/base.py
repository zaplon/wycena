import typing

from pydantic import BaseModel

from wycena.models.enums import QueryFilterType
from wycena.settings import settings


class AddressMixin:
    street: str
    building_number: str
    apartment_nr: str = None
    city: str


class QueryFilter(BaseModel):
    field_name: str
    filter_type: QueryFilterType
    value: str


class QueryOptions(BaseModel):
    filters: typing.List[QueryFilter] = None
    sortBy: str = None
    page: int = None
    pageSize: int = settings.API_PAGE_SIZE


class BaseDBModel(BaseModel):
    def filter(self, options: QueryOptions):
        raise NotImplemented
