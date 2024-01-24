from pynamodb.attributes import UnicodeAttribute, NumberAttribute, BooleanAttribute, ListAttribute

from wycena.db.models.base import BaseMeta, BaseModel


class Evaluation(BaseModel):
    class Meta(BaseMeta):
        table_name = 'evaluations'
    address = UnicodeAttribute(hash_key=True)
    buyer = UnicodeAttribute()
    provider = UnicodeAttribute()
    price = NumberAttribute()
    estimated_value = NumberAttribute()
    phone_number = UnicodeAttribute()
    pdf = UnicodeAttribute()
    assigned_to = UnicodeAttribute()
    finished = BooleanAttribute()
    photos = ListAttribute()
