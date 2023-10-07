from pydantic import BaseModel, Field
import uuid
from typing import Dict


class Parent(BaseModel):
    """Note: Currntly only the datbase parent is supported. 
    The page parent is not supported yet.
    """

    type: str = Field(default="database_id")
    database_id: uuid.UUID

    def create_object(self, property_name: str = "parent") -> Dict:
        """Create a file object that can be used in the properties of a page.

        Args:
            property_name (str): The name of the property that should be created 
                (default: "parent")

        Returns:
            Dict: The created file object
        """
        return {
            property_name: {
                "database_id": str(self.database_id),
            }
        }
