from typing import Dict, Literal, Optional, Union

from pydantic import Field

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.properties.properties_base_dict import (
    PropertiesDictBase,
)


class UniqueId(PropertiesBase):
    number: Union[float, int]
    prefix: Optional[str] = Field(default=None)

    def create_object(self, property_name: str) -> Dict:
        unique_id = {
            property_name: {"unique_id": {"number": self.number, "prefix": self.prefix}}
        }

        unique_id_cleaned = self.clean_none(unique_id)

        return unique_id_cleaned


class UniqueIdDict(PropertiesDictBase):
    type: Literal["unique_id"] = Field(default="unique_id")
    unique_id: UniqueId

    def _get_base(self) -> Optional[PropertiesBase]:
        return self.unique_id
