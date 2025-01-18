from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase
import datetime

class Base(DeclarativeBase):
    pass

class Guide(Base):
    __tablename__ = 'guides'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    nationality = Column(String, nullable=False)
    location = Column(String, nullable=False)
    whatsapp = Column(String, nullable=False)
    telegram = Column(String, nullable=False)
    languages = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    places = Column(String, nullable=False)
    vehicle = Column(String, nullable=False)
    vehicle_capacity = Column(Integer, nullable=False)
    # vehicle_photo = Column(String, nullable=False)
    vehicle_type = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)