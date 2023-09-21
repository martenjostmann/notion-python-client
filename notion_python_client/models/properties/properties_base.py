from pydantic import BaseModel
from typing import Dict, no_type_check, List
from abc import ABC, abstractmethod
import inspect


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
                predicate=lambda x: isinstance(
                    x, property) and x.fset is not None
            )
            for setter_name, func in setters:
                if setter_name == name:
                    object.__setattr__(self, name, value)
                    break
            else:
                raise e


class PropertiesBase(PatchedModel, ABC):
    @abstractmethod
    def create_object(self, property_name: str) -> Dict:
        pass

    def clean_none(self, d):
        if isinstance(d, dict):
            return {k: self.clean_none(v) for k, v in d.items() if v is not None}
        else:
            return d

    @staticmethod
    def build_properties(properties: List[Dict]) -> Dict:
        """Create a properties object from a list of properties that can be used to update a page.

        Args:
            properties (List[Dict]): List of propertie dictionaries that were created by the create_object method of the property classes.

        Returns:
            Dict: Combined properties dictionary out of a list of properties.
        """
        properties_dict = {}

        for property in properties:
            properties_dict.update(property)

        return {"properties": properties_dict}
