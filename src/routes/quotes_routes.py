from fastapi import APIRouter, Depends
from fastapi import status
from sqlalchemy.orm import Session
from src.generics.api_interfaces import ApiFilter
from src.models.models import Quote
from src.schemas.quotes_schemas import QuoteSchema
from src.generics.api_interfaces import BaseResponse
from src.dependencies.db_dep import db_dep


quotes_router = APIRouter()

@quotes_router.get("/quotes", tags=["quotes", "list"], response_model=BaseResponse[list[QuoteSchema]], status_code=status.HTTP_200_OK)
async def list_quotes(page: int, size: int, db: Session = Depends(db_dep)):
    """
    Returns a list of quotes back to the client
    """

    quotes: list[Quote] = Quote.list(db=db, filter=ApiFilter(page=page, size=size))
    quotes_data: list[QuoteSchema] = [QuoteSchema.model_validate(quote) for quote in quotes]
    return BaseResponse(data=quotes_data)