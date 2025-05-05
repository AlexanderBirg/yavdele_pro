from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.repository.student import get_student_attendance
from app.core.security import get_current_user
from app.schemas.auth import TokenData
from app.repository.student import mark_attendance_for_student

router = APIRouter(tags=["students"])

@router.get("/attendance/today/")
def get_today_attendance(student_id: int, db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
    """Возвращаем данные о посещаемости для студента"""
    if current_user.user_id != student_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to access this resource",
        )
    
    attendance_data = get_student_attendance(db, student_id)
    if not attendance_data:
        raise HTTPException(status_code=404, detail="Attendance not found")
    return attendance_data

@router.post("/attendance/check-in")
def check_in(
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user)
):
    # Разрешаем только студентам
    if current_user.role != "student":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Доступ только для студентов"
        )
    # Жёстко фиксируем lesson_id = 1
    LESSON_ID = 1
    # Отмечаем в репозитории
    mark_attendance_for_student(db, current_user.user_id, LESSON_ID)
    return {"msg": "Attendance marked successfully"}