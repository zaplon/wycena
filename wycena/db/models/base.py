from pynamodb.models import Model

from wycena.settings import settings


class BaseMeta:
    region = 'eu-central-1'
    host = settings.DB_HOST
    aws_access_key_id = "anything"
    aws_secret_access_key = "fake"


class BaseModel(Model):
    def filter(self, QueryOptions):
        pass
