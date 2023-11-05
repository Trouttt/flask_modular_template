#from sqlalchemy import create_engine
#import sqlalchemy
#from sqlalchemy.engine import URL
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, relationship, backref, sessionmaker
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, create_engine
from datetime import datetime


Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    year = Column(Integer(), nullable=False)
    publisher = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    author_id = Column(Integer(), ForeignKey('authors.id'))
    author = relationship('Author', back_populates='books')
    
    category_id = Column(Integer(), ForeignKey('categories.id'))
    category = relationship('Category', back_populates='books')

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    books = relationship('Book', back_populates='author')

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    books = relationship('Book', back_populates='category')

def initialize_db():
    url = URL.create(
        drivername="postgresql",
        username="postgres",
        password="postgres",
        host="localhost",
        database="postgres"
    )

    engine = create_engine(url)
    Base.metadata.create_all(engine)

    return engine

#def initialize_db(app):
#    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
#    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#    db = sqlalchemy(app)
#
#    return db





