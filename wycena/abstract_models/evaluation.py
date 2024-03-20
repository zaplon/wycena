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
    costumer: str
    phone_number: str
    price: float
    broker: str
    estimated_value: float = None
    vision_datetime: datetime.datetime = None
    finished: bool = False
    paid: bool = False
    assigned_to: str = None
    pdf: str = None
