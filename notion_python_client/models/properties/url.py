from typing import Dict, Literal, Optional

from pydantic import Field

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.properties.properties_base_dict import (
    PropertiesDictBase,
)


class URL(PropertiesDictBase, PropertiesBase):
    type: Literal['url'] = Field(default="url")
    url: Optional[str] = Field(default=None)

    def create_object(self, property_name: str) -> Dict:
        url = {
            property_name: {
                "url": self.url
            }
        }

        url_cleaned = self.clean_none(url)

        return url_cleaned
