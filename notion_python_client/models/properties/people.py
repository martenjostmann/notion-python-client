from typing import Dict, List, Literal
from pydantic import Field

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.user import User


class People(PropertiesBase):
    type: Literal['people'] = Field(default="people")
    people: List[User]

    def create_object(self, property_name: str) -> Dict:
        people = {
            property_name: {
                "people": self.people
            }
        }

        people_cleaned = self.clean_none(people)

        return people_cleaned
