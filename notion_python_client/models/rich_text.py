from pydantic import BaseModel, Field

from typing import Literal, Dict, Optional

from notion_python_client.models.equation import Equation
from notion_python_client.models.mention import Mention
from notion_python_client.models.text import Text
from notion_python_client.models.annotations import Annotation
from notion_python_client.models.properties.properties_base import PropertiesBase


class RichText(PropertiesBase, BaseModel):
    type: Literal["text", "mention", "equation"]
    text: Optional[Text] = Field(default=None)
    mention: Optional[Mention] = Field(default=None)
    equation: Optional[Equation] = Field(default=None)
    annotations: Annotation = Field(default=None)
    plain_text: Optional[str] = Field(default=None)
    href: Optional[str] = Field(default=None)

    def create_object(self, property_name: str) -> Dict:
        if self.type == "text":
            text = {
                property_name: {
                    "content": self.text.content,
                    "link": self.text.link
                }
            }

            text_cleaned = self.clean_none(text)

            return text_cleaned
