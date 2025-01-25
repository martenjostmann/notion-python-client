from datetime import datetime
from typing import Annotated, Dict, Optional, Union

from pydantic import BaseModel, Field

from notion_python_client.models.emoji import Emoji
from notion_python_client.models.file import File
from notion_python_client.models.parent import Parent
from notion_python_client.models.properties import (
    URL,
    Checkbox,
    CreatedBy,
    CreatedTime,
    DateDict,
    Email,
    Files,
    FormulaDict,
    LastEditedBy,
    LastEditedTime,
    MultiSelect,
    Number,
    People,
    PhoneNumber,
    Relation,
    RichTextProp,
    SelectDict,
    StatusDict,
    Title,
    UniqueIdDict,
    RollupDict,
)
from notion_python_client.models.user import User


class Page(BaseModel):
    object: str = Field(default="page")
    id: str
    archived: Optional[bool] = Field(default=False)
    parent: Parent
    created_time: datetime
    last_edited_time: datetime
    created_by: User
    last_edited_by: User
    icon: Optional[Union[File, Emoji]] = Field(default=None)
    cover: Optional[File] = Field(default=None)
    properties: Dict[
        str,
        Annotated[
            Union[
                DateDict,
                StatusDict,
                Number,
                SelectDict,
                MultiSelect,
                People,
                Files,
                Checkbox,
                Email,
                PhoneNumber,
                FormulaDict,
                Relation,
                CreatedTime,
                CreatedBy,
                LastEditedTime,
                LastEditedBy,
                RichTextProp,
                Title,
                URL,
                UniqueIdDict,
                RollupDict,
            ],
            Field(discriminator="type"),
        ],
    ]
    url: str
    public_url: Optional[str] = Field(default=None)
