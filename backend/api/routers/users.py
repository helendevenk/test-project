from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/users", tags=["users"])

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    """获取用户信息"""
    return UserResponse(id=user_id, name="test", email="test@example.com")
