from typing import List

from notion_python_client.models.properties.properties_base_dict import PropertiesDictBase
from notion_python_client.models.properties.select import Select


class MultiSelectDict(PropertiesDictBase):
    multi_select: List[Select]
