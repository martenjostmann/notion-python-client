import inspect
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Union, no_type_check

from pydantic import BaseModel, Field

from notion_python_client.models.properties.properties_base_dict import (
    PropertiesDictBase,
)


class PropertiesBase:
    pass


class PatchedModel(BaseModel):
    @no_type_check
    def __setattr__(self, name, value):
        """
        To be able to use properties with setters
        """
        try:
            super().__setattr__(name, value)
        except ValueError as e:
            setters = inspect.getmembers(
                self.__class__,
                predicate=lambda x: isinstance(x, property) and x.fset is not None,
            )
            for setter_name, func in setters:
                if setter_name == name:
                    object.__setattr__(self, name, value)
                    break
            else:
                raise e


class PropertiesBase(PatchedModel, ABC):
    id: Optional[str] = Field(default=None)

    @abstractmethod
    def create_object(self, property_name: str) -> Dict:
        pass

    def clean_none(self, d):
        if isinstance(d, dict):
            return {k: self.clean_none(v) for k, v in d.items() if v is not None}
        else:
            return d

    @staticmethod
    def build_properties(
        properties: Union[
            List[Dict], Dict[str, Union[PropertiesBase, PropertiesDictBase]]
        ],
    ) -> Dict:
        """Create a properties object from a list of properties
        that can be used to update a page.

        Args:
            properties (
                Union[List[Dict], Dict[str, Union[PropertiesBase, PropertiesDictBase]]]
                ):
                List of property dictionaries that were created
                by the create_object method of the property classes.
                Or
                Dict of a property class and a property name.
                The create_object method of the property class will be
                called with the property name as argument.

                The dict should be of the following form:
                {
                    "type": "external",
                    "external": {
                        "url": "www.test.de/image.png"
                    }
                }

        Returns:
            Dict: Combined properties dictionary out of a list of properties.
        """
        properties_dict = {}

        if isinstance(properties, list):
            for property in properties:
                properties_dict.update(property)
        else:
            for property_name, property in properties.items():
                if isinstance(property, PropertiesDictBase):
                    print(property)
                    property = property._get_base()
                properties_dict.update(property.create_object(property_name))

        return {"properties": properties_dict}
