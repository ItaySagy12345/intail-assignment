from fastapi import Depends
from src.dependencies.db_dep import db_dep
from src.models.models import Author
from sqlalchemy.orm import Session
from typing import Union


def author_dep(slug: str, db: Session = Depends(db_dep)) -> Author:
    """
    Returns the author by its slug
    Param: slug [String]: The slug of the author to return
    Param: db [Session]: The database session
    Return: [Author]: The author db model
    Raises: ArgumentsError
    """
    
    author: Union[Author, None] = Author.find(db=db, slug=slug)
    return author