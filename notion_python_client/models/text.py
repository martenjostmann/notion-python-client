from pydantic import BaseModel, Field
from typing import Optional

from notion_python_client.models.link import Link


class Text(BaseModel):
    content: str
    link: Optional[Link] = Field(default=None)
