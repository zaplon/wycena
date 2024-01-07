import os
import tempfile

import strawberry

from wycena.api import storage
from wycena.importer.transaction import perform_import


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
