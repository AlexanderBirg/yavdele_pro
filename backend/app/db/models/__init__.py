# Импортируем каждый модуль, чтобы при импорте пакета models
# регистрировались все модели в metadata
from .user import User
from .group import Group
from .course import Course
from .classroom import Classroom
from .lesson import Lesson
from .attendance import Attendance