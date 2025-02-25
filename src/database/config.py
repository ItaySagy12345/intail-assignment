from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.config import CONFIG


engine = create_engine(f'postgresql+psycopg2://{CONFIG["db"]["postgres_user"]}:{CONFIG["db"]["postgres_password"]}@{CONFIG["db"]["postgres_host"]}:{CONFIG["db"]["postgres_port"]}/{CONFIG["db"]["postgres_db"]}')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)