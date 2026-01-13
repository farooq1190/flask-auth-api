import jwt
import datetime
from config import JWT_SECRET, JWT_ALGORITHM    

def generate_token(username):
    payload = {
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

def verify_token(token):
    return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])    
