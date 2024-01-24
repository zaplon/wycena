import datetime
import typing

from pydantic import BaseModel

from wycena.models.enums import PropertyType


class Photo(BaseModel):
    url: str
    description: str
    datetime: datetime.datetime


class Evaluation(BaseModel):
    address: str
    type: PropertyType
    buyer: str
    phone_number: str
    price: float
    provider: str
    estimated_value: float = None
    vision_datetime: datetime.datetime = None
    photos: typing.List[Photo]
    finished: bool = False
    paid: bool = False
    assigned_to: str = None
    pdf: str = None
