from typing import Dict, Union

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.properties.properties_base_dict import PropertiesDictBase


class Number(PropertiesDictBase, PropertiesBase):
    number: Union[float, int]

    def create_object(self, property_name: str) -> Dict:
        number = {
            property_name: {
                "number": self.number
            }
        }

        number_cleaned = self.clean_none(number)

        return number_cleaned