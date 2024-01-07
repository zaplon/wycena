from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute, BooleanAttribute

from wycena.db.models.base import BaseMeta


class Transaction(Model):
    class Meta(BaseMeta):
        table_name = 'transaction'
    id = UnicodeAttribute(hash_key=True)
    street = UnicodeAttribute()
    building_number = UnicodeAttribute()
    apartment_nr = NumberAttribute(null=True)
    city = UnicodeAttribute()
    type = UnicodeAttribute()
    long = NumberAttribute()
    lat = NumberAttribute()
    price = NumberAttribute(range_key=True)
    area = NumberAttribute()
    transaction_date = UTCDateTimeAttribute()
    district = UnicodeAttribute(null=True)
    primary_market = BooleanAttribute(null=True)
    floor = NumberAttribute(null=True)
    number_of_floors = NumberAttribute(null=True)
    number_of_rooms = NumberAttribute(null=True)
