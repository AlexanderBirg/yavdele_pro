from sqlalchemy import Column, Integer, ForeignKey, Date, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.session import Base
from datetime import datetime

class Attendance(Base):
    __tablename__ = "attendance"
    attendance_id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    lesson_id = Column(Integer, ForeignKey("lessons.lesson_id"), nullable=False)
    date = Column(Date, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint("student_id", "lesson_id", "date", name="uix_student_lesson_date"),
    )

    student = relationship("User")
    lesson = relationship("Lesson")
