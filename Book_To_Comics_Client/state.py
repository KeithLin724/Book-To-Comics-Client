"""Base state for the app."""

import reflex as rx
import httpx
import asyncio
from PIL import Image
from PIL.Image import Image as pil_Image
from io import BytesIO
import time
from Book_To_Comics_Client.func import helper, book_to_comics_func as btc_func


class State(rx.State):
    """Base state for the app.

    The base state is used to store general vars used throughout the app.
    """

    """
    chat room start
    """
    question: str
    chat_history: list[tuple[str, str]]

    ai_is_thinking: bool = False

    def answer_ai_enter(self, key_event):
        if key_event == "Enter" and self.question != "":
            return self.answer_ai()

    async def answer_ai(self):
        # Our chatbot is not very smart right now...
        format_request = {
            "type_service": "chat",
            "name": "tmp",
            "prompt": self.question,
        }
        self.ai_is_thinking = True
        yield

        async with httpx.AsyncClient() as client:
            # response = await client.get("http://localhost:8000/ping")
            response = await client.post(
                "http://140.113.238.35:5000/generate_service",
                json=format_request,
                timeout=10,
            )

        res = response.json()

        answer = res.get("message")
        self.chat_history.append((self.question, ""))

        # Clear the question input.
        self.question = ""
        self.ai_is_thinking = False
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

    counter: int = 0

    ## about the front work
    zoom_image: pil_Image = ""

    is_zoomed: bool = False

    ## in book to comic button , when the user summit the text
    is_cutting_prompt: bool = False

    async def toggle_zoom(self, image: pil_Image = ""):
        self.is_zoomed = not self.is_zoomed
        self.zoom_image = image
        yield

    show_copy_in_top: bool = False

    async def copy_show(self, copy_message: str):
        """
        The `copy_show` function toggles the `show_copy_in_top` attribute, sets the clipboard to
        `copy_message`, waits for 1 second, and then toggles the `show_copy_in_top` attribute again.

        :param copy_message: The `copy_message` parameter is a string that represents the message you want
        to copy to the clipboard
        :type copy_message: str
        """
        self.show_copy_in_top = not self.show_copy_in_top
        yield rx.set_clipboard(copy_message)
        # time.sleep(1)
        await asyncio.sleep(1)
        self.show_copy_in_top = not self.show_copy_in_top
        yield

    # about the message #####

    def send(self):
        self.text_list = [i for i in range(int(self.text))]
        self.text = ""
        self.counter = 0
        yield rx.console_log("here")

    # 0: index , 1 : image , 2 : image_url , 3: prompt
    img_src_arr: list[tuple[int, Image.Image, str, str]]

    # send to server
    @rx.background
    async def get_test_image(self):
        async with self:
            self.img_src_arr = []
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
                self.img_src_arr[i] = (i, res, res_url, "cat is running")
        return

    async def get_test(self):
        if self.text != "test":
            return State.get_test_image
        return State.get_test_image_2

    @rx.background
    async def get_test_image_2(self):
        yield rx.console_log("run test 2")

        async with self:
            self.text = ""
            self.is_cutting_prompt = True
            self.img_src_arr = []
        yield

        # TODO: demo get the prompt
        # demo delay
        await asyncio.sleep(3)

        async with httpx.AsyncClient() as client:
            response = await client.get("http://140.113.238.35:5000/test_get_prompt")

        # yield rx.console_log(response.text)
        res = response.json()
        prompt_res_list = res["prompt"]

        async with self:
            self.is_cutting_prompt = False
        yield

        # TODO: update the member
        async with self:
            self.img_src_arr = [
                (
                    i,
                    "",
                    "",
                    prompt,
                )
                for i, prompt in enumerate(prompt_res_list)
            ]
            self.text = ""

        response_arr = []

        # TODO: demo use prompt to get the image
        async with httpx.AsyncClient() as client:
            tasks = [
                client.get("http://140.113.238.35:5000/test_get_image")
                for prompt in prompt_res_list
            ]
            # run in same time
            response = await asyncio.gather(*tasks)

        response_arr = [
            (
                Image.open(BytesIO(item.content)),
                helper.image_to_url(item.content),
                prompt,
            )
            for (prompt, item) in zip(prompt_res_list, response)
        ]

        # update the image
        async with self:
            self.img_src_arr = [
                (i, res, res_url, prompt)
                for i, (res, res_url, prompt) in enumerate(response_arr)
            ]

        return

    @rx.background
    async def run_book_to_comics(self):
        yield rx.console_log("run book to comics")

        # TODO: init
        async with self:
            self.is_cutting_prompt = True
            self.img_src_arr = []

        # TODO: get cut prompt
        result_prompt = await btc_func.cut_prompt(self.text)
        provider, prompt_res_list = result_prompt["provider"], result_prompt["message"]

        yield rx.console_log(f"cut prompt provider is {provider}")

        # TODO: update the member
        async with self:
            self.is_cutting_prompt = False
            self.img_src_arr = [
                (
                    i,  # index
                    "",  # image
                    "",  # image_url
                    prompt,  # prompt
                )
                for i, prompt in enumerate(prompt_res_list)
            ]

            self.text = ""

        yield

        # TODO: send cut prompt get the tasks id
        result_task_list = await btc_func.prompt_to_image(prompt_res_list)
        result_task_list = result_task_list["result"]

        # TODO: each array location wait the image is process success
        # 创建任务列表，每个任务对应一个图像处理任务
        tasks = [
            State.poll_for_image_result(index, task_id_dict)
            for index, task_id_dict in enumerate(result_task_list)
        ]

        # 并发运行所有任务
        await asyncio.gather(*tasks)
        yield

        return

    @rx.background
    async def poll_for_image_result(self, index: int, task_id_dict: dict) -> None:
        RESULT_SERVICE_FORMAT = {
            "type_service": "string",
            "unique_id": "string",
            "file_path": "string",
            "file_name": "string",
            "time": "string",
            "request_path": "string",
        }

        json_data = task_id_dict | RESULT_SERVICE_FORMAT

        while True:
            # result = await check_image_status(task_id, index)

            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "http://140.113.238.35:5000/result_service",
                    json=json_data,
                )

            result = response.json()
            # TODO: use the state code to check is it success
            # TODO: check the content type
            if result["state"] == "finished":
                result_item = result["result"]
                pass

                yield rx.console_log(f"get image number:{index}")
                break

            await asyncio.sleep(1)  # 休眠1秒后再次检查

        async with self:
            prompt = self.img_src_arr[index][-1]
            self.img_src_arr[index] = (
                index,
                Image.open(BytesIO(result_item.content)),
                helper.image_to_url(result_item.content),
                prompt,
            )
        yield

    def image_refresh(self):
        yield rx.window_alert("You clicked the image!")
        self.counter += 1

    pass
