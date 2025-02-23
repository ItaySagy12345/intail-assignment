from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from contextlib import asynccontextmanager
from src.routes.home_route import home_router
from src.routes.quotes_routes import quotes_router
from src.tasks.scrape_quotes_task import scrape_quotes_task

scheduler = BackgroundScheduler()

@asynccontextmanager
async def lifespan(app: FastAPI):
    scrape_quotes_task()
    # scheduler.add_job(scrape_quotes, 'interval', seconds=1 * 60 * 60 * 6)
    scheduler.start()
    yield
    scheduler.shutdown()

app = FastAPI(lifespan=lifespan)

app.include_router(home_router)
app.include_router(quotes_router, prefix="/api")