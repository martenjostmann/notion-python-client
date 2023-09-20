from pydantic import BaseModel, Field
from typing import Literal, Dict, Optional
from datetime import datetime


class File(BaseModel):
    type: Literal["external", "file"]
    file: Optional[Dict[str, datetime]] = Field(default=None)
    external: Optional[Dict] = Field(default=None)
