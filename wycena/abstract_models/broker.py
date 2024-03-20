from pydantic import BaseModel


class Broker(BaseModel):
    name: str
    phone_number: str
    notes: str
