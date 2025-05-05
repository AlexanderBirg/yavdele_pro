from sqlalchemy.orm import Session
from app.db.models.user import User
from app.db.models.group import Group
from app.core.security import get_password_hash
from app.db.session import SessionLocal

def seed_users(db: Session):
    # Пример группы для студентов
    group = Group(group_name="Группа 1")
    db.add(group)
    db.commit()

    # # Создание преподавателя
    # teacher = User(
    #     login="teacher",
    #     password_hash=get_password_hash("teacher"),
    #     name="Преподаватель 1",
    #     role="teacher",
    #     group_id=None,
    #     external_id=None
    # )
    # db.add(teacher)

    # Создание студента
    for i in range(22, 23):
        student = User(
            login=f"student{i}",
            password_hash=get_password_hash(f"student{i}"),
            name=f"Студент {i}",
            role="student",
            group_id=group.group_id,
            external_id=None
        )
        db.add(student)

    db.commit()

def main():
    db = SessionLocal()
    seed_users(db)

if __name__ == "__main__":
    main()