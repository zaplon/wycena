import datetime
import uuid
from typing import Optional

from pydantic import BaseModel

from .enums import PropertyType
from .base import AddressMixin


class Transaction(BaseModel, AddressMixin):
    id: uuid.UUID
    type: PropertyType
    long: float
    lat: float
    price: int
    area: float
    transaction_date: datetime.date
    district: Optional[str] = ""
    primary_market: Optional[bool] = None
    floor: Optional[int] = None
    number_of_floors: Optional[int] = None
    number_of_rooms: Optional[int] = None
