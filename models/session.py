from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Session(Base):
    __tablename__ = 'sessions'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    bot_id = Column(Integer, ForeignKey("bots.id"))

    bot = relationship("Bot", back_populates="sessions")

    def __repr__(self):
        return f"<Session(id={self.id}, desc='{self.description}', bot_id={self.bot_id})>"
