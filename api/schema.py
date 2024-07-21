from pydantic import BaseModel


class MemeGet(BaseModel):
    id: int
    description: str
    image_url: str


class MemeCreated(BaseModel):
    id: int
