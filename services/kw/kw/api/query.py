import strawberry

from . import models


@strawberry.type
class Query:
    @strawberry.field
    def ksiega_wieczysta(self, numer: str) -> models.KsiegaWieczysta:
        pass


