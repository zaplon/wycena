from pynamodb.models import Model

from wycena.models.base import QueryOptions
from wycena.models.enums import QueryFilterType
from wycena.settings import settings


class BaseMeta:
    region = 'eu-central-1'
    host = settings.DB_HOST
    aws_access_key_id = "anything"
    aws_secret_access_key = "fake"


class BaseModel(Model):
    @classmethod
    def filter(cls, options: QueryOptions):
        conditions = None
        for f in options.filters:
            if f.filter_type == QueryFilterType.EQUAL:
                conditions &= getattr(cls, f.field_name) == f.value
            elif f.filter_type == QueryFilterType.GREATER_THAN:
                conditions &= getattr(cls, f.field_name) > f.value
            elif f.filter_type == QueryFilterType.LOWER_THAN:
                conditions &= getattr(cls, f.field_name) < f.value
        return cls.query(
            hash_key=cls._hash_keyname,
            filter_condition=conditions,
            limit=options.pageSize,
            last_evaluated_key=options.last_key
        )

