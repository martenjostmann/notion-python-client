from pydantic import BaseModel, Field
from typing import Literal, Optional

from notion_python_client.models.database_reference import DatabaseReference
from notion_python_client.models.date import Date
from notion_python_client.models.link import Link
from notion_python_client.models.page_reference import PageReference
from notion_python_client.models.template_reference import TemplateReference
from notion_python_client.models.user import User


class Mention(BaseModel):
    type: Literal["database", "date",
                  "link_preview", "page", "template_mention", "user"]
    database: Optional[DatabaseReference] = Field(default=None)
    date: Optional[Date] = Field(default=None)
    link_preview: Optional[Link] = Field(default=None)
    page: Optional[PageReference] = Field(default=None)
    template_mention: Optional[TemplateReference] = Field(default=None)
    user: Optional[User] = Field(default=None)
