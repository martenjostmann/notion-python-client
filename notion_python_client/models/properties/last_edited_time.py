from typing import Dict
from datetime import datetime

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.properties.properties_base_dict import PropertiesDictBase


class LastEditedTime(PropertiesDictBase, PropertiesBase):
    last_edited_time: datetime

    def create_object(self, property_name: str) -> Dict:
        """The last_edited_time property cannot be updated, so it is not included in the last_edited_time object."""

        return None
