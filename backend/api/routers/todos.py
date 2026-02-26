from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1", tags=["todos"])


class TodoResponse(BaseModel):
    """Todo 响应模型"""
    id: int
    title: str
    completed: bool


# 模拟 todo 数据（实际项目中应从数据库获取）
MOCK_TODOS = [
    {"id": 1, "title": "Learn FastAPI", "completed": True},
    {"id": 2, "title": "Build a REST API", "completed": False},
    {"id": 3, "title": "Write tests", "completed": False},
]


@router.get("/todos", response_model=list[TodoResponse])
async def get_todos():
    """获取所有 todo 列表"""
    return MOCK_TODOS
