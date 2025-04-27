from typing import Dict, Literal, Optional

from pydantic import Field

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.properties.properties_base_dict import (
    PropertiesDictBase,
)


class Status(PropertiesBase):
    """Status property

    Args:
        color_ (_type_, optional): The color of the status badge. Defaults to "default".
        id (str, optional): The id of the status. Defaults to None.
        name (str): The name of the option as it appears in Notion.

    """

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
    name: str

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
        """Color cannot be updated, so it is not included in the status object."""

        status = {
            property_name: {
                "status": {
                    "name": self.name,
                }
            }
        }

        status_cleaned = self.clean_none(status)

        return status_cleaned


class StatusDict(PropertiesDictBase):
    type: Literal["status"] = Field(default="status")
    status: Status

    def _get_base(self) -> Optional[PropertiesBase]:
        return self.status
