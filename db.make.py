import sqlalchemy as db
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Text, Boolean

engine = db.create_engine('sqlite:///childlibrary.db')
connection = engine.connect()
metadata = db.MetaData()

childlibrary = Table('childlibrary', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('author', String),
    Column('genre', Integer),
    Column('cover', String),
    Column('description', Text)
)

metadata.create_all(engine)
