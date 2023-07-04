from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text
from typing import List

from comment_model import Comment
from post_model import Post

UserBase = DeclarativeBase()

class User(UserBase):
    __tablename__ = "users"

    # Primary key and relations
    id: Mapped[int] = mapped_column(primary_key=True)
    comments: Mapped[List["Comment"]] = relationship(back_populates='user')
    posts:Mapped[List["Post"]] = relationship(back_populates='user')
    
    # Properties
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    mdp: Mapped[str] = mapped_column(nullable=False)
    