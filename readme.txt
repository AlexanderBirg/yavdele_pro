----------------------
----------------------

--- ЗАПУСК СЕРВЕРА ---

----------------------
----------------------

# Разреши локальное выполнение скриптов (только на время этой сессии):
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

---------------------

# в папке проекта создаем при первом запуске
python -m venv .venv

# Активация виртуалки
# Для PowerShell:
.\.venv\Scripts\Activate.ps1
# Для CMD:
.\.venv\Scripts\activate.bat
# macOS/Linux:
source .venv/bin/activate

# Будет префикс (.venv) в командной строке

---------------------

# при первом запуске устанавливаем зависимости
pip install -r requirements.txt

---------------------

# Далее установить postgres и создать бд attendance, чтобы была структура "Servers > PostgreSQL 17 > attendance"
# postgresql://postgres:admin@localhost:5432/attendance - в поиске по проекту найти эту строку и заменить "admin" под свой пароль

---------------------

# запуск проекта для теста на машине
uvicorn app.main:app --reload --app-dir backend

# При первом запуске - заменить в main.py переменную isSeedDb на True и поочередно вызвать seed_users seed_lessons seed_attendance функции, чтобы заполнить БД тестовыми данными
# После всех манипуляций - заменить в main.py переменную isSeedDb на False и получить рабочий сервер

# В идеале сделать более умное решение, но времени нема, поэтому захардкодил овнокод

---------------------

# Для тестов по локальной сети вместе, чтобы сервак был доступен для apk приложений
uvicorn app.main:app --reload --app-dir backend --host 0.0.0.0 --port 8000

# IP определяем по команде
ipconfig
# поле ipv4 - отсюда берем IP и вставляем его в поле URL в apk файле

---------------------
---------------------

--- ЛОГИКА РАБОТЫ ---

---------------------
---------------------

Запустили сервер

---------------------

Принцип отметки прост:

Открыли приложение на смартфоне
Ввели локальный ip адрес сервера в поле URL в приложении (н-р, IP = 192.168.1.101 => http://192.168.1.101:8000)
Ввели логин и пароль студента, допустим student2 student2

Если все ок, перенаправимся на второй экран
чекаем вкл ли блютуз по нажатию на кнопку, если да, то после нажатия на кнопку отправится на сервер сообщение об отметке (через 2 сек) - это имитация механизма отметки по BLE метке

Если блютуз включен, а приложуха все равно шлет подальше => выключаем блютуз, жмем кнопку, снова включаем блютуз и жмакаем кнопку - должно сработать

Для проверки, что с телефона сервак доступен - просто открыть страницу сервера, должно появиться окно для авторизации препода => сервак доступен, баг в чем-то другом :)

---------------------

Принцип проверки посещаемости прост:

На ПК перешли по ссылке локального сервера (н-р, http://192.168.1.101:8000)
Получили страницу авторизации
ввели логин и пароль препода (teacher teacher)
перенаправились на страницу http://127.0.0.1:8000/index.html, где увидим список отмеченных на паре студентов (каждые N секунд или по перезагрузке страницы происходит обновление списка)

---------------------

По приколу можно авторизовать студня через страницу авторизации препода:

авторизовываемся как студент (логин и пароль студня)
нас закидывает на страницу index.html
вручнуюю переходим на страницу student.html
нажимаем на кнопку - отметиться!

У препода в списке отобразится отметка нового студня

---------------------
