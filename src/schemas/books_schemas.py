from pydantic import BaseModel


class BookSchemaBase(BaseModel):
    slug: str
    name: str
    

class BookCreateSchema(BookSchemaBase):
    """
    Schema for creating a new Book
    """

    api_id: str


class BookSchema(BookSchemaBase):
    """
    Schema for a Book
    """

    class Config:
        from_attributes=True