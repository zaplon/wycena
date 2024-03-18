import os
from unittest import mock

from sqlmodel import Session, select

from wycena.abstract_models import PropertyType
from wycena.db.models import get_engine
from wycena.importer.transaction import perform_import
from wycena.db import models as db_models


def test_importer(fixtures_dir, db_session):
    with mock.patch("wycena.importer.transaction.get_coords", return_value=(30,20)):
        perform_import(
            os.path.join(fixtures_dir, "importer", "mokotow.csv"),
            city="Warszawa",
            type=PropertyType.APARTMENT
        )
    with Session(get_engine()) as session:
        statement = select(db_models.Transaction)
        assert len(list(session.exec(statement))) > 0
