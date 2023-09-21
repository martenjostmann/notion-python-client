from typing import Dict

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.properties.properties_base_dict import PropertiesDictBase
from notion_python_client.models.user import User

class CreatedBy(PropertiesDictBase, PropertiesBase):
    created_by: User

    def create_object(self, property_name: str) -> Dict:
        """The created_by property cannot be updated, so it is not included in the created_by object."""

        return None
