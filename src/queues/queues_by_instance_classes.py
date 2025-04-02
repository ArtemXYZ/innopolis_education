"""
    Модуль содержит реализации различных типов очередей для списка экземпляров классов.
"""

from collections import deque

# from midl_attestation.logistics_company import Delivery
from src.services.tools import ServiceTols


# ----------------------------------------------------------------------------------------------------------------------
class _QueueByInstanceClasses(ServiceTols):
    """
        Класс содержит реализацию очереди для списка экземпляров классов.
        Поддерживает операции добавления (enqueue) и удаления (dequeue) элементов.

        Принцип работы: FIFO (First In, First Out) – "Первым пришёл, первым ушёл".
    """





    def __init__(self):
        super().__init__()
        self.queue_obj: deque | None = None

    def set_queue_array(self, _array: list):
        """
            Инициализация очереди.
            :param _array: Список экземпляров класса.
            :return:
        """

        if self.queue_obj:
            raise ValueError(f'Ошибка инициализации очереди, очередь не пустая: {self.queue_obj:}')
        else:
            self.validator(_array, list)
            self.queue_obj = deque(_array)
        return self

    def add_in_queue(self, item: object) -> None:
        """
            Добавляет элемент в конец очереди.
            :param item: Экземпляр класса для добавления в очередь.
        """

        self.validator(item, object)
        self.queue_obj.append(item)

    def del_in_queue(self) -> object:
        """
            Удаляет и возвращает элемент из начала очереди.

            :return: Удаленный элемент.
            :raises IndexError: Если очередь пуста.
        """
        if not self.is_empty_array(self.queue_obj):
            return self.queue_obj.popleft()
        raise IndexError('Список пуст! Невозможно извлечь задачу.')


    def size_queue(self) -> int:
        """
            Возвращает количество элементов в очереди.
            :return: Количество элементов в очереди.
        """

        self.validator(self.queue_obj, object)

        return self.siz_array(self.queue_obj)

    def __str__(self):

        return (
            f'{list(self.queue_obj)}'
        )


    def __repr__(self) -> str:

        return (
            f'{self.__class__.__name__}. '
            f'Очередь "FIFO": {list(self.queue_obj)}'
        )


class QueueByInstanceClasses(ServiceTols):
    """
        Класс содержит реализацию очереди для списка экземпляров классов.
        Поддерживает операции добавления (enqueue) и удаления (dequeue) элементов.
        Реализован как Singleton - будет существовать только один экземпляр этого класса.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Инициализация очереди при первом создании экземпляра
            cls._instance.queue_obj = None
        return cls._instance

    def __init__(self):
        # Проверяем, чтобы инициализация выполнялась только один раз
        if not hasattr(self, '_initialized'):
            super().__init__()
            self._initialized = True

    def set_queue_array(self, _array: list):
        """
            Инициализация очереди.
            :param _array: Список экземпляров класса.
            :return:
        """
        if self.queue_obj:
            raise ValueError(f'Ошибка инициализации очереди, очередь не пустая: {self.queue_obj:}')
        else:
            self.validator(_array, list)
            self.queue_obj = deque(_array)
        return self

    def add_in_queue(self, item: object) -> None:
        """
            Добавляет элемент в конец очереди.
            :param item: Экземпляр класса для добавления в очередь.
        """
        self.validator(item, object)
        self.queue_obj.append(item)

    def del_in_queue(self) -> object:
        """
            Удаляет и возвращает элемент из начала очереди.
            :return: Удаленный элемент.
            :raises IndexError: Если очередь пуста.
        """
        if not self.is_empty_array(self.queue_obj):
            return self.queue_obj.popleft()
        raise IndexError('Список пуст! Невозможно извлечь задачу.')

    def size_queue(self) -> int:
        """
            Возвращает количество элементов в очереди.
            :return: Количество элементов в очереди.
        """
        self.validator(self.queue_obj, object)
        return self.siz_array(self.queue_obj)

    def __str__(self):
        return f'{list(self.queue_obj)}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}. Очередь "FIFO": {list(self.queue_obj)}'

