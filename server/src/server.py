import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apscheduler.schedulers.background import BackgroundScheduler
from contextlib import asynccontextmanager
from src.routes.home_route import home_router
from src.routes.quotes_routes import quotes_router
from src.routes.authors_routes import authors_router
from src.tasks.scrape_quotes_task import scrape_quotes_task
from src.config.config import CONFIG


scheduler = BackgroundScheduler()

def run_scrape_quotes_task():
    asyncio.run(scrape_quotes_task()) 

@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.add_job(run_scrape_quotes_task, 'interval', seconds=1 * 5)
    # scheduler.add_job(run_scrape_quotes_task, 'interval', seconds=1 * 60 * 60)
    scheduler.start()
    yield
    scheduler.shutdown()

app = FastAPI(lifespan=lifespan)

origins = [
    CONFIG["frontend"]["domain"]
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(home_router)
app.include_router(quotes_router, prefix="/api")
app.include_router(authors_router, prefix="/api")