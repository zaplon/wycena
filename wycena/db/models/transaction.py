from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute, BooleanAttribute

from wycena.db.models.base import BaseMeta, BaseModel


class CityIndex(GlobalSecondaryIndex):
    class Meta:
        index_name = "city_index"
        read_capacity_units = 5
        write_capacity_units = 10
        # All attributes from the table are projected here
        projection = AllProjection()
    city = UnicodeAttribute(hash_key=True)


class Transaction(BaseModel):
    class Meta(BaseMeta):
        table_name = 'transaction'
    id = UnicodeAttribute(hash_key=True)
    street = UnicodeAttribute()
    building_nr = UnicodeAttribute()
    apartment_nr = NumberAttribute(null=True)
    city = UnicodeAttribute()
    city_index = CityIndex()
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
