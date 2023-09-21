from typing import Dict, List, Union

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.properties.properties_base_dict import PropertiesDictBase
from notion_python_client.models.rich_text import RichText, Text


class Title(PropertiesDictBase, PropertiesBase):
    title_: List[RichText]

    def __init__(self, title: Union[str, List[RichText]], **kwargs):
        if type(title) == str:
            super().__init__(
                title_=[RichText(type="text", text=Text(content=title), plain_text=title)], **kwargs)
        elif type(title) == list:
            super().__init__(
                title_=title, **kwargs)
        else:
            raise TypeError(
                "Title must be of type str or List[RichText]")

    @property
    def title(self):
        return self.title_

    @title.setter
    def title(self, title: Union[str, List[RichText]]):
        if type(title) == str:
            self.title_ = [RichText(type="text", text=Text(
                content=title), plain_text=title)]
        elif type(title) == list:
            self.title_ = title
        else:
            raise TypeError(
                "Title must be of type str or List[RichText]")

    def create_object(self, property_name: str) -> Dict:
        title = {
            property_name: {
                "title": [t.create_object("text") for t in self.title_]
            }
        }

        title_cleaned = self.clean_none(title)

        return title_cleaned
