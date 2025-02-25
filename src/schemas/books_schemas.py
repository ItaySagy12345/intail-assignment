from pydantic import BaseModel


class BookSchemaBase(BaseModel):    
    """
    Abstract Schema for a book
    """

    slug: str
    name: str
    

class BookCreateSchema(BookSchemaBase):
    """
    Schema for creating a new Book
    """

    api_id: str


class BookSchema(BookSchemaBase):
    """
    Schema for a Book to return to the client
    """

    class Config:
        from_attributes=True