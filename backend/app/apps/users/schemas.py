from pydantic import BaseModel, EmailStr, Field, StringConstraints, field_validator
from typing import Annotated
from password_strength import PasswordPolicy
from apps.core.schemas import IdSchema

class PasswordUserSchema(BaseModel):
    password: str = Field(examples=["GHHJdjdk5456+_+"])

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str | None:
        password_policy = PasswordPolicy.from_names(
            length=8,
            numbers=1,
            uppercase=1,
            special=1,
        )
        errors = password_policy.test(value)
        if not errors:
            return value
        error_messages = []
        for error in errors:
            error_name = error.name()
            if error_name == "length":
                error_messages.append(
                    f"Password must be at least {error.length} characters long"
                )
            elif error_name == "uppercase":
                error_messages.append(
                    f"Password must contain at least {error.count} uppercase letter(s)"
                )
            elif error_name == "numbers":
                error_messages.append(
                    f"Password must contain at least {error.count} digit(s)"
                )
            elif error_name == "special":
                error_messages.append(
                    f"Password must contain at least {error.count} special character(s)"
                )
            raise ValueError(';'.join(error_messages))



class BaseUserSchema(BaseModel):
    email: EmailStr = Field(describtion="User Email", examples=["example@gmail.com"])
    name: Annotated[
        str, StringConstraints(
            pattern=r"^[A-Za-zА-Яа-яЁё'-]{2,50}(\s[A-Za-zА-Яа-яЁё'-]{2,50})*$",
            strip_whitespace=True,
            min_length=3,
            max_length=50

           )
        ]


class RegisterUserSchema(BaseUserSchema, PasswordUserSchema):
    pass
from typing import Annotated

class PasswordUserSchema(BaseModel):
    password: str = Field(examples=["GHHJdjdk5456+_+"])

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str | None:
        password_policy = PasswordPolicy.from_names(
            length=8,
            numbers=1,
            uppercase=1,
            special=1,
        )
        errors = password_policy.test(value)
        if not errors:
            return value
        error_messages = []
        for error in errors:
            error_name = error.name()
            if error_name == "length":
                error_messages.append(
                    f"Password must be at least {error.length} characters long"
                )
            elif error_name == "uppercase":
                error_messages.append(
                    f"Password must contain at least {error.count} uppercase letter(s)"
                )
            elif error_name == "numbers":
                error_messages.append(
                    f"Password must contain at least {error.count} digit(s)"
                )
            elif error_name == "special":
                error_messages.append(
                    f"Password must contain at least {error.count} special character(s)"
                )
            raise ValueError(';'.join(error_messages))



class BaseUserSchema(BaseModel):
    email: EmailStr = Field(describtion="User Email", examples=["example@gmail.com"])
    name: Annotated[
        str, StringConstraints(
            pattern=r"^[A-Za-zА-Яа-яЁё'-]{2,50}(\s[A-Za-zА-Яа-яЁё'-]{2,50})*$",
            strip_whitespace=True,
            min_length=3,
            max_length=50

           )
        ]


class RegisterUserSchema(BaseUserSchema, PasswordUserSchema):
    pass

class RegisteredSchema(BaseUserSchema, IdSchema):
    pass