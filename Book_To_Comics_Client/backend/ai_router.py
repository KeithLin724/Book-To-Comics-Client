from fastapi import APIRouter
from router_item import CutPromptItem, ListPromptItem

ai_router = APIRouter()


@ai_router.post("/cut_prompt")
async def cut_prompt(message: CutPromptItem):
    return {"message": "not ready"}


@ai_router.post("/list_prompt_to_image")
async def prompt_to_image(list_of_prompt: ListPromptItem):
    return {"message": "not ready"}
