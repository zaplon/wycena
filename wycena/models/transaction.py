import datetime
import uuid

from pydantic import BaseModel

from wycena.models import PropertyType
from wycena.models.base import AddressMixin, QueryFilter


class Transaction(BaseModel, AddressMixin):
    id: uuid.UUID
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

    def to_db(self):
        from wycena.db.models.transaction import Transaction as TransactionModel
        return TransactionModel(
            id=str(self.id),
            type=self.type.value,
            transaction_date=datetime.datetime.combine(self.transaction_date, datetime.time.min),
            **self.model_dump(exclude={'id', 'transaction_date', 'type'})
        ).save()

    @staticmethod
    def filter(options: QueryFilter):
        from wycena.db.models.transaction import Transaction as TransactionModel
        return TransactionModel.filter(options)
