from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import Base, engine
from app.apis.auth import router as auth_router
from app.apis.student import router as student_router
from app.apis.teacher import router as teacher_router
from app.scripts.seed_db import seed_users
from app.scripts.seed_lesson import seed_lessons
from app.scripts.seed_attendance import seed_attendance

# Работа в режиме заполнения БД тестовыми данными
isSeedDb = False

# Если передан флаг isSeedDb, заполняем базу данными
if isSeedDb:
    print("Заполнение базы данных тестовыми данными...")
    from sqlalchemy.orm import Session
    from app.db.session import SessionLocal

    # Создаем сессию для работы с базой данных
    db = SessionLocal()

    # Заполняем базу тестовыми данными
    # seed_users(db)
    # seed_lessons(db)
    # seed_attendance(db)

    print("База данных успешно заполнена тестовыми данными.")
else:
    # создаём все таблицы
    Base.metadata.create_all(bind=engine)

    # Инициализация приложения
    app = FastAPI(title="Attendance MVP")

    # Разрешаем CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # здесь подключим роутеры:
    app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
    app.include_router(student_router, prefix="/api/student", tags=["students"])
    app.include_router(teacher_router, prefix="/api/teacher", tags=["teachers"])

    # Отдаём статические файлы из папки frontend
    app.mount("/", StaticFiles(directory="frontend", html=True), name="static")

    # Главная страница, которая будет отдавать frontend/index.html
    @app.get("/", response_class=HTMLResponse)
    async def main():
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()