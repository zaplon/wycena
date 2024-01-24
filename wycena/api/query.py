import typing

import strawberry

from test_wycena.models.evaluation import EvaluationFactory
from test_wycena.models.transaction import TransactionFactory
from wycena.api import models


Item = typing.TypeVar("Item")


@strawberry.type
class PaginationWindow(typing.Generic[Item]):
    items: typing.List[Item] = strawberry.field(
        description="The list of items in this pagination window."
    )
    total_pages: int = strawberry.field(
        description="Total number of pages in the filtered dataset."
    )


@strawberry.type
class Query:
    @strawberry.field
    def evaluations(self, options: models.QueryOptions = None) -> PaginationWindow[models.Evaluation]:
        return PaginationWindow(items=EvaluationFactory.create_batch(10), total_pages=2)

    @strawberry.field
    def evaluation_by_id(self, pk: str) -> models.Evaluation:
        return EvaluationFactory.create()

    @strawberry.field
    def transactions(self, options: models.QueryOptions = None) -> PaginationWindow[models.Transaction]:
        return PaginationWindow(items=models.Transaction, total_pages=20)

    @strawberry.field
    def similar_transactions(self, lat: float, long: float,
                             area: float, floor: int = None
                             ) -> typing.List[models.Transaction]:
        pass
