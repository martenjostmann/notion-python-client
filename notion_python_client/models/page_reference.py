from pydantic import BaseModel
import uuid


class PageReference(BaseModel):
    id: uuid.UUID
