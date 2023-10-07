from datetime import datetime
from typing import Dict, Literal

from notion_python_client.models.properties.properties_base import PropertiesBase

class CreatedTime(PropertiesBase):
    type: Literal['created_time'] = "created_time"
    created_time: datetime

    def create_object(self, property_name: str) -> Dict:
        """The created_time property cannot be updated, 
        so it is not included in the created_time object."""

        return None
