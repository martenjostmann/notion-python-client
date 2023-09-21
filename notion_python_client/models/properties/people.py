from typing import Dict, List

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.properties.properties_base_dict import PropertiesDictBase
from notion_python_client.models.user import User


class People(PropertiesDictBase, PropertiesBase):
    people: List[User]

    def create_object(self, property_name: str) -> Dict:
        people = {
            property_name: {
                "people": self.people
            }
        }

        people_cleaned = self.clean_none(people)

        return people_cleaned
