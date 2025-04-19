"""
    Модуль содержит функции асинхронного подключения к базам данных.
    Для асинхронного подключения обязательно использовать конфиг типа: CONFIG_RNAME=postgresql+asyncpg.
    Обязательна установка библиотеки asyncpg.
"""


# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------- Импорт стандартных библиотек

# ---------------------------------- Импорт сторонних библиотек
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

# -------------------------------- Локальные модули
# from configs import CONFIG_LOCAL_DB


# ======================================================================================================================
class Connector:

    def __init__(self, config: dict | URL | str ):  # = CONFIG_LOCAL_DB
        self.config = config
        self.url_db = self.get_url_string
        self.engine = create_engine(self.url_db)  # , echo=True (Для логирования)!
        self.maker_session = sessionmaker(bind=self.engine, class_=Session, expire_on_commit=False)

    @property
    def get_url_string(self) -> URL | None:
        """
            Создаем URL строку:
            :return: URL строка
        """

        # Проверка типа входной конфигурации подключения:
        # Если на вход конфигурация в словаре:
        if isinstance(self.config, dict):
            _url_db = URL.create(**self.config)  # 1. Формируем URL-строку соединения с БД.
            #  Эквивалент: url_conf_locdb = (f'{drivername}://{username}:{password}@{host}:{port}/{database}')

        # Если на вход url_conf_locdb:
        elif isinstance(self.config, str):
            _url_db = self.config
        else:
            raise ValueError("Invalid config type. Expected dict, URL or str")
        return _url_db

    @property
    def get_session(self) -> Session:
        """
            Создаем объект сессии с локальной бд для всех модулей:
            :return: Синхронная сессия
        """

        return self.maker_session()







