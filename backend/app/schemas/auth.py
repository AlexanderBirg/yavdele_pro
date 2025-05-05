from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
  access_token: str
  token_type: str

class TokenData(BaseModel):
  user_id: Optional[int] = None
  role: Optional[str] = None  # Добавляем роль в TokenData

class UserLogin(BaseModel):
  login: str
  password: str