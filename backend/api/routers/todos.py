from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["todos"])


class TodoResponse(BaseModel):
    """Todo response schema."""
    id: int
    title: str
    completed: bool


SAMPLE_TODOS = [
    TodoResponse(id=1, title="Learn FastAPI", completed=True),
    TodoResponse(id=2, title="Build a todo API", completed=False),
    TodoResponse(id=3, title="Write tests", completed=False),
]


@router.get("/api/v1/todos", response_model=list[TodoResponse])
async def get_todos():
    """
    Retrieve all todo items.
    
    Returns:
        list[TodoResponse]: List of todo items with id, title, and completed status.
    """
    return SAMPLE_TODOS
