from typing import Dict, Literal

from notion_python_client.models.properties.properties_base import PropertiesBase


class Checkbox(PropertiesBase):
    type: Literal['checkbox'] = "checkbox"
    checkbox: bool

    def create_object(self, property_name: str) -> Dict:
        checkbox = {
            property_name: {
                "checkbox": self.checkbox
            }
        }

        checkbox_cleaned = self.clean_none(checkbox)

        return checkbox_cleaned
