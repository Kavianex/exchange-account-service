from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import settings


SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format(
    settings.DBUSER,
    settings.DBPASS,
    settings.DBHOST,
    settings.DBPORT,
    settings.DBNAME,
)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
