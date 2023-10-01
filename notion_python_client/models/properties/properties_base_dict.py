from pydantic import BaseModel, Field
from typing import Optional, Literal


class PropertiesDictBase(BaseModel):
    id: Optional[str] = Field(default=None)
