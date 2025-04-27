from typing import Dict, Literal, Optional

from pydantic import Field

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.properties.properties_base_dict import (
    PropertiesDictBase,
)


class Select(PropertiesBase):
    color_: Optional[
        Literal[
            "blue",
            "brown",
            "default",
            "gray",
            "green",
            "orange",
            "pink",
            "purple",
            "red",
            "yellow",
        ]
    ] = Field(default="default")
    id: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)

    @property
    def color(self):
        return self.color_

    @color.setter
    def color(self, value):
        if value not in [
            "blue",
            "brown",
            "gray",
            "green",
            "orange",
            "pink",
            "purple",
            "red",
            "yellow",
        ]:
            self.color_ = "default"
        else:
            self.color_ = value

    def create_object(self, property_name: str) -> Dict:
        """Color cannot be updated, so it is not included in the select object."""

        select = {
            property_name: {
                "select": {
                    "name": self.name,
                }
            }
        }

        select_cleaned = self.clean_none(select)

        return select_cleaned


class SelectDict(PropertiesDictBase):
    type: Literal["select"] = Field(default="select")
    select: Optional[Select] = Field(default=None)

    def _get_base(self) -> Optional[PropertiesBase]:
        return self.select
