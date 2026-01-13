import os

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
JWT_SECRET = os.getenv("JWT_SECRET", "jwt-secret")
JWT_ALGORITHM = "HS256"
