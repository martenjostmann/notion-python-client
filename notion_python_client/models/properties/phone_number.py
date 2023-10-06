from typing import Dict, Optional, Literal
from pydantic import Field

from notion_python_client.models.properties.properties_base import PropertiesBase



class PhoneNumber(PropertiesBase):
    type: Literal["phone_number"] = Field(default="phone_number")
    phone_number: Optional[str] = Field(default=None)

    def create_object(self, property_name: str) -> Dict:
        phone_number = {
            property_name: {
                "phone_number": self.phone_number
            }
        }

        phone_number_cleaned = self.clean_none(phone_number)

        return phone_number_cleaned
