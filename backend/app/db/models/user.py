from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)  # "student" или "teacher"
    group_id = Column(Integer, ForeignKey("groups.group_id"), nullable=True)
    external_id = Column(String, unique=True, nullable=True)

    group = relationship("Group", back_populates="students")
