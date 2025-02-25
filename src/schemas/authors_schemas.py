from pydantic import BaseModel
from typing import Optional
from src.schemas.books_schemas import BookSchema


class AuthorSchemaBase(BaseModel):
    """
    Abstract Schema for an author
    """
        
    slug: str
    name: str
    birth_date: str
    death_date: Optional[str] = None


class AuthorCreateSchema(AuthorSchemaBase):
    """
    Schema for creating a new author
    """

    api_id: str


class AuthorSchema(AuthorSchemaBase):
    """
    Schema for an author to return to the client
    """

    books: list[BookSchema]

    class Config:
        from_attributes=True