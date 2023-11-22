import asyncio
import httpx  # 确保使用 pip 安装此库：pip install httpx


async def check_image_status(task_id, index):
    # async with httpx.AsyncClient() as client:
    #     response = await client.get(f"/check_image_state?task_id={task_id}")
    #     response.raise_for_status()
    #     return response.json()
    await asyncio.sleep(1 / (index + 1) * 3)
    return {
        "state": "finished",
        "result": f"ok {task_id}",
    }


async def poll_for_image_result(task_id, results, index):
    while True:
        result = await check_image_status(task_id, index)

        if result["state"] == "finished":
            results[index] = result["result"]
            print(results)
            return

        await asyncio.sleep(1)  # 休眠1秒后再次检查


# 使用多个任务的示例
async def main_example():
    task_ids = ["task_id_1", "task_id_2"]
    results = [""] * len(task_ids)  # 用空字符串初始化结果数组

    # 创建任务列表，每个任务对应一个图像处理任务
    tasks = [
        poll_for_image_result(task_id, results, index)
        for index, task_id in enumerate(task_ids)
    ]

    # 并发运行所有任务
    await asyncio.gather(*tasks)

    # 打印最终结果
    print("最终结果:", results)


# 运行 asyncio 事件循环
# asyncio.run(main_example())
