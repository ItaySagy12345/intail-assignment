from pydantic import BaseModel
from typing import Optional


class AuthorSchemaBase(BaseModel):
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
    Schema for an author
    """

    books: list[str]

    class Config:
        from_attributes=True