from datetime import datetime
from typing import Optional, Union, Dict, Annotated

from pydantic import BaseModel, Field
from notion_python_client.models.user import User
from notion_python_client.models.file import File
from notion_python_client.models.emoji import Emoji
from notion_python_client.models.parent import Parent
from notion_python_client.models.properties import *


class Page(BaseModel):
    object: str = Field(default="page")
    id: str
    parent: Parent
    created_time: datetime
    last_edited_time: datetime
    created_by: User
    last_edited_by: User
    icon: Optional[Union[File, Emoji]] = Field(default=None)
    cover: Optional[File] = Field(default=None)
    properties: Dict[str, Annotated[Union[DateDict, StatusDict, Number, SelectDict, MultiSelectDict, People, Files, Checkbox,
                                          Email, PhoneNumber, FormulaDict, Relation, CreatedTime, CreatedBy, LastEditedTime, LastEditedBy, RichTextProp, Title, URL, UniqueIdDict], Field(discriminator="type")]]
    url: str
    public_url: Optional[str] = Field(default=None)
