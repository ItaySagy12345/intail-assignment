from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from src.database.crud_base import CrudBase


Base = declarative_base()

class Quote(CrudBase, Base):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, unique=True, index=True)
    name = Column(String, index=True)