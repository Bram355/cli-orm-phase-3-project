from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Bot(Base):
    __tablename__ = 'bots'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    sessions = relationship("Session", back_populates="bot")

    def __repr__(self):
        return f"<Bot(id={self.id}, name='{self.name}')>"
