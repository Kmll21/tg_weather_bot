from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = f"sqlite:///weather.db"

engine = create_engine(DATABASE_URL, echo=True)

session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()