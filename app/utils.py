from datetime import datetime

def is_expired(dt):
    return dt and datetime.utcnow() > dt
