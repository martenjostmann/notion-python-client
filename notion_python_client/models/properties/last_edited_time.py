from typing import Dict, Literal
from datetime import datetime

from pydantic import Field

from notion_python_client.models.properties.properties_base import PropertiesBase


class LastEditedTime(PropertiesBase):
    type: Literal['last_edited_time'] = Field(default="last_edited_time")
    last_edited_time: datetime

    def create_object(self, property_name: str) -> Dict:
        """The last_edited_time property cannot be updated, 
        so it is not included in the last_edited_time object."""

        return None
