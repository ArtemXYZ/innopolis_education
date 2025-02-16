"""
    Модуль содержит реализации различных типов очередей для списка экземпляров классов.
"""

from collections import deque
import heapq

from src.services.tools import ServiceTols


# ----------------------------------------------------------------------------------------------------------------------
class QueueByInstanceClasses(ServiceTols):
    """
        Класс содержит реализацию очереди для списка экземпляров классов.
        Поддерживает операции добавления (enqueue) и удаления (dequeue) элементов.
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
            self._validator(_array, list)
            self.queue_obj = deque(_array)
        return self

    def add_queue(self, item: object) -> None:
        """
            Добавляет элемент в конец очереди.
            :param item: Экземпляр класса для добавления в очередь.
        """

        self._validator(item, object)
        self.queue_obj.append(item)

    def del_queue(self) -> object:
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

        self._validator(self.queue_obj, object)

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



#
#         # self.array = array
#         # self.queue = deque(self.array if self.array else [])  # Инициализация очереди
#         # self.search_element = search_element
#         # self.attribute_name = attribute_name
#        array: list[object] = None,
#             search_element: int | str = None,
#             attribute_name: str = None