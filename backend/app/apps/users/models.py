from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from apps.core.base_models import Base


class User(Base):
    name:Mapped[str]=mapped_column()
    email:Mapped[str]=mapped_column(unique=True)
    hashed_password:Mapped[str]