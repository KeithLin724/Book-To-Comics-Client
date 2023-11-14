from fastapi import APIRouter
from router_item import CutPromptItem, ListPromptItem
import base64

ai_router = APIRouter()


def image_to_url(image_content: bytes) -> str:
    """
    The function `image_to_url` converts image content into a data URI string.

    :param image_content: The `image_content` param eter is a bytes object that represents the content of
    an image file
    :type image_content: bytes
    :return: a string that represents the image content as a data URI.
    """
    image_base64 = base64.b64encode(image_content).decode("utf-8")
    data_uri = f"data:image/png;base64,{image_base64}"
    return data_uri


def image_to_markdown(image_url: str) -> str:
    return f"![Image]({image_url})"


@ai_router.post("/cut_prompt")
async def cut_prompt(message: CutPromptItem):
    return {"message": "not ready"}


@ai_router.post("/list_prompt_to_image")
async def prompt_to_image(list_of_prompt: ListPromptItem):
    return {"message": "not ready"}
