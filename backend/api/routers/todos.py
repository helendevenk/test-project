from fastapi import APIRouter

from pydantic import BaseModel


class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool


router = APIRouter(prefix="/api/v1/todos", tags=["todos"])


# 模拟 todo 数据
TODOS = [
    {"id": 1, "title": "Learn FastAPI", "completed": True},
    {"id": 2, "title": "Build a REST API", "completed": False},
    {"id": 3, "title": "Write documentation", "completed": False},
]


@router.get("", response_model=list[TodoResponse])
async def get_todos():
    """返回 todo 列表"""
    return TODOS
