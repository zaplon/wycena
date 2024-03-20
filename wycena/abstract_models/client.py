from pydantic import BaseModel

from wycena.abstract_models.base import AddressMixin


class Client(BaseModel, AddressMixin):
    name: str
    phone_number: str
