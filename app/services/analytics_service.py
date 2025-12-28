from app.database import SessionLocal
from app.models import AccessLog

def log_access(token, user_id):
    db = SessionLocal()
    db.add(AccessLog(token=token, user_id=user_id))
    db.commit()
    db.close()
