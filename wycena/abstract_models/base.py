import typing

from pydantic import BaseModel

from .enums import QueryFilterType
from wycena.settings import settings


class AddressMixin:
    street: str
    building_nr: str
    apartment_nr: typing.Optional[int] = None
    city: str


class QueryFilter(BaseModel):
    field_name: str
    filter_type: QueryFilterType
    value: str


class QueryOptions(BaseModel):
    filters: typing.List[QueryFilter] = None
    sort_by: typing.Optional[str] = None
    offset: typing.Optional[int] = None
    page_size: typing.Optional[int] = settings.API_PAGE_SIZE
