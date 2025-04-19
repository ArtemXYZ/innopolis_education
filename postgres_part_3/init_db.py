"""
Модуль создания и удаления бд
"""
# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------- Импорт стандартных библиотек Пайтона
# ---------------------------------- Импорт сторонних библиотек


# -------------------------------- Локальные модули
from postgres_part_3.configs import ENGINE
from postgres_part_3.mockup_db import Base


# ----------------------------------------------------------------------------------------------------------------------
class InitDB:
    """
        Создание таблиц и базы данных перед началом работы.
    """

    def __init__(self):
        self.base = Base
        self.engine = ENGINE

    def create_db(self):
        """
            Функция создания базы данных и всех таблиц если они еще не созданы.
        """

        # with self.engine.begin() as conn:
        #     conn.run_sync(self.base.metadata.create_all)

        self.base.metadata.create_all(self.engine)

    def drop_db(self):  # engine_obj:AsyncEngine
        """
            Функция сброса (удаления) базы данных и всех таблиц.
        """

        # with self.engine.begin() as conn:
        #     conn.run_sync(self.base.metadata.drop_all)

        self.base.metadata.drop_all(self.engine)
