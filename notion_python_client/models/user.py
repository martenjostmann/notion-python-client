from pydantic import BaseModel, Field
import uuid


class User(BaseModel):
    object: str = Field(default="user")
    id: uuid.UUID
