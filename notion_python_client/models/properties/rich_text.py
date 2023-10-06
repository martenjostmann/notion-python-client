from typing import Dict, List, Literal
from pydantic import Field

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.rich_text import RichText


class RichTextProp(PropertiesBase):
    type: Literal['rich_text'] = Field(default="rich_text")
    rich_text: List[RichText]

    def create_object(self, property_name: str) -> Dict:

        rich_text = {
            property_name: {
                "rich_text": self.rich_text
            }
        }

        rich_text_cleaned = self.clean_none(rich_text)

        return rich_text_cleaned
