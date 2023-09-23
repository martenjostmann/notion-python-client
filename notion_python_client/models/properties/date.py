from pydantic import Field

from typing import Dict, Optional, Union
from datetime import datetime, date

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.properties.properties_base_dict import PropertiesDictBase


class Date(PropertiesBase):
    start: Optional[Union[datetime, date]]
    end: Optional[datetime] = Field(default=None)

    def create_object(self, property_name: str) -> Dict:
        date = {
            property_name: {
                "date": {
                    "start": self.start,
                    "end": self.end
                }
            }
        }

        date_cleaned = self.clean_none(date)

        return date_cleaned


class DateDict(PropertiesDictBase):
    date: Optional[Date]
