from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.repository.teacher import get_attendance_for_lesson
from app.core.security import get_current_user
from app.schemas.auth import TokenData

router = APIRouter(tags=["teachers"])

@router.get("/attendance/today/")
def get_teacher_attendance(lesson_id: int, db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
    """Возвращаем данные о посещаемости для преподавателя"""
    # Проверка, является ли пользователь преподавателем
    if current_user.role != "teacher":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to access this resource",
        )
    attendance_data = get_attendance_for_lesson(db, lesson_id)
    if not attendance_data:
        raise HTTPException(status_code=404, detail="No students found for this lesson")
    return attendance_data