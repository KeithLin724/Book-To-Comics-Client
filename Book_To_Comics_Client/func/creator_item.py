from pydantic import BaseModel
from typing import Optional
import asyncio


class User(BaseModel):
    GITHUB_API = lambda user_name: f"https://api.github.com/users/{user_name}"
    name: Optional[str] = ""
    login: str
    # icon
    avatar_url: Optional[str] = ""
    html_url: str
    followers: int
    # info
    bio: Optional[str] = ""
    company: Optional[str] = ""
    location: Optional[str] = ""
    public_repos: int
    public_gists: int

    @staticmethod
    async def parse_obj_with_async(obj):
        return await asyncio.to_thread(User.parse_obj, obj)
