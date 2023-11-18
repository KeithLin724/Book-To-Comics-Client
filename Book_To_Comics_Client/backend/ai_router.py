from fastapi import APIRouter
import httpx
import ast
import asyncio

from router_item import CutPromptItem, ListPromptItem

ai_router = APIRouter()


@ai_router.post("/cut_prompt")
async def cut_prompt(message: CutPromptItem):
    """
    The `cut_prompt` function takes a `CutPromptItem` message as input, cuts the list of prompts in the
    message to describe the image, and returns the provider and the list of prompt items.

    :param message: The `message` parameter is a `CutPromptItem` object. It is used as input to the
    `CUT_PROMPT_FUNC` lambda function, which is responsible for cutting the list of prompts in the
    message to describe the image. The lambda function should return a list of strings, where each
    :type message: CutPromptItem
    :return: The function `cut_prompt` returns a dictionary with two keys: "provider" and "prompt_list".
    The value of the "provider" key is the provider obtained from the response, and the value of the
    "prompt_list" key is a list of prompts obtained from the response.
    """
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
        "provider": provider,
        "prompt_list": prompt_list,
    }


@ai_router.post("/list_prompt_to_image")
async def prompt_to_image(list_of_prompt: ListPromptItem):
    # TODO: make the prompt to json_data request
    json_data_list = [
        {
            "type_service": "text_to_image",
            "prompt": prompt_item,
        }
        for prompt_item in list_of_prompt.prompt_list
    ]

    # TODO: send request to server
    async with httpx.AsyncClient() as client:
        tasks = [
            client.post(
                "http://140.113.238.35:5000/generate_service",
                json=json_data,
                timeout=10,
            )
            for json_data in json_data_list
        ]
        response = await asyncio.gather(*tasks)

    result_list_of_id = [item.json() for item in response]

    return {"result": result_list_of_id}
