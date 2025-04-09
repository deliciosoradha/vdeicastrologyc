from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    birth_date = Column(DateTime)
    birth_time = Column(String)
    birth_place = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    created_at = Column(DateTime, server_default='now()')
    
    reports = relationship("Report", back_populates="user")

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"
