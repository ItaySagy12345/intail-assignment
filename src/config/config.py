import os
from dotenv import load_dotenv


load_dotenv()

CONFIG = {
    "frontend": {
        "domain": os.getenv('CLIENT')
    },
    "authors_api": {
        "domain": os.getenv('AUTHORS_API')
    },
    "db": {
        "postgres_user": os.getenv('POSTGRES_USER'),
        "postgres_password": os.getenv('POSTGRES_PASSWORD'),
        "postgres_host": os.getenv('POSTGRES_HOST'),
        "postgres_port": int(os.getenv('POSTGRES_PORT')),
        "postgres_db": os.getenv('POSTGRES_DB')
    }
}