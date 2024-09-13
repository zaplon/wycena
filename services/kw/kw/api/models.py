import strawberry

from kw import abstract_models


@strawberry.experimental.pydantic.type(model=abstract_models.KsiegaWieczysta, all_fields=True)
class KsiegaWieczysta:
    pass
