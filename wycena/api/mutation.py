import os
import tempfile
import uuid

import strawberry
from strawberry.scalars import JSON

from wycena.api import storage
from wycena.importer.transaction import perform_import
from wycena.api.models import InstanceType

from wycena.db import models as db_models  # noqa


@strawberry.type
class Mutation:
    @strawberry.mutation
    def import_transactions(self, file_pointer: str) -> bool:
        extension = file_pointer.split('.')[-1]
        f = tempfile.NamedTemporaryFile(delete=False, suffix=extension)
        f.write(storage.read(file_pointer))
        f.close()
        perform_import(f)
        os.unlink(f.name)
        return True

    @strawberry.mutation
    def add_instance(self, instance_type: InstanceType, data: JSON) -> JSON:
        klass = globals()[f"db_models.{instance_type.value}"]
        instance = klass.create(data)
        return instance.dict()

    @strawberry.mutation
    def update_instance(self, instance_type: InstanceType, pk: uuid.UUID, data: JSON):
        klass = globals()[f"db_models.{instance_type.value}"]
        instance = klass.update(pk, data)
        return instance.dict()

    @strawberry.mutation
    def remove_instance(self, instance_type: InstanceType, data: JSON):
        klass = globals()[f"db_models.{instance_type.value}"]
        klass.delete(data)
