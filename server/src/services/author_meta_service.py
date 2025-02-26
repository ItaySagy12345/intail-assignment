import re
import httpx
from functools import reduce
from fastapi import Response
from src.config.config import CONFIG
from src.errors.errors import ArgumentsError


async def author_meta_service(author: str, book_limit: int) -> tuple[dict, dict]:
    """
    Service that returns the given author's metadata including the books they have written per the book_limit parameter
    Param: author [String]: The name of the author
    Param: book_limit [Integer]: The number of the author's books to fetch
    Return [tuple[dict, dict]]: A tuple with the author_meta and books_meta response objects
    """
    
    timeout = httpx.Timeout(10.0)
    slug_parts: list[str] = re.split(r"[ .]+", author)
    query_suffix: str = reduce(lambda acc, part: f"{acc}%20{part}", slug_parts)
    
    async with httpx.AsyncClient(timeout=timeout) as client:
        author_initial_meta = await client.get(f"{CONFIG['authors_api']['domain']}/search/authors.json?q={query_suffix}")
        author_initial_meta = author_initial_meta.json()

        if "docs" in author_initial_meta and "key" in author_initial_meta["docs"][0]:
            author_key: str = author_initial_meta["docs"][0]["key"]
        else:
            raise ArgumentsError(message="Could not find author information")
        
        author_meta: Response = await client.get(f"{CONFIG['authors_api']['domain']}/authors/{author_key}.json")
        author_meta: dict = author_meta.json()

        books_meta: Response = await client.get(f"{CONFIG['authors_api']['domain']}/authors/{author_key}/works.json?limit={book_limit}")
        books_meta: dict = books_meta.json()

    return (author_meta, books_meta)