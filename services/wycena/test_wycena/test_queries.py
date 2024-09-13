from test_wycena.factories.transaction import TransactionFactory
from wycena.abstract_models import QueryOptions, QueryFilter
from wycena.abstract_models.enums import QueryFilterType
from wycena.api.main import schema
from wycena.db.models import Transaction


def test_filtering_transactions(db_session):
    TransactionFactory.create(city="Warszawa")
    TransactionFactory.create(city="Katowice")
    options = QueryOptions(filters=[
        QueryFilter(field_name="city", value="Warszawa", filter_type=QueryFilterType.EQUAL)]
    )
    transactions, _ = Transaction.filter(options)
    assert len(transactions) == 1


def test_transactions_query(db_session):
    query = """
        query GetTransactions($options: QueryOptions!){
            transactions(options: $options) {
                items {
                    city
                    price
                }
            }
        }
    """
    result = schema.execute_sync(
        query,
        variable_values={"options": {"filters": []}},
    )
    assert result.errors is None
