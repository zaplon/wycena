from pynamodb.attributes import UnicodeAttribute

from wycena.db.models.base import BaseMeta, BaseModel


class Evaluation(BaseModel):
    class Meta(BaseMeta):
        table_name = 'evaluations'
    address = UnicodeAttribute(hash_key=True)
    buyer = UnicodeAttribute()
