from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Course(Base):
    __tablename__ = "courses"
    course_id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String, nullable=False)
    external_id = Column(String, unique=True, nullable=True)
