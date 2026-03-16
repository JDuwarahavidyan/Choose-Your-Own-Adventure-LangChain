from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import settings

engine = create_engine(url=settings.DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)  # Check Nortan

Base = declarative_base()

# Each request usually creates its own session and then closes it when the request is finished.
# This is a common pattern in web applications to ensure that database connections are properly
# managed and released back to the connection pool.


def get_db():
    db = SessionLocal()
    try:
        yield db  # yield pause function and continue later
    finally:
        db.close()


def create_tables():
    Base.metadata.create_all(bind=engine)
