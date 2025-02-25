from pydantic import BaseModel


class QuoteSchemaBase(BaseModel):
    """
    Abstract Schema for a Quote
    """
        
    slug: str
    name: str
    text: str
    author: str


class QuoteCreateSchema(QuoteSchemaBase):
    """
    Schema for creating a new quote
    """

    pass


class QuoteSchema(QuoteSchemaBase):
    """
    Schema for a quote to return to the client
    """

    class Config:
        from_attributes=True