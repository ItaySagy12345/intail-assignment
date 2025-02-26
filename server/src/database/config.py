from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.config import CONFIG


engine = create_engine(CONFIG["db"]["postgres_url"])

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)