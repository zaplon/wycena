import typing
import uuid

import strawberry

from . import models
from wycena.db import models as db_models
from wycena.settings import settings

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
        items, total_count = db_models.Evaluation.filter(options)
        return PaginationWindow(items=items, total_pages=int(total_count/settings.API_PAGE_SIZE))

    @strawberry.field
    def evaluation_by_pk(self, pk: uuid.UUID) -> models.Evaluation:
        return db_models.Evaluation.get(pk)

    @strawberry.field
    def transactions(self, options: models.QueryOptions = None) -> PaginationWindow[models.Transaction]:
        items, total_count = db_models.Transaction.filter(options)
        return PaginationWindow(items=items, total_pages=int(total_count/settings.API_PAGE_SIZE))

    @strawberry.field
    def similar_transactions(self, lat: float, long: float,
                             area: float, floor: int = None
                             ) -> typing.List[models.Transaction]:
        pass

    @strawberry.field
    def clients(self, options: models.QueryOptions = None) -> PaginationWindow[models.Client]:
        items, total_count = db_models.Client.filter(options)
        return PaginationWindow(items=items, total_pages=int(total_count/settings.API_PAGE_SIZE))

    @strawberry.field
    def client_by_pk(self, pk: uuid.UUID) -> models.Client:
        return db_models.Client.get(pk)

    @strawberry.field
    def brokers(self, options: models.QueryOptions = None) -> PaginationWindow[models.Broker]:
        items, total_count = db_models.Broker.filter(options)
        return PaginationWindow(items=items, total_pages=int(total_count/settings.API_PAGE_SIZE))

    @strawberry.field
    def broker_by_pk(self, pk: uuid.UUID) -> models.Broker:
        return db_models.Broker.get(pk)
