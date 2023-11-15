"""Base state for the app."""

import reflex as rx
import httpx
import asyncio


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

    text: str
    text_list: list[int] = []
    img_src: str

    counter: int = 0

    def send(self):
        self.text_list = [i for i in range(int(self.text))]
        self.text = ""
        self.counter = 0
        yield rx.console_log("here")

    def image_refresh(self):
        self.img_src = ""
        self.counter += 1

    pass
