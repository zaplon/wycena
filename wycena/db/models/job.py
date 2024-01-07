from pynamodb.attributes import UnicodeAttribute, BooleanAttribute
from pynamodb.models import Model


class Job(Model):
    id = UnicodeAttribute(hash_key=True)
    type = UnicodeAttribute()
    finished = BooleanAttribute()
    status = UnicodeAttribute(null=True)
