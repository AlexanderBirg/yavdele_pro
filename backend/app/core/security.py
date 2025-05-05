from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt
from passlib.context import CryptContext
import os
from app.schemas.auth import TokenData
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE_ME_RANDOM_SECRET")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Инициализация Context для хеширования паролей с использованием bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def verify_password(plain_password: str, hashed_password: str) -> bool:
  """Проверка пароля. Сравнивает хешированный пароль с введённым."""
  return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
  """Хеширует пароль перед сохранением."""
  return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
  """Создаёт JWT токен с заданными данными и временем истечения."""
  to_encode = data.copy()
  expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
  to_encode.update({"exp": expire})
    
  # Добавляем роль в токен, например "student" или "teacher"
  to_encode["role"] = data.get("role", "student")  # Если роль не передана, по умолчанию "student"

  return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    """Проверка и декодирование токена"""
    try:
        # Декодируем токен
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Получаем user_id из данных в токене
        return TokenData(**payload)
    except JWTError:
        return None  # В случае ошибки возвращаем None (неверный или просроченный токен)

def get_current_user(token: str = Depends(oauth2_scheme)):
    """Получаем текущего пользователя на основе токена"""
    user_data = verify_token(token)
    if user_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user_data
