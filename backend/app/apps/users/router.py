from fastapi import APIRouter, status
from apps.users.schemas import RegisteredSchema
from apps.users.schemas import RegisterUserSchema
users_router = APIRouter()

@users_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(new_user: RegisterUserSchema) -> RegisteredSchema:
    created_user = RegisteredSchema(id=12345, **new_user.dict())
    return created_user