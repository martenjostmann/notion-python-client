from pydantic import BaseModel
from typing import Optional, Literal


class Annotation(BaseModel):
    bold: Optional[bool]
    italic: Optional[bool]
    strikethrough: Optional[bool]
    underline: Optional[bool]
    code: Optional[bool]
    color: Optional[Literal["blue", "blue_background", "brown", "brown_background",
                            "default", "gray", "gray_background", "green",
                            "green_background", "orange", "orange_background", "pink",
                            "pink_background", "purple", "purple_background", "red",
                            "red_background", "yellow", "yellow_background"]]
