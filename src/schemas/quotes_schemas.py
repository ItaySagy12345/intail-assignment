from pydantic import BaseModel


class QuoteSchemaBase(BaseModel):
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
    Schema for a quote
    """

    class Config:
        from_attributes=True