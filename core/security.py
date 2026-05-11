from typing import Annotated
from fastapi import HTTPException, Depends, status
from jose import jwt,JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from core.config import settings


Secret_key = settings.SECRET_KEY 
Algorithm = settings.ALGORITHM 

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/login")


def hash_password(password):
    return pwd_context.hash(password)


def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)


def create_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(hours=5)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,Secret_key, algorithm=Algorithm)


def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token,Secret_key, algorithms=[Algorithm])
        user_id:int = payload.get("user_id")
        user_email:str = payload.get("user_email")
        role: str = payload.get("role")
        if  user_id is None or  user_email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not  validate user")
        return {
            "id" : user_id,
            "email" : user_email,
            "role" : role
        }
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not  validate user")

        
      


 