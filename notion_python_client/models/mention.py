from pydantic import BaseModel, Field
from typing import Literal, Optional

from database_reference import DatabaseReference
from date import Date
from link import Link
from page_reference import PageReference
from template_reference import TemplateReference
from user import User


class Mention(BaseModel):
    type: Literal["database", "date",
                  "link_preview", "page", "template_mention", "user"]
    database: Optional[DatabaseReference] = Field(default=None)
    date: Optional[Date] = Field(default=None)
    link_preview: Optional[Link] = Field(default=None)
    page: Optional[PageReference] = Field(default=None)
    template_mention: Optional[TemplateReference] = Field(default=None)
    user: Optional[User] = Field(default=None)
