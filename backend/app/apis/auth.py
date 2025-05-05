from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repository.user import authenticate_user
from app.core.security import create_access_token
from app.schemas.auth import Token

router = APIRouter(tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

@router.post("/login", response_model=Token)
async def login_for_access_token(
  form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
  user = authenticate_user(db, form_data.username, form_data.password)

  if not user:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Incorrect username or password",
      headers={"WWW-Authenticate": "Bearer"},
    )
  access_token = create_access_token({
    "user_id": str(user.user_id),
    "role": user.role
  })
  return {"access_token": access_token, "token_type": "bearer"}