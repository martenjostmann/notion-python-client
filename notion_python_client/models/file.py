from pydantic import BaseModel, Field
from typing import Literal, Dict, Optional, Union
from datetime import datetime


class File(BaseModel):
    name: Optional[str] = Field(default=None)
    type: Literal["external", "file"]
    file: Optional[Dict[str, Union[str, datetime]]] = Field(default=None)
    external: Optional[Dict] = Field(default=None)

    def create_object(self, property_name: str = "file") -> Dict:
        """Create a file object that can be used in the properties of a page.

        Args:
            property_name (str): The name of the property that should be created
                (default: "file")

        Returns:
            Dict: The created file object
        """
        if self.file is not None:
            return {
                property_name: {
                    # "name": self.name,
                    "file": self.file,
                }
            }
        elif self.external is not None:
            return {
                property_name: {
                    # "name": self.name,
                    "external": self.external
                }
            }
