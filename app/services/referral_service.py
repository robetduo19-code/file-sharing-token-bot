from app.database import SessionLocal
from app.models import Referral

def handle_referral(code, new_user_id):
    if not code.startswith("ref_"):
        return
    referrer = int(code.replace("ref_", ""))
    if referrer == new_user_id:
        return
    db = SessionLocal()
    if not db.query(Referral).filter_by(referred_id=new_user_id).first():
        db.add(Referral(referrer_id=referrer, referred_id=new_user_id))
        db.commit()
    db.close()
