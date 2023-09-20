from pydantic import BaseModel
from typing import Optional

from notion_python_client.models.link import Link


class Text(BaseModel):
    content: str
    link: Link
