from _datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.sql import func

class Base(DeclarativeBase, AsyncAttrs):
    __abstract__ = True

    id: Mapped[int] =mapped_column(autoincrement=True, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now())



    @declared_attr.directive
    def __tablename__(cls):
        return cls.__name__.lower() + 's'

