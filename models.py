import sqlalchemy as db
import json
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Boolean, Text
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, IntegerField
from wtforms.validators import DataRequired

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
                	

class BooksForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    genre = StringField('genre', validators=[DataRequired()])
    cover = StringField('cover', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
  
class Books:

  def get_book(self, id):
    sql = childlibrary.select().where(childlibrary.c.id == id)
    result = connection.execute(sql)
    row = result.fetchone()
    return row

 
  def make_book(self, title, author, genre, cover, description):
    sql = childlibrary.insert().values(title = title, 
                                      author = author,
                                      genre = genre,
                                      cover = cover,
                                      description = description)
    result = connection.execute(sql, [{'title': title, 'author': author, 'genre': genre,
                                       'cover': cover, 'description': description}])
    connection.commit()


  def delete_book(self, id):
    book_id = self.get_book(id)
    if book_id:
      statement = childlibrary.delete().where(childlibrary.c.id == id)
      connection.execute(statement)
      connection.commit()
      return True
    return False


  def update(self, id):
    book_id = self.get_book(id)
    if book_id:

      if book_id[6]:
        statement=childlibrary.update().where(childlibrary.c.id==id)
      else:
        statement=childlibrary.update().where(childlibrary.c.id==id)
      connection.execute(statement)
      connection.commit()

      return True
    return False

  def __del__(self):
    connection.close()


books = Books()