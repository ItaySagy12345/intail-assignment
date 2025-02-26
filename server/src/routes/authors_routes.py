import json
from fastapi import APIRouter
from fastapi import status
from src.errors.errors import ArgumentsError
from src.schemas.authors_schemas import AuthorSchema
from src.generics.api_interfaces import BaseResponse
from src.cache.config import redis_cache


authors_router = APIRouter()

@authors_router.get("/authors/{slug}", tags=["authors", "get"], response_model=BaseResponse[AuthorSchema], status_code=status.HTTP_200_OK)
async def get_author(slug: str):
    """
    Returns an author by its slug to the client
    """

    cache_author_key = f"author:{slug}"
    cached_author = await redis_cache.get(key=cache_author_key)
    if cached_author is None:
        raise ArgumentsError(message="Could not find author information")

    author_data = json.loads(cached_author)
    author_schema = AuthorSchema(
        slug=author_data['slug'],
        name=author_data['name'],
        birth_date=author_data['birth_date'],
        death_date=author_data['death_date'],
        books=author_data['books']
    )
    return BaseResponse(data=author_schema)