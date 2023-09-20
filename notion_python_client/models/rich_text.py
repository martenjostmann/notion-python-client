from pydantic import BaseModel, Field

from typing import Literal, Dict, Optional

from notion_python_client.models.equation import Equation
from notion_python_client.models.mention import Mention
from notion_python_client.models.text import Text
from notion_python_client.models.annotations import Annotation


class RichText(BaseModel):
    type: Literal["text", "mention", "equation"]
    text: Optional[Text] = Field(default=None)
    mention: Optional[Mention] = Field(default=None)
    equation: Optional[Equation] = Field(default=None)
    annotations: Annotation = Field(default=None)
    plain_text: str
    href: Optional[str] = Field(default=None)
