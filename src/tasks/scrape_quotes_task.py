from sqlalchemy.orm import Session
from src.database.database_session import DatabaseSession
from src.utils.dynamic_content_scraper import DynamicContentScraper
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from src.dependencies.db_dep import db_dep
from src.schemas.quotes_schemas import QuoteCreateSchema
from src.utils.slug_generator import slug_generator
from src.models.models import Quote
from src.errors.errors import InternalServerError
from typing import Union


def scrape_quotes_task() -> None:
    with DatabaseSession() as db:
        scraper: Union[DynamicContentScraper, None] = None
        pages: int = 5

        try:
            for page in range(1, pages + 1):
                url = f"https://quotes.toscrape.com/js/page/{page}/"
                scraper = DynamicContentScraper(url)
                quote_elements: list[WebElement] = scraper.scrape(key="quote")

                for quote_element in quote_elements:
                    author: str = quote_element.find_element(By.CLASS_NAME, "author").text
                    text: str = quote_element.find_element(By.CLASS_NAME, "text").text
                    name: str = f"{author[:10]}-{text[:5]}"
                    slug: str = slug_generator(db=db, name=name, model=Quote)

                    create_quote = QuoteCreateSchema(
                        name=name,
                        slug=slug,
                        text=text,
                        author=author
                    )

                    Quote.create(db, create_quote)

                scraper.close()

        except Exception as e:
            raise InternalServerError(message=f"Error scraping content: {e}")

        finally:
            if scraper:
                scraper.close()
