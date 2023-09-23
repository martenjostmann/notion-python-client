from typing import Dict

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.properties.properties_base_dict import PropertiesDictBase


class PhoneNumber(PropertiesDictBase, PropertiesBase):
    phone_number: str

    def create_object(self, property_name: str) -> Dict:
        phone_number = {
            property_name: {
                "phone_number": self.phone_number
            }
        }

        phone_number_cleaned = self.clean_none(phone_number)

        return phone_number_cleaned