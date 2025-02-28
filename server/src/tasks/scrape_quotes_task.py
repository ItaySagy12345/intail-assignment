from typing import Union
from sqlalchemy import and_
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from src.services.author_meta_service import author_meta_service
from src.utils.dynamic_content_scraper import DynamicContentScraper
from src.database.database_session import DatabaseSession
from src.schemas.quotes_schemas import QuoteCreateSchema
from src.models.models import Quote
from src.errors.errors import InternalServerError
from src.utils.logger import logger
from src.utils.string_helpers import getTimestamp
from src.models.models import Author, Book, AuthorBook
from src.schemas.authors_schemas import AuthorCreateSchema, AuthorSchema
from src.schemas.books_schemas import BookCreateSchema
from src.schemas.author_books import AuthorBookCreateSchema
from src.cache.config import redis_cache
from src.utils.string_helpers import format_slug


MAX_BOOKS = 5
MAX_PAGES = 5
QUOTES_PER_PAGE = 10
MAX_QUOTES = MAX_PAGES * QUOTES_PER_PAGE

async def scrape_quotes_task() -> None:
    """
    Task for scraping quotes from the designated web page
    Return None
    """

    base_url = f"https://quotes.toscrape.com/js"
    scraper: Union[DynamicContentScraper, None] = None

    try:        
        with DatabaseSession() as db:    
            for page in range(1, MAX_PAGES + 1):
                url_paginated = f"{base_url}/page/{page}/"
                logger.info(msg=f"[BEGIN]: Scraping quotes from: {url_paginated} at {getTimestamp()}")
                scraper = DynamicContentScraper(url=url_paginated)
                quote_elements: list[WebElement] = scraper.scrape(key="quote")

                for quote_element in quote_elements:
                    quote_author: str = quote_element.find_element(By.CLASS_NAME, "author").text
                    quote_text: str = quote_element.find_element(By.CLASS_NAME, "text").text
                    quote_slug: str = format_slug(slug=f"{quote_author[:10]}-{quote_text[:15]}")
                    quote_query = (Quote.slug == quote_slug)
                    quote_exists: Union[Quote, None] = Quote.find(db=db, query=quote_query)
                    quote_count: int = Quote.count(db=db)
                    if quote_exists is None:
                        if quote_count >= MAX_QUOTES:
                            logger.info(msg=f"[ALERT]: Quote {quote_slug} from: {url_paginated} at {getTimestamp()} is new") 
                        else:
                            create_quote = QuoteCreateSchema(
                                slug=quote_slug,
                                text=quote_text,
                                author=format_slug(slug=quote_author)
                            )
                            Quote.create(db, create_quote)

                            (author_meta, books_meta) = await author_meta_service(author=quote_author, book_limit=MAX_BOOKS)
                            author_key: str = author_meta["key"]
                            author_name: str = author_meta["name"]
                            author_slug: str = format_slug(slug=author_meta["name"])
                            author_birth_date: str = author_meta.get("birth_date", '')
                            author_death_date: str = author_meta.get("death_date", None)
                            author_query = (Author.slug == author_slug)
                            author_slug_valid: bool = bool(author_slug)
                            author_exists: Union[Author, None] = Author.find(db=db, query=author_query)
                            if author_slug_valid and author_exists is None:
                                create_author = AuthorCreateSchema(
                                    api_id=author_key,
                                    slug=author_slug,
                                    name=author_name,
                                    birth_date=author_birth_date,
                                    death_date=author_death_date
                                )
                                new_author = Author.create(db=db, data=create_author)
                            
                            books: Union[list[dict], None] = books_meta.get("entries", None)
                            new_books: list[Book] = []
                            if books or len(books) >= 1:
                                for book in books:
                                    book_key: str = book["key"]
                                    book_name: str = book["title"]
                                    book_slug: str = format_slug(slug=book["title"])
                                    book_query = (Book.slug == book_slug)
                                    book_exists: Union[Book, None] = Book.find(db=db, query=book_query)
                                    if book_exists is None:
                                        create_book = BookCreateSchema(
                                            api_id=book_key,
                                            slug=book_slug,
                                            name=book_name
                                        )
                                        new_book: Book = Book.create(db=db, data=create_book)
                                        new_books.append(new_book)
                                    else:
                                        new_books.append(book_exists)

                                for new_book in new_books:
                                    author_book_query = and_(AuthorBook.author_id == new_author.id, AuthorBook.book_id == new_book.id)
                                    author_book_exists: Union[AuthorBook, None] = AuthorBook.find(db=db, query=author_book_query)
                                    if author_book_exists is None:
                                        create_author_book = AuthorBookCreateSchema(
                                            author_id=new_author.id,
                                            book_id=new_book.id
                                        )
                                        AuthorBook.create(db=db, data=create_author_book)
                            
                            cache_books: list[str] = [book.name for book in new_books]
                            cache_author = AuthorSchema(
                                slug=new_author.slug,
                                name=new_author.name,
                                birth_date=new_author.birth_date,
                                death_date=new_author.death_date,
                                books=cache_books
                            )
                            cache_author_key = f"author:{new_author.slug}"
                            cached_author_exists: Union[str, None] = await redis_cache.get(key=cache_author_key)
                            if cached_author_exists is None:
                                await redis_cache.set(key=cache_author_key, value=cache_author.model_dump_json())

                scraper.close()
                logger.info(msg=f"[END]: Scraping quotes from: {url_paginated} at {getTimestamp()}")

    except Exception as e:
        raise InternalServerError(message=f"Error scraping content: {e}")

    finally:
        if scraper:
            scraper.close()