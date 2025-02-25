import re
import httpx
from typing import Union
from functools import reduce
from fastapi import APIRouter, Depends
from fastapi import status
from sqlalchemy.orm import Session
from src.config.config import CONFIG
from src.errors.errors import ArgumentsError
from src.models.models import Author, Book, AuthorBook
from src.schemas.authors_schemas import AuthorSchema, AuthorCreateSchema
from src.schemas.books_schemas import BookCreateSchema
from src.schemas.author_books import AuthorBookCreateSchema
from src.generics.api_interfaces import BaseResponse
from src.dependencies.author_dep import author_dep
from src.dependencies.db_dep import db_dep


authors_router = APIRouter()

@authors_router.get("/authors/{slug}", tags=["authors", "get"], response_model=BaseResponse[AuthorSchema], status_code=status.HTTP_200_OK)
async def get_author(slug: str, author: Author = Depends(author_dep), db: Session = Depends(db_dep)):
    """
    Returns an author by its slug to the client
    """

    if not author:
        slug_parts: list[str] = re.split(r"[ .]+", slug)
        query_suffix: str = reduce(lambda acc, part: f"{acc}%20{part}", slug_parts)
        
        async with httpx.AsyncClient() as client:
            author_initial_meta = await client.get(f"{CONFIG['authors_api']['domain']}/search/authors.json?q={query_suffix}")
            author_initial_meta = author_initial_meta.json()

            author_key = ''
            if "docs" in author_initial_meta and "key" in author_initial_meta["docs"][0]:
                author_key = author_initial_meta["docs"][0]["key"]
            else:
                raise ArgumentsError(message="Could not find author information")
            
            author_meta = await client.get(f"{CONFIG['authors_api']['domain']}/authors/{author_key}.json")
            author_meta = author_meta.json()
            author_birth_date = author_meta.get("birth_date", '')
            author_death_date = author_meta.get("death_date", None)
            
            limit: int = 5
            books_meta = await client.get(f"{CONFIG['authors_api']['domain']}/authors/{author_key}/works.json?limit={limit}")
            books_meta = books_meta.json()
            books = books_meta.get("entries", None)

        new_author = AuthorCreateSchema(
            api_id=author_key,
            slug=slug,
            name=slug,
            birth_date=author_birth_date,
            death_date=author_death_date
        )
        author = Author.create(db=db, data=new_author)

        if books:
            new_books: list[Book] = []
            for book in books:
                slug: str = book["title"]
                book_exists: Union[Book, None] = Book.find(db=db, slug=book["title"])

                if not book_exists:
                    create_book = BookCreateSchema(
                        api_id=book["key"],
                        slug=slug,
                        name=slug
                    )
                    new_book: Book = Book.create(db=db, data=create_book)
                    new_books.append(new_book)
                else:
                    new_books.append(book_exists)

            for new_book in new_books:
                create_author_book = AuthorBookCreateSchema(
                    author_id=author.id,
                    book_id=new_book.id
                )
                AuthorBook.create(db=db, data=create_author_book)

    author = Author.find(db=db, slug=author.slug)
    author_data: AuthorSchema = AuthorSchema.model_validate(author)
    return BaseResponse(data=author_data)
