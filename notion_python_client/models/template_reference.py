from pydantic import BaseModel, Field
from typing import Optional, Literal


class TemplateReference(BaseModel):
    type: Literal["template_mention_date", "template_mention_uesr"]
    template_mention_date: Optional[Literal["today", "now"]] = Field(
        default=None)
    template_mention_user: Optional[Literal["me"]] = Field(default=None)
