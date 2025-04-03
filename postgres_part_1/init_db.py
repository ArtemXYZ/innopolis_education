"""
    Модуль создания и удаления бд
"""

# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------- Импорт стандартных библиотек
# ---------------------------------- Импорт сторонних библиотек
from sqlalchemy import text
from sqlalchemy.orm import Session

# -------------------------------- Локальные модули

# ======================================================================================================================
class InitDB:
    """
        Класс (де)инициализации базы данных.
    """

    def __init__(self, session: Session, sql_create_table: str, sql_drop_table: str):
        self.session = session
        self.sql_create_table = text(sql_create_table)
        self.sql_drop_table = text(sql_drop_table)

    def create_db(self) -> None:  # engine_obj:AsyncEngine
        """
            Функция создания базы данных если она еще не создана.
            В SQLite база данных создается автоматически при первом подключении к несуществующему файлу.
            Если база данных уже существует, запрос проигнорируется.
        """

        self.session.execute(self.sql_create_table)

    def drop_db(self) -> None:
        """
            Функция сброса (удаления) всех таблиц.
        """

        self.session.execute(self.sql_drop_table)
