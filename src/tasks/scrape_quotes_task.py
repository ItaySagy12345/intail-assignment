from typing import Union
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from src.utils.dynamic_content_scraper import DynamicContentScraper
from src.database.database_session import DatabaseSession
from src.schemas.quotes_schemas import QuoteCreateSchema
from src.utils.slug_generator import slug_generator
from src.models.models import Quote
from src.errors.errors import InternalServerError
from src.utils.logger import logger
from src.utils.string_helpers import getTimestamp


MAX_PAGES = 5
QUOTES_PER_PAGE = 5
MAX_QUOTES = MAX_PAGES * QUOTES_PER_PAGE

def scrape_quotes_task() -> None:
    """
    Task for scraping quotes from the designated web page
    Return None
    """
            
    with DatabaseSession() as db:
        base_url = f"https://quotes.toscrape.com/js"

        quote_count: int = Quote.count(db=db)
        if quote_count >= MAX_QUOTES:
            logger.info(msg=f"[ALERT]: Skipped scraping quotes from: {base_url} at {getTimestamp()}")
            return

        scraper: Union[DynamicContentScraper, None] = None
        pages: int = 5

        try:
            for page in range(1, pages + 1):
                url = f"{base_url}/page/{page}/"
                logger.info(msg=f"[BEGIN]: Scraping quotes from: {url} at {getTimestamp()}")
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
  
                logger.info(msg=f"[END]: Scraping quotes from: {url} at {getTimestamp()}")
                scraper.close()

        except Exception as e:
            raise InternalServerError(message=f"Error scraping content: {e}")

        finally:
            if scraper:
                scraper.close()