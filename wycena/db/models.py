import uuid
from typing import Optional, List

from sqlalchemy import create_engine
from sqlmodel import Field, SQLModel, Relationship, Session, select
from wycena import abstract_models
from wycena.settings import settings


class BaseModel(SQLModel):
    @classmethod
    def get(cls, pk: uuid.UUID):
        with Session(get_engine()) as session:
            statement = select(cls).where(getattr(cls, "id") == pk)
            return session.exec(statement).first()

    @classmethod
    def filter(cls, options: abstract_models.QueryOptions):
        with Session(get_engine()) as session:
            statement = select(cls)
            for query_filter in options.filters:
                if query_filter.filter_type == abstract_models.QueryFilterType.EQUAL:
                    statement = statement.where(getattr(cls, query_filter.field_name) == query_filter.value)
                elif query_filter.filter_type == abstract_models.QueryFilterType.GREATER_THAN:
                    statement = statement.where(getattr(cls, query_filter.field_name) > query_filter.value)
                elif query_filter.filter_type == abstract_models.QueryFilterType.LOWER_THAN:
                    statement = statement.where(getattr(cls, query_filter.field_name) < query_filter.value)
            total_count = len(list(session.exec(statement)))
            if options.offset:
                statement = statement.offset(options.offset)
            statement = statement.limit(options.page_size)
            return list(session.exec(statement)), total_count


class Transaction(abstract_models.Transaction, BaseModel, table=True):
    id: Optional[uuid.UUID] = Field(default=None, primary_key=True)


class Evaluation(abstract_models.Evaluation, BaseModel, table=True):
    id: Optional[uuid.UUID] = Field(default=None, primary_key=True)
    photos: List["Photo"] = Relationship(back_populates="evaluation")


class Photo(abstract_models.Photo, BaseModel, table=True):
    id: Optional[uuid.UUID] = Field(default=None, primary_key=True)
    evaluation_id: uuid.UUID = Field(foreign_key="evaluation.id")
    evaluation: Evaluation = Relationship(back_populates="photos")


class Buyer(abstract_models.Buyer, BaseModel, table=True):
    id: Optional[uuid.UUID] = Field(default=None, primary_key=True)


class Broker(abstract_models.Broker, BaseModel, table=True):
    id: Optional[uuid.UUID] = Field(default=None, primary_key=True)


def get_engine():
    return create_engine(settings.DSN)


def create_models():
    SQLModel.metadata.create_all(get_engine())
