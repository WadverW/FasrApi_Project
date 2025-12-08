from pydantic import BaseModel, Field


class IdSchema(BaseModel):
    id: int = Field(examples=[12345], gt=0)