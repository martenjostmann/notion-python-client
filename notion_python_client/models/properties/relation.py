from pydantic import Field
from typing import Dict, List

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.properties.properties_base_dict import PropertiesDictBase
from notion_python_client.models.page_reference import PageReference


class Relation(PropertiesDictBase, PropertiesBase):
    has_more: bool = Field(default=False)
    relation: List[PageReference]

    def create_object(self, property_name: str) -> Dict:

        relation = {
            property_name: {
                "relation": [{"id": r} for r in self.relation]
            }
        }

        relation_cleaned = self.clean_none(relation)

        return relation_cleaned
