from typing import Dict, Literal

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.user import User


class LastEditedBy(PropertiesBase):
    type: Literal['last_edited_by'] = "last_edited_by"
    last_edited_by: User

    def create_object(self, property_name: str) -> Dict:
        """The last_edited_by property cannot be updated, 
        so it is not included in the last_edited_by object."""

        return None
