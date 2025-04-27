from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from notion_python_client.models.properties import PropertiesBase


class PropertiesDictBase(BaseModel):
    id: Optional[str] = Field(default=None)

    def _get_base(self) -> Optional[PropertiesBase]:
        """Returns the base property object."""
        return None
