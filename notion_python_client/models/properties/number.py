from typing import Dict, Union, Optional, Literal
from pydantic import Field

from notion_python_client.models.properties.properties_base import PropertiesBase


class Number(PropertiesBase):
    type: Literal['number'] = Field(default="number")
    number: Optional[Union[float, int]] = Field(default=None)

    def create_object(self, property_name: str) -> Dict:
        number = {
            property_name: {
                "number": self.number
            }
        }

        number_cleaned = self.clean_none(number)

        return number_cleaned
