import datetime

from wycena.models import PropertyType
from wycena.models.base import BaseDBModel, AddressMixin


class Transaction(BaseDBModel, AddressMixin):
    type: PropertyType
    long: float
    lat: float
    price: int
    area: float
    transaction_date: datetime.date
    district: str = None
    primary_market: bool = None
    floor: int = None
    number_of_floors: int = None
    number_of_rooms: int = None
