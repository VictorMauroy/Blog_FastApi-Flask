from sqlalchemy import create_engine

from model import Base

database_url = "sqlite:///./database.db"
engine = create_engine(database_url)

# Generate database from the tables linked to the "Base".
# Every entity that inherit Base will be obtained and generated
Base.metadata.create_all(bind=engine)
