from sqlalchemy import Column, Integer, ForeignKey, Time, String
from sqlalchemy.orm import relationship
from app.db.session import Base

class Lesson(Base):
    __tablename__ = "lessons"
    lesson_id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.course_id"), nullable=False)
    group_id = Column(Integer, ForeignKey("groups.group_id"), nullable=False)
    teacher_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    classroom_id = Column(Integer, ForeignKey("classrooms.classroom_id"), nullable=False)
    day_of_week = Column(String, nullable=False)      # например, "Monday"
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)

    course = relationship("Course")
    group = relationship("Group", back_populates="lessons")
    teacher = relationship("User")
    classroom = relationship("Classroom", back_populates="lessons")
