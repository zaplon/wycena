from test_wycena.models.transaction import TransactionFactory
from wycena.models import Transaction, QueryOptions, QueryFilter
from wycena.models.enums import QueryFilterType


def test_filtering_transactions(db):
    TransactionFactory.create(city="Warszawa").to_db()
    TransactionFactory.create(city="Katowice").to_db()
    options = QueryOptions(filters=[
        QueryFilter(field_name="city", value="Warszawa", filter_type=QueryFilterType.EQUAL)]
    )
    assert len(Transaction.filter(options)) == 1
