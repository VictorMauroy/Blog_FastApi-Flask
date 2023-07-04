from sqlalchemy import create_engine

from Models.user_model import UserBase
from Models.comment_model import CommentBase
from Models.post_model import PostBase

database_url = "sqlite:///./database.db"
engine = create_engine(database_url)

# Generate database from the tables linked to the "Base".
# Every entity that inherit Base will be obtained and generated
UserBase.metadata.create_all(engine)
PostBase.metadata.create_all(engine)
CommentBase.metadata.create_all(engine)