from pydantic import BaseModel


class CutPromptItem(BaseModel):
    message: str


class ListPromptItem(BaseModel):
    message: list[str]
