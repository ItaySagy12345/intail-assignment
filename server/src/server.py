from fastapi import FastAPI
from src.routes.home_route import home_router


app = FastAPI()

app.include_router(home_router)