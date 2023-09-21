from datetime import datetime
from typing import Dict

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.properties.properties_base_dict import PropertiesDictBase


class CreatedTime(PropertiesDictBase, PropertiesBase):
    created_time: datetime

    def create_object(self, property_name: str) -> Dict:
        """The created_time property cannot be updated, so it is not included in the created_time object."""

        return None
