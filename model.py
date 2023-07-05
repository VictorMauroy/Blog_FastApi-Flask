from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text
from typing import List

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    # Primary key and relations
    id: Mapped[int] = mapped_column(primary_key=True)
    comments: Mapped[List["Comment"]] = relationship(back_populates='user')
    posts:Mapped[List["Post"]] = relationship(back_populates='user')
    
    # Properties
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)


class Comment(Base):
    __tablename__ = "comments"

    # Primary key and relations
    id: Mapped[int] = mapped_column(primary_key=True)
    # User relation
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates='comments')
    # Post relation
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False)
    post: Mapped["Post"] = relationship(back_populates='posts')
    
    # Properties
    message: Mapped[str] = mapped_column(Text, nullable=False)

class Post(Base):
    __tablename__ = "posts"

    # Primary key and relations
    id: Mapped[int] = mapped_column(primary_key=True)
    # User relation
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user:Mapped["User"] = relationship(back_populates='posts')
    # Comment relation
    comments: Mapped[List["Comment"]] = relationship(back_populates='post')

    # Properties
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)