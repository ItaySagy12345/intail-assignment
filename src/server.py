from fastapi import FastAPI
from src.routes.home_route import home_router
from src.routes.quotes_routes import quotes_router


app = FastAPI()

app.include_router(home_router)
app.include_router(quotes_router, prefix="/api")