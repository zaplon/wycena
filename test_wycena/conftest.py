import os
from typing import Any, Generator

import pytest
from factory.alchemy import SQLAlchemyModelFactory
# Ensure our engine is shared
from sqlmodel import Session, SQLModel

from wycena.db.models import get_engine


@pytest.fixture
def fixtures_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures')


@pytest.fixture(scope="function")
def db_session() -> Generator[Session, Any, None]:
    from factories import EvaluationFactory, PhotoFactory, TransactionFactory # noqa

    engine = get_engine()
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    session = Session(engine)

    # Ensure that all factories use the same session
    for factory in SQLAlchemyModelFactory.__subclasses__():
        factory._meta.sqlalchemy_session = session

    yield session

    session.rollback()
    session.close()
