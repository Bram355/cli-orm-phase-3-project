from models.bot import Bot
from models.session import Session
from database import SessionLocal

def create_bot(name):
    db = SessionLocal()
    bot = Bot(name=name)
    db.add(bot)
    db.commit()
    db.refresh(bot)
    db.close()
    return bot

def list_bots():
    db = SessionLocal()
    bots = db.query(Bot).all()
    db.close()
    return bots

def delete_bot(name):
    db = SessionLocal()
    bot = db.query(Bot).filter(Bot.name == name).first()
    if bot:
        db.delete(bot)
        db.commit()
    db.close()

def add_session_to_bot(bot_id, description):
    db = SessionLocal()
    session = Session(description=description, bot_id=bot_id)
    db.add(session)
    db.commit()
    db.refresh(session)
    db.close()
    return session
