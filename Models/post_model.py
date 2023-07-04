from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text
from typing import List

from user_model import User
from comment_model import Comment

PostBase = DeclarativeBase()

class Post(PostBase):
    __tablename__ = "posts"

    # Primary key and relations
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user:Mapped["User"] = relationship(back_populates='posts')
    comments: Mapped[List["Comment"]] = relationship(back_populates='post')

    # Properties
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    