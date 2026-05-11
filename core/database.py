from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import settings

Database_url = settings.DATABASE_URL 

engine = create_engine(
    Database_url,
    connect_args={"check_same_thread":False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()