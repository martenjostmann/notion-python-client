from typing import Dict, Literal, Optional
from pydantic import Field
from datetime import datetime

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.properties.properties_base_dict import (
    PropertiesDictBase,
)


class Rollup(PropertiesBase):
    """Rollup property

    Args:
        function: The function to apply to the rollup.
        relation_property_id: The id of the related database property that is rolled up.
        relation_property_name: The name of the related database property that is rolled up.
        rollup_property_id: The id of the rollup property.
        rollup_property_name: The name of the rollup property.

    """

    type: Literal["array", "date", "incomplete", "number", "unsupported"]
    array: Optional[list] = Field(default=None)
    date: Optional[datetime] = Field(default=None)
    number: Optional[float] = Field(default=None)
    incomplete: Optional[bool] = Field(default=None)
    unsupported: Optional[bool] = Field(default=None)
    function: Literal[
        "average",
        "checked",
        "count_per_group",
        "count",
        "count_values",
        "date_range",
        "earliest_date",
        "empty",
        "latest_date",
        "max",
        "median",
        "min",
        "not_empty",
        "percent_checked",
        "percent_empty",
        "percent_not_empty",
        "percent_per_group",
        "percent_unchecked",
        "range",
        "unchecked",
        "unique",
        "show_original",
        "show_unique",
        "sum",
    ]

    def create_object(self, property_name: str) -> Dict:
        """Create a rollup json object."""

        rollup = {
            property_name: {
                "rollup": {
                    "type": self.type,
                    "array": self.array,
                    "date": self.date,
                    "number": self.number,
                    "incomplete": self.incomplete,
                    "unsupported": self.unsupported,
                    "function": self.function,
                }
            }
        }

        rollup_cleaned = self.clean_none(rollup)

        return rollup_cleaned


class RollupDict(PropertiesDictBase):
    type: Literal["rollup"] = Field(default="rollup")
    rollup: Rollup

    def _get_base(self) -> Optional[PropertiesBase]:
        return self.rollup
