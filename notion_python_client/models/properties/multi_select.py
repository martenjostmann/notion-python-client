from typing import List, Literal
from pydantic import Field

from notion_python_client.models.properties.properties_base_dict import PropertiesDictBase
from notion_python_client.models.properties.select import Select


class MultiSelectDict(PropertiesDictBase):
    type: Literal['multi_select'] = Field(default="multi_select")
    multi_select: List[Select]
