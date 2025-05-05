Разреши локальное выполнение скриптов (только на время этой сессии):
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

Активировать виртуальное окружение
cd C:\Projects\YaVDele_PRO\attendance-mvp

Для PowerShell:
.\.venv\Scripts\Activate.ps1
Для CMD:
.\.venv\Scripts\activate.bat

После активации виртуалки будет префикс (.venv) в командной строке.

--------------

pip install -r requirements.txt

--------------

uvicorn app.main:app --reload --app-dir backend


По локалке
uvicorn app.main:app --reload --app-dir backend --host 0.0.0.0 --port 8000

--------------



--------------