import os
import re
import tempfile
import uuid

import strawberry
from strawberry.scalars import JSON

from wycena.api import storage
from wycena.importer.transaction import perform_import
from wycena.api.models import InstanceType

from wycena.db import models as db_models  # noqa


def camel_to_snake(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()


def snake_to_camel(name):
    init, *temp = name.split('_')
    return ''.join([init.lower(), *map(str.title, temp)])


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
        data.pop("id")
        klass = getattr(db_models, instance_type.value.capitalize())
        instance = klass.create({camel_to_snake(k): v for (k, v) in data.items()})
        return {snake_to_camel(k): v for (k, v) in instance.model_dump(mode='json').items()}

    @strawberry.mutation
    def update_instance(self, instance_type: InstanceType, pk: uuid.UUID, data: JSON) -> JSON:
        klass = getattr(db_models, instance_type.value.capitalize())
        instance = klass.update(pk, {camel_to_snake(k): v for (k, v) in data.items()})
        return {snake_to_camel(k): v for (k, v) in instance.model_dump(mode='json').items()}

    @strawberry.mutation
    def remove_instance(self, instance_type: InstanceType, pk: uuid.UUID) -> None:
        klass = getattr(db_models, instance_type.value.capitalize())
        klass.delete(pk)
