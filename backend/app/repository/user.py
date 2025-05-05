from sqlalchemy.orm import Session
from app.db.models.user import User
from app.core.security import verify_password

def authenticate_user(db: Session, login: str, password: str) -> User | None:
  user = db.query(User).filter(User.login == login).first()

  if not user:
    return None
  if not verify_password(password, user.password_hash):
    return None

  return user

def get_user(db: Session, user_id: int) -> User | None:
  return db.query(User).filter(User.user_id == user_id).first()