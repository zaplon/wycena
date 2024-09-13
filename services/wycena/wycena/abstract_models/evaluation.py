import datetime
import uuid

from pydantic import BaseModel

from .enums import PropertyType


class Photo(BaseModel):
    url: str
    description: str
    datetime: datetime.datetime


class Evaluation(BaseModel):
    id: uuid.UUID
    address: str
    type: PropertyType
    price: float
    estimated_value: float = None
    paid: bool = False
    pdf: str = None
