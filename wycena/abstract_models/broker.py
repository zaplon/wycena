from pydantic import BaseModel


class Broker(BaseModel):
    name: str
