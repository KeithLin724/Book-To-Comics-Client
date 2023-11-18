from fastapi import APIRouter
import httpx
import ast

from router_item import CutPromptItem, ListPromptItem

ai_router = APIRouter()


@ai_router.post("/cut_prompt")
async def cut_prompt(message: CutPromptItem):
    # TODO: "cut prompt" prompt function
    CUT_PROMPT_FUNC = (
        lambda message: f"can you cut list of prompt in the message to describe the image how to look like, return like ['...' , '...' , ...], message is {message}"
    )

    json_data = {
        "type_service": "chat",
        "prompt": CUT_PROMPT_FUNC(message=message),
    }

    # TODO: send request to server
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://140.113.238.35:5000/generate_service",
            json=json_data,
            timeout=10,
        )

    # TODO: get the result
    result = response.json()

    provider, message = result["provider"], result["message"]

    message = message.replace("\n", "")

    prompt_list = ast.literal_eval(message)

    return {
        "state": "success",
        "provider": provider,
        "prompt_list": prompt_list,
    }


@ai_router.post("/list_prompt_to_image")
async def prompt_to_image(list_of_prompt: ListPromptItem):
    return {"message": "not ready"}
