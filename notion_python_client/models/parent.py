from pydantic import BaseModel, Field
import uuid


class Parent(BaseModel):
    type: str = Field(default="database_id")
    database_id: uuid.UUID
