from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.session import Base

class Classroom(Base):
    __tablename__ = "classrooms"
    classroom_id = Column(Integer, primary_key=True, index=True)
    room_number = Column(String, unique=True, nullable=False)
    ble_identifier = Column(String, unique=True, nullable=False)

    lessons = relationship("Lesson", back_populates="classroom")
