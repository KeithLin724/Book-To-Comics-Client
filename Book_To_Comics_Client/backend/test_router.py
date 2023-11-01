from fastapi import APIRouter


test_router = APIRouter()


@test_router.get("/test")
async def test():
    # from base import FOLDER_PATH

    return {"result": "ready"}


@test_router.get("/test_result")
async def test_result():
    return {"result": "not ready"}


@test_router.post("/test_result")
async def test_result_post():
    return {"result": "not ready"}
