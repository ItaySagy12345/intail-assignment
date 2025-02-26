from pydantic import BaseModel


class AuthorBookCreateSchema(BaseModel):
    """
    Schema for creating a new AuthorBook
    """

    author_id: int
    book_id: int