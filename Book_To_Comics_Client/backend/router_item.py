from pydantic import BaseModel


class CutPromptItem(BaseModel):
    prompt: str


class ListPromptItem(BaseModel):
    prompt: list[str]
