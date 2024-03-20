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
    def create(cls, data: dict):
        with Session(get_engine()) as session:
            instance = cls(**data)
            session.add(instance)
            session.commit()
            session.refresh(instance)
        return instance


    @classmethod
    def update(cls, pk: uuid.UUID, data: dict):
        with Session(get_engine()) as session:
            statement = select(cls).where(getattr(cls, "id") == pk)
            instance = session.exec(statement).one()
            for k, v in data.items():
                setattr(instance, k, v)
            session.add(instance)
            session.commit()
            session.refresh(instance)
        return instance

    @classmethod
    def delete(cls, pk: uuid.UUID):
        with Session(get_engine()) as session:
            statement = select(cls).where(getattr(cls, "id") == pk)
            instance = session.exec(statement).one()
            session.delete(instance)
            session.commit()

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


class Client(abstract_models.Client, BaseModel, table=True):
    id: Optional[uuid.UUID] = Field(default=None, primary_key=True)


class Broker(abstract_models.Broker, BaseModel, table=True):
    id: Optional[uuid.UUID] = Field(default=None, primary_key=True)


class Evaluation(abstract_models.Evaluation, BaseModel, table=True):
    id: Optional[uuid.UUID] = Field(default=None, primary_key=True)
    photos: List["Photo"] = Relationship(back_populates="evaluation")
    client_id: uuid.UUID = Field(foreign_key="client.id")
    broker_id: Optional[uuid.UUID] = Field(default=None, foreign_key="broker.id")

    client: Client = Relationship(back_populates="evaluations")
    broker: Broker = Relationship(back_populates="evaluations")


class Photo(abstract_models.Photo, BaseModel, table=True):
    id: Optional[uuid.UUID] = Field(default=None, primary_key=True)
    evaluation_id: uuid.UUID = Field(foreign_key="evaluation.id")
    evaluation: Evaluation = Relationship(back_populates="photos")


def get_engine():
    return create_engine(settings.DSN)


def create_models():
    SQLModel.metadata.create_all(get_engine())
