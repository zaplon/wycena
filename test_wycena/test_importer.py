import os

from wycena.importer.transaction import perform_import
from wycena.db import models as db_models


def test_importer(fixtures_dir, db):
    perform_import(
        os.path.join(fixtures_dir, "importer", "mokotow.csv"),
        city="Warszawa",
        type="apartment"
    )
    assert db_models.Transaction.count() > 0
