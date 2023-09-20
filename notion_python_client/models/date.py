from pydantic import BaseModel, Field
from typing import Optional, Union
from datetime import datetime, date


class Date(BaseModel):
    start: Union[datetime, date]
    end: Optional[datetime] = Field(default=None)
