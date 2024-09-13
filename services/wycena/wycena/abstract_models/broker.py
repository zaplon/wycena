import uuid

from pydantic import BaseModel


class Broker(BaseModel):
    id: uuid.UUID
    name: str
    phone_number: str
    notes: str
