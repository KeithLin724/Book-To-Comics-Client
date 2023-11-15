"""Base state for the app."""

import reflex as rx
import httpx
import asyncio
from .func import helper
from PIL import Image
from io import BytesIO


class State(rx.State):
    """Base state for the app.

    The base state is used to store general vars used throughout the app.
    """

    """
    chat room start
    """
    question: str
    chat_history: list[tuple[str, str]]

    async def answer_ai(self):
        # Our chatbot is not very smart right now...
        format_request = {
            "type_service": "chat",
            "name": "tmp",
            "prompt": self.question,
        }
        async with httpx.AsyncClient() as client:
            # response = await client.get("http://localhost:8000/ping")
            response = await client.post(
                "http://140.113.238.35:5000/generate_service",
                json=format_request,
            )

        res = response.json()

        answer = res.get("message")
        self.chat_history.append((self.question, ""))

        # Clear the question input.
        self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield

        for i in range(len(answer)):
            # Pause to show the streaming effect.
            await asyncio.sleep(0.05)
            # Add one letter at a time to the output.
            self.chat_history[-1] = (
                self.chat_history[-1][0],
                answer[: i + 1],
            )
            yield

    # async def answer(self):
    #     # Our chatbot is not very smart right now...

    #     async with httpx.AsyncClient() as client:
    #         response = await client.get("http://localhost:8000/ping")

    #     answer = "I don't know! " + response.text + "`hello world`"
    #     self.chat_history.append((self.question, ""))

    #     # Clear the question input.
    #     self.question = ""
    #     # Yield here to clear the frontend input before continuing.
    #     yield

    #     for i in range(len(answer)):
    #         # Pause to show the streaming effect.
    #         await asyncio.sleep(0.05)
    #         # Add one letter at a time to the output.
    #         self.chat_history[-1] = (
    #             self.chat_history[-1][0],
    #             answer[: i + 1],
    #         )
    #         yield

    """
    chat room end
    """

    posts: list[str] = []

    @rx.background
    async def get_posts(self):
        async with httpx.AsyncClient() as client:
            for pid in range(10):
                response = await client.get(f"https://dummyjson.com/products/{pid}")
                async with self:
                    self.posts.append(response.text)

    res: str = ""

    @rx.background
    async def get_posts_host(self):
        async with httpx.AsyncClient() as client:
            response = await client.get("http://localhost:8000/ping")
            async with self:
                # self.posts.append(response.text)
                self.res = response.text

    @rx.background
    async def get_request(self, url):
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            async with self:
                self.res = f"code : {response.status_code} , {response.text}"

    # @rx.background
    async def test_get_request(self):
        async with httpx.AsyncClient() as client:
            response = await client.get("http://localhost:8000/ping")
        self.res = response.text
        # async with self:
        #     self.res = result.text

    ############################

    text: str
    text_list: list[int] = []
    img_src: str

    counter: int = 0

    def send(self):
        self.text_list = [i for i in range(int(self.text))]
        self.text = ""
        self.counter = 0
        yield rx.console_log("here")

    img_src_arr: list[tuple[int, Image.Image]]

    def copy_show(self, image_url):
        yield rx.set_clipboard(image_url)
        yield rx.window_alert("Copied to clipboard!")

    # send to server
    @rx.background
    async def get_test_image(self):
        async with self:
            self.img_src_arr = [(i, "") for i in range(int(self.text))]
            self.text = ""

        response_arr = []
        async with httpx.AsyncClient() as client:
            for _ in self.img_src_arr:
                response = await client.get("http://140.113.238.35:5000/test_get_image")

                response_arr.append(
                    (
                        Image.open(BytesIO(response.content)),
                        helper.image_to_url(response.content),
                    )
                )

        async with self:
            for i, (res, res_url) in enumerate(response_arr):
                self.img_src_arr[i] = (i, res, res_url)
        return

    # def send_new(self):
    #     self.text_list = [i for i in range(int(self.text))]
    #     self.text = ""
    #     yield rx.console_log("here")

    def image_refresh(self):
        yield rx.window_alert("You clicked the image!")
        self.counter += 1

    pass
