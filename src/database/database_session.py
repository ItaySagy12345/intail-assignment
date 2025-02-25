from src.database.config import SessionLocal


class DatabaseSession:
    """
    Context manager for the database session
    """
        
    def __init__(self) -> None:
        self.db = SessionLocal()
    
    def __enter__(self):
        return self.db
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.db.rollback()
        else:
            self.db.commit()
        self.db.close()