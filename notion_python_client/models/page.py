from datetime import datetime
from typing import Optional, Union, Dict

from pydantic import BaseModel, Field
from notion_python_client.models.user import User
from notion_python_client.models.file import File
from notion_python_client.models.emoji import Emoji
from notion_python_client.models.properties import *


class Page(BaseModel):
    object: str = Field(default="page")
    id: str
    created_time: datetime
    last_edited_time: datetime
    created_by: User
    last_edited_by: User
    icon: Optional[Union[File, Emoji]] = Field(default=None)
    cover: Optional[File] = Field(default=None)
    properties: Dict[str, Union[DateDict, StatusDict, Number, SelectDict, MultiSelectDict, People, Files, Checkbox,
                                Email, PhoneNumber, FormulaDict, Relation, CreatedTime, CreatedBy, LastEditedTime, LastEditedBy, RichTextProp, Title, URL, UniqueIdDict]]
    url: str
    public_url: Optional[str] = Field(default=None)


if __name__ == "__main__":
    data = {
        "object": "page",
        "id": "be633bf1-dfa0-436d-b259-571129a590e5",
        "created_time": "2022-10-24T22:54:00.000Z",
        "last_edited_time": "2023-03-08T18:25:00.000Z",
        "created_by": {
            "object": "user",
            "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"
        },
        "last_edited_by": {
            "object": "user",
            "id": "9188c6a5-7381-452f-b3dc-d4865aa89bdf"
        },
        "cover": None,
        "icon": {
            "type": "emoji",
            "emoji": "🐞"
        },
        "parent": {
            "type": "database_id",
            "database_id": "a1d8501e-1ac1-43e9-a6bd-ea9fe6c8822b"
        },
        "archived": True,
        "properties": {
            "Due date": {
                "id": "M%3BBw",
                "type": "date",
                "date": {
                    "start": "2023-02-23",
                    "end": None,
                    "time_zone": None
                }
            },
            "Status": {
                "id": "Z%3ClH",
                "type": "status",
                "status": {
                    "id": "86ddb6ec-0627-47f8-800d-b65afd28be13",
                    "name": "Not started",
                    "color": "default"
                }
            }


        },
        "url": "https://www.notion.so/Bug-bash-be633bf1dfa0436db259571129a590e5",
        "public_url": "https://jm-testing.notion.site/p1-6df2c07bfc6b4c46815ad205d132e22d"
    }
    page_obj = Page(**data)
    print(page_obj.properties["Due date"].type)
    print(page_obj.properties["Status"].status.name)
