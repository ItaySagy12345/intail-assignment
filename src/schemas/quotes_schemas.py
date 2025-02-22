from pydantic import BaseModel


class QuoteCreateSchema(BaseModel):
    """
    Schema for creating a new quote
    """

    slug: str
    name: str


class QuoteSchema(BaseModel):
    """
    Schema for a quote
    """

    slug: str
    name: str

    class Config:
        from_attributes=True