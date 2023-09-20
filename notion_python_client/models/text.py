from pydantic import BaseModel
from typing import Optional

from link import Link


class Text(BaseModel):
    content: str
    link: Link
