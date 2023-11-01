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

    async def answer(self):
        # Our chatbot is not very smart right now...
        answer = "I don't know!"
        self.chat_history.append((self.question, ""))

        # Clear the question input.
        self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield

        for i in range(len(answer)):
            # Pause to show the streaming effect.
            await asyncio.sleep(0.1)
            # Add one letter at a time to the output.
            self.chat_history[-1] = (
                self.chat_history[-1][0],
                answer[: i + 1],
            )
            yield

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
            # for pid in range(10):
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
        result = self.get_request("http://localhost:8000/ping/")
        async with self:
            self.res = result.text

    pass
