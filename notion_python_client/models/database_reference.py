from pydantic import BaseModel
import uuid


class DatabaseReference(BaseModel):
    id: uuid.UUID
