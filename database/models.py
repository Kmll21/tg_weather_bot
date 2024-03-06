from sqlalchemy import Column, Integer, String

from .database import Base


class Weather(Base):
    __tablename__ = 'Weather'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    user_id = Column(Integer, unique=True, nullable=False)
    city = Column(String)