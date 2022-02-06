import imp
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

SQLALCHEMY_DATAQBASE_URL= settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATAQBASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)