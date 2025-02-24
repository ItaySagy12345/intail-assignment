import re
import requests
from functools import reduce
from fastapi import APIRouter, Depends
from fastapi import status
from sqlalchemy.orm import Session
from src.config.config import CONFIG
from src.models.models import Author, Book, AuthorBook
from src.schemas.authors_schemas import AuthorSchema, AuthorCreateSchema
from src.schemas.books_schemas import BookCreateSchema
from src.schemas.author_books import AuthorBookCreateSchema
from src.generics.api_interfaces import BaseResponse
from src.dependencies.author_dep import author_dep
from src.dependencies.db_dep import db_dep
from src.utils.slug_generator import slug_generator
from typing import Union


authors_router = APIRouter()

@authors_router.get("/authors/{slug}", tags=["authors", "get"], response_model=BaseResponse[AuthorSchema], status_code=status.HTTP_200_OK)
async def get_item(slug: str, author: Author = Depends(author_dep), db: Session = Depends(db_dep)):
    """
    Returns an author by its slug to the client
    """

    if not author:
        slug_parts: list[str] = re.split(r"[ .]+", slug)
        query_suffix: str = reduce(lambda acc, part: f"{acc}%20{part}", slug_parts)
        author_initial_meta: dict = requests.get(f"{CONFIG['authors_api']['domain']}/search/authors.json?q={query_suffix}").json()
        author_key: str = author_initial_meta["docs"][0]["key"]

        author_meta: dict = requests.get(f"{CONFIG['authors_api']['domain']}/authors/{author_key}.json").json()
        author_birth_date: str = author_meta["birth_date"]
        author_death_date: Union[str, None] = author_meta["death_date"] if hasattr(author_meta, "death_date") else None
 
        limit: int = 5
        books_meta: dict = requests.get(f"{CONFIG['authors_api']['domain']}/authors/{author_key}/works.json?limit={limit}").json()
        books: list = books_meta["entries"]

        # Create author
        new_author = AuthorCreateSchema(
            api_id=author_key,
            slug=author_meta["name"],
            name=author_meta["name"],
            birth_date=author_birth_date,
            death_date=author_death_date
        )
        author = Author.create(db=db, data=new_author)

        # Create books
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

        # Create AuthorBooks
        for new_book in new_books:
            create_author_book = AuthorBookCreateSchema(
                author_id=author.id,
                book_id=new_book.id
            )

            AuthorBook.create(db=db, data=create_author_book)

    author = Author.find(db=db, slug=author.slug)
    author_data: AuthorSchema = AuthorSchema.model_validate(author)
    return BaseResponse(data=author_data)