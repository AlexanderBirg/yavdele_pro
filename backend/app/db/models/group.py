from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.session import Base

class Group(Base):
    __tablename__ = "groups"
    group_id = Column(Integer, primary_key=True, index=True)
    group_name = Column(String, nullable=False)
    external_id = Column(String, unique=True, nullable=True)

    students = relationship("User", back_populates="group")
    lessons = relationship("Lesson", back_populates="group")
