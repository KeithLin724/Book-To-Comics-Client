import ast
import httpx
import asyncio
import Book_To_Comics_Client.state as state_data
import re

CUT_PROMPT_FUNC_1 = (
    lambda message: f"""
Given an image, I need your help to generate a clear list of prompts describing how the image looks. The prompts should be in list format.
Please use the information in the provided message {message} to craft the prompts. Return your responses in the format ['...', '...', ...]. Be as detailed and imaginative as possible. Thank you!
            """
)

CUT_PROMPT_FUNC_2 = (
    lambda message: f"""
Generate a list of prompts describing the appearance of an image based on the provided message. 
The prompts should be imaginative and comprehensive. Use the information in the message {message} to craft the prompts. 
Please present your responses in the format ['...', '...', ...]. Thank you!
        """
)


async def message_to_list_prompt(message: str):
    if prompt_list := re.findall(r"\d+\.\s(.+)", message):
        return prompt_list

    # else
    open_message = message.find("[")

    if open_message == -1:
        return None

    close_message = message.find("]")

    if close_message == -1:
        return None

    message = message[open_message : close_message + 1]

    message = message.replace("\n", "").replace("'", "\\'").replace("\\", "").strip()

    prompt_list = ast.literal_eval(message)

    return prompt_list


async def cut_prompt(message_in: str):
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
    # CUT_PROMPT_FUNC = (
    #     lambda message: f"can you cut list of prompt in the message to describe the image how to look like, return like ['...' , '...' , ...], message is {message}"
    # )
    #     CUT_PROMPT_FUNC = (
    #         lambda message: f"""
    # Given an image, I need your help to generate a clear list of prompts describing how the image looks. The prompts should be in list format. For example:

    # 1. Describe the overall scene or setting.
    # 2. Highlight any prominent objects or subjects.
    # 3. Comment on the colors and lighting.
    # 4. Provide emotional or atmospheric descriptions.
    # 5. Include any notable actions or interactions.

    # Please use the information in the provided message {message} to craft the prompts. Return your responses in the format ['...', '...', ...]. Be as detailed and imaginative as possible. Thank you!
    #         """
    #     )

    json_data = {
        "type_service": "cut_prompt",
        "prompt": CUT_PROMPT_FUNC_1(message=message_in),
    }

    # TODO: send request to server
    async with httpx.AsyncClient() as client:
        resend = True
        while resend:
            try:
                response = await client.post(
                    f"http://{state_data.SERVER_URL}/generate_service",
                    json=json_data,
                    timeout=30,
                )
                resend = False
                break
            except httpx.ReadTimeout as e:
                resend = True

    # TODO: get the result
    result = response.json()

    result_list = [
        item_dict
        | {"prompt_list": await message_to_list_prompt(message=item_dict["response"])}
        for item_dict in result
        if item_dict["state"] == "OK"
    ]

    error_message = []

    for item in result_list:
        # TODO: find the process success
        if item["prompt_list"] is not None:
            return {
                "provider": item["provider"],
                "prompt_list": item["prompt_list"],
            }

        error_message.append(f"{item['provider']}:{item['response']}")

    # TODO: choose one of theme
    # provider, message = result["provider"], result["response"]

    # prompt_list = await message_to_list_prompt(message=message)

    # if prompt_list is None:
    #     prompt_list = f"{provider}:{message}"

    return {
        "provider": "",
        "prompt_list": "",
        "error": True,
        "error_message": "\n".join(error_message),
    }


async def prompt_to_image(list_of_prompt: list[str]):
    # TODO: make the prompt to json_data request
    json_data_list = [
        {
            "type_service": "text_to_image",
            "prompt": prompt_item,
        }
        for prompt_item in list_of_prompt
    ]

    # TODO: send request to server
    async with httpx.AsyncClient() as client:
        tasks = [
            client.post(
                f"http://{state_data.SERVER_URL}/generate_service",
                json=json_data,
                timeout=10,
            )
            for json_data in json_data_list
        ]
        response = await asyncio.gather(*tasks)

    result_list_of_id = [item.json() for item in response]

    return {"result": result_list_of_id}
