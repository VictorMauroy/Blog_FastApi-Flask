from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///database.db", echo=True)

# with engine.connect() as cnx:
#     result = cnx.execute(text(
#     """
#     SELECT 'hello'
#     """
#     ))
#     print(result.all())