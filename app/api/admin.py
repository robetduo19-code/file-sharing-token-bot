from fastapi import APIRouter, Header, HTTPException
from app.config import config
from app.database import SessionLocal
from app.models import User, Token, Referral

router = APIRouter(prefix="/api/admin")

def check(key):
    if key != config.ADMIN_KEY:
        raise HTTPException(403)

@router.get("/stats")
def stats(x_admin_key: str = Header(...)):
    check(x_admin_key)
    db = SessionLocal()
    data = {
        "users": db.query(User).count(),
        "tokens": db.query(Token).count(),
        "referrals": db.query(Referral).count()
    }
    db.close()
    return data
