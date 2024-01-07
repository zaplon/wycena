from pynamodb.models import Model

from wycena.models import QueryOptions
from wycena.models.enums import QueryFilterType
from wycena.settings import settings


class BaseMeta:
    region = 'eu-central-1'
    host = settings.DB_HOST
    aws_access_key_id = "anything"
    aws_secret_access_key = "fake"


class BaseModel(Model):
    def filter(self, options: QueryOptions):
        conditions = None
        for f in options.filters:
            if f.filter_type == QueryFilterType.EQUAL:
                conditions &= getattr(self, f.field_name) == f.value
        return self.query(conditions=conditions, limit=options.pageSize)
