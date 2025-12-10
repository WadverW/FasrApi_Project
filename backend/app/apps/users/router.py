from fastapi import APIRouter, status
from apps.users.schemas import RegisteredSchema
from apps.users.schemas import RegisterUserSchema
from apps.auth.password_handler import PasswordEncrypt

users_router = APIRouter()

@users_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(new_user: RegisterUserSchema) -> RegisteredSchema:
    created_user = RegisteredSchema(id=12345, **new_user.dict())

    # _hash = await PasswordEncrypt.get_password_hash(new_user.password)
    # verify = await PasswordEncrypt.verify_password(new_user.password, _hash)

    return created_user