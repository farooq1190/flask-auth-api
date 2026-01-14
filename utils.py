import jwt
from flask import current_app
from datetime import datetime, timedelta
from config import JWT_SECRET, JWT_ALGORITHM    

def generate_token(username):
    payload = {
        'username': username,
        'exp': datetime.datetime.utcnow() + timedelta(hours=1)
    }

    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm="HS256")

def verify_token(token):
    try:
        payload = jwt.decode(
            token, current_app.config['SECRET_KEY'], 
            algorithms=["HS256"]
            )
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None