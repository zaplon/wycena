import os

import pytest

from wycena.db.models import Evaluation, Transaction


@pytest.fixture
def fixtures_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures')


@pytest.fixture
def db():
    Evaluation.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
    Transaction.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
    yield
    Evaluation.delete_table()
    Transaction.delete_table()
