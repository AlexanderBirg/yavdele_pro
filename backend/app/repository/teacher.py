from sqlalchemy.orm import Session
from app.db.models.attendance import Attendance

def get_attendance_for_lesson(db: Session, lesson_id: int):
    # Выполним join с таблицей students, чтобы получить ФИО и логин
    attendance_data = db.query(Attendance).filter(Attendance.lesson_id == lesson_id).join(Attendance.student).all()

    # Преобразуем результат в удобный формат
    result = []
    for attendance in attendance_data:
        result.append({
            "login": attendance.student.login,
            "name": attendance.student.name,
            # "present": attendance.present,
            "timestamp": attendance.timestamp
        })

    return result