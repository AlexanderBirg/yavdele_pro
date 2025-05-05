from app.db.session import SessionLocal
from app.db.models.attendance import Attendance
from app.db.models.user import User
from app.db.models.lesson import Lesson
from datetime import datetime
from sqlalchemy.orm import Session

def seed_attendance(db: Session):
    student = db.query(User).filter(User.login == "student").first()
    lesson = db.query(Lesson).first()  # Возьмём первый урок

    # Добавим посещаемость
    attendance = Attendance(
        student_id=student.user_id,
        lesson_id=lesson.lesson_id,
        date=datetime.utcnow().date(),
        timestamp=datetime.utcnow()
    )
    db.add(attendance)
    db.commit()

def main():
    db = SessionLocal()
    seed_attendance(db)

if __name__ == "__main__":
    main()