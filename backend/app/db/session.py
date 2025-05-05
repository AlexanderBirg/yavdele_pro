import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:admin@localhost:5432/attendance"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Сначала определяем Base
Base = declarative_base()

# Только после этого импортируем модели,
# чтобы у них было к чему привязываться
from app.db.models.user import User
from app.db.models.group import Group
from app.db.models.course import Course
from app.db.models.classroom import Classroom
from app.db.models.lesson import Lesson
from app.db.models.attendance import Attendance

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
