import jwt
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from config import SECRET_KEY, ALGORITHM
from ..models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.InvalidTokenError:
        return None

def authenticate_user(username: str, password: str):
    user = User.objects(username=username).first()
    if user and user.verify_password(password):
        return user
    return None

def create_access_token(user_id: str, role: str):
    payload = {"user_id": user_id, "role": role}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token
