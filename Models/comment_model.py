from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text
from typing import List

from user_model import User
from post_model import Post

CommentBase = DeclarativeBase()

class Comment(CommentBase):
    __tablename__ = "comments"

    # Primary key and relations
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates='comments')
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False)
    post: Mapped["Post"] = relationship(back_populates='posts')
    
    # Properties
    message: Mapped[str] = mapped_column(Text, nullable=False)
