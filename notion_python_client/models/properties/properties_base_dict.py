from pydantic import BaseModel, Field
from typing import Optional, Literal


class PropertiesDictBase(BaseModel):
    id: Optional[str] = Field(default=None)
    type: Optional[Literal["checkbox", "created_by",
                           "created_time", "date", "email", "files",
                           "formula", "last_edited_by", "last_edited_time", "multi_select",
                           "number", "people", "phone_number", "relation", "rich_text",
                           "rollup", "select", "title", "url", "status", "unique_id", "url"]] = Field(default=None)
