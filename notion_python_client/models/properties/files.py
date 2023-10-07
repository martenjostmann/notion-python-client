from typing import Dict, List, Literal
from pydantic import Field

from notion_python_client.models.properties.properties_base import PropertiesBase
from notion_python_client.models.file import File


class Files(PropertiesBase):
    type: Literal['files'] = Field(default="files")
    files: List[File]

    def create_object(self, property_name: str) -> Dict:
        """When updating a file page property value, 
        the value is overwritten by the array of files passed."""

        files = {
            property_name: {
                "files": [file.create_object()["file"] for file in self.files]
            }
        }

        files_cleaned = self.clean_none(files)

        return files_cleaned
