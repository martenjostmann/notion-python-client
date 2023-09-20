from pydantic import BaseModel, Field


class Emoji(BaseModel):
    type: str = Field(default="emoji")
    emoji: str
