from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from src.database.crud_base import CrudBase
from sqlalchemy.orm import relationship

Base = declarative_base()

class Quote(CrudBase, Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    text = Column(String, index=True)
    author = Column(String, index=True)


class AuthorBook(CrudBase, Base):
    __tablename__ = 'authors_books'

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey('authors.id'), index=True)
    book_id = Column(Integer, ForeignKey('books.id'), index=True)


class Book(CrudBase, Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    api_id = Column(String, unique=True, index=True)
    slug = Column(String, unique=True, index=True)
    name = Column(String, index=True)

    authors = relationship("Author", secondary="authors_books", back_populates="books")


class Author(CrudBase, Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    api_id = Column(String, unique=True, index=True)
    slug = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    birth_date = Column(String, index=True)
    death_date = Column(String, index=True, nullable=True)

    books = relationship("Book", secondary="authors_books", back_populates="authors")