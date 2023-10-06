from __future__ import annotations

from typing import List, Literal, Dict
from pydantic import Field

from notion_python_client.models.properties.select import Select


class MultiSelect(Select):

    type: Literal['multi_select'] = Field(default="multi_select")
    multi_select: List[Select]

    def create_object(self, property_name: str) -> Dict:
        """Color cannot be updated, so it is not included in the select object."""

        select = {
            property_name: {
                "multi_select": [{
                    "name": ms.name,
                } for ms in self.multi_select]
            }
        }

        select_cleaned = self.clean_none(select)

        return select_cleaned
