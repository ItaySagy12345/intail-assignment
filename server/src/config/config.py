import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

CONFIG = {
    "frontend": {
        "domain": os.getenv('CLIENT')
    },
    "authors_api": {
        "domain": os.getenv('AUTHORS_API')
    },
    "db": {
        "postgres_host": os.getenv('POSTGRES_HOST'),
        "postgres_port": int(os.getenv('POSTGRES_PORT', 5432)),
        "postgres_user": os.getenv('POSTGRES_USER'),
        "postgres_password": os.getenv('POSTGRES_PASSWORD'),
        "postgres_db": os.getenv('POSTGRES_DB'),
        "postgres_url": os.getenv('POSTGRES_URL')
    }
}