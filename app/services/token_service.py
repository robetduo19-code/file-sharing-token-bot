import uuid
from datetime import datetime, timedelta
from app.database import SessionLocal
from app.models import Token
from app.utils import is_expired

def create_token(file_id, seconds):
    db = SessionLocal()
    token = str(uuid.uuid4())
    db.add(Token(
        token=token,
        file_id=file_id,
        expires_at=datetime.utcnow() + timedelta(seconds=seconds)
    ))
    db.commit()
    db.close()
    return token

def validate_token(token_str):
    db = SessionLocal()
    t = db.query(Token).filter_by(token=token_str, used=False).first()
    if not t or is_expired(t.expires_at):
        db.close()
        return None
    t.used = True
    db.commit()
    fid = t.file_id
    db.close()
    return fid
