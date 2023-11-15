import base64


def image_to_url(image_content: bytes) -> str:
    """
    The function `image_to_url` converts image content into a data URI string.

    :param image_content: The `image_content` parameter is expected to be a bytes object that represents
    the content of an image file
    :type image_content: bytes
    :return: a string that represents the image content as a data URI.
    """
    image_base64 = base64.b64encode(image_content).decode("utf-8")
    data_uri = f"data:image/png;base64,{image_base64}"
    return data_uri


def image_to_markdown(image_url: str) -> str:
    return f"![Image]({image_url})"
