Разреши локальное выполнение скриптов (только на время этой сессии):
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# в папке проекта
python -m venv .venv

Для PowerShell:
.\.venv\Scripts\Activate.ps1
Для CMD:
.\.venv\Scripts\activate.bat

# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt

После активации виртуалки будет префикс (.venv) в командной строке.


Далее в postgres создать бд attendance

--------------

uvicorn app.main:app --reload --app-dir backend


По локалке если
uvicorn app.main:app --reload --app-dir backend --host 0.0.0.0 --port 8000

для определения ip
ipconfig
поле ipv4

--------------



--------------