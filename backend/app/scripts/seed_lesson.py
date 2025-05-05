from app.db.session import SessionLocal
from app.db.models.lesson import Lesson
from app.db.models.course import Course
from app.db.models.classroom import Classroom
from app.db.models.user import User
from datetime import time
from sqlalchemy.orm import Session

def seed_lessons(db: Session):
    # Пример курса и аудитории
    course = Course(course_name="Математика")
    classroom = Classroom(room_number="102", ble_identifier="BLE102")
    db.add(course)
    db.add(classroom)
    db.commit()

    # Преподаватель
    teacher = db.query(User).filter(User.login == "teacher").first()

    # Пример урока
    lesson = Lesson(
        course_id=course.course_id,
        group_id=1,  # предполагаем, что группа с ID 1 существует
        teacher_id=teacher.user_id,
        classroom_id=classroom.classroom_id,
        day_of_week="Monday",
        start_time=time(9, 0),
        end_time=time(10, 30)
    )
    db.add(lesson)
    db.commit()

def main():
    db = SessionLocal()
    seed_lessons(db)

if __name__ == "__main__":
    main()