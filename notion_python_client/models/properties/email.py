from typing import Dict

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.properties.properties_base_dict import PropertiesDictBase


class Email(PropertiesDictBase, PropertiesBase):
    email: str

    def create_object(self, property_name: str) -> Dict:
        email = {
            property_name: {
                "email": self.email
            }
        }

        email_cleaned = self.clean_none(email)

        return email_cleaned
