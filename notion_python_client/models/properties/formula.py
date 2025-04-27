from datetime import datetime
from typing import Dict, Literal, Optional, Union

from pydantic import Field

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.properties.properties_base_dict import (
    PropertiesDictBase,
)


class Formula(PropertiesBase):
    boolean: Optional[bool] = Field(default=None)
    date: Optional[datetime] = Field(default=None)
    number: Optional[Union[float, int]] = Field(default=None)
    string: Optional[str] = Field(default=None)
    type: Literal["boolean", "date", "number", "string"]

    def create_object(self, property_name: str) -> Dict:
        """The formula property cannot be updated,
        so it is not included in the formula object."""

        return None


class FormulaDict(PropertiesDictBase):
    type: Literal["formula"] = Field(default="formula")
    formula: Formula

    def _get_base(self) -> Optional[PropertiesBase]:
        return self.formula
