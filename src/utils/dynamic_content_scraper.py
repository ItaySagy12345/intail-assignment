from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from src.errors.errors import InternalServerError


class DynamicContentScraper:
    def __init__(self, url: str) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        self.driver = driver

    def scrape(self, key: str) -> list[WebElement]:
        try:
            content: list[WebElement] = self.driver.find_elements(By.CLASS_NAME, key)
            return content
        except Exception as e:
            raise InternalServerError(message=f"Error scraping content: {e}")
    
    def close(self) -> None:
        self.driver.quit()
