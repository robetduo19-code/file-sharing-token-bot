from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    joined_at = Column(DateTime, default=datetime.utcnow)

class File(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True)
    tg_file_id = Column(String)

class Token(Base):
    __tablename__ = "tokens"
    token = Column(String, primary_key=True)
    file_id = Column(Integer)
    expires_at = Column(DateTime)
    used = Column(Boolean, default=False)

class Referral(Base):
    __tablename__ = "referrals"
    id = Column(Integer, primary_key=True)
    referrer_id = Column(Integer)
    referred_id = Column(Integer)

class AccessLog(Base):
    __tablename__ = "access_logs"
    id = Column(Integer, primary_key=True)
    token = Column(String)
    user_id = Column(Integer)
    accessed_at = Column(DateTime, default=datetime.utcnow)
