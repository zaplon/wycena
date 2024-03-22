import uuid

from pydantic import BaseModel

from wycena.abstract_models.base import AddressMixin


class Client(BaseModel, AddressMixin):
    id: uuid.UUID
    name: str
    phone_number: str
