from sqlalchemy.orm import Session
from app.db.models.attendance import Attendance
from datetime import datetime

def get_student_attendance(db: Session, student_id: int):
    return db.query(Attendance).filter(Attendance.student_id == student_id).all()

def mark_attendance_for_student(db: Session, student_id: int, lesson_id: int):
    today = datetime.utcnow().date()
    # Проверяем, есть ли уже запись за сегодня
    existing = db.query(Attendance).filter(
        Attendance.student_id == student_id,
        Attendance.lesson_id == lesson_id,
        Attendance.date == today
    ).first()

    if not existing:
        new = Attendance(
            student_id=student_id,
            lesson_id=lesson_id,
            date=today,
            timestamp=datetime.utcnow()
        )
        db.add(new)
        db.commit()