from pydantic import Field

from typing import Dict, Optional, Union, Literal
from datetime import datetime, date

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.properties.properties_base_dict import PropertiesDictBase


class Date(PropertiesBase):
    start: Optional[Union[datetime, date]]
    end: Optional[Union[datetime, date]] = Field(default=None)

    def create_object(self, property_name: str) -> Dict:

        _start = None
        _end = None

        if self.start is not None:
            if isinstance(self.start, datetime):
                _start = self.start.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "z"
            else:
                _start = self.start.strftime('%Y-%m-%d')

        if self.end is not None:
            if isinstance(self.end, datetime):
                _end = self.end.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "z"
            else:
                _end = self.end.strftime('%Y-%m-%d')

        date = {
            property_name: {
                "date": {
                    "start": _start,
                    "end": _end
                }
            }
        }

        date_cleaned = self.clean_none(date)

        return date_cleaned


class DateDict(PropertiesDictBase):
    type: Literal['date'] = Field(default="date")
    date: Optional[Date] = Field(default=None)

    def _get_base(self) -> PropertiesBase:
        return self.date
