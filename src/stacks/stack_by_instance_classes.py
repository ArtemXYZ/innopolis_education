"""
    Модуль содержит реализации различных типов стека для списка экземпляров классов.
"""

import heapq

# from midel_attestation.logistics_company import Delivery
from src.services.tools import ServiceTols


# ----------------------------------------------------------------------------------------------------------------------
class StackByInstanceClasses(ServiceTols):
    """
        Класс содержит реализацию стека (адаптацию стандартного модуля heapq ("кучи") для работы
        с приоритетными очередями, LIFO) для списка экземпляров классов.

        Принцип работы: LIFO (Last In, First Out) – "Последним пришёл, первым ушёл".
    """

    def __init__(self):
        super().__init__()
        self.stack_obj: list[object] = []

    def set_stack_array(self, _array: list):
        """
            Инициализация стека.
            :param _array: Список экземпляров класса.
            :return:
        """

        if self.stack_obj:
            raise ValueError(f'Ошибка инициализации очереди, очередь не пустая: {self.stack_obj:}')
        else:
            self.validator(_array, list | list[object])
            self.stack_obj = _array
            heapq.heappop(self.stack_obj)
        return self

    def add_in_stack(self, item: object) -> None:
        """
            Добавляет элемент в кучу.
            :param item: Экземпляр класса для добавления в очередь.
        """

        self.validator(item, Delivery)
        heapq.heappush(self.stack_obj, item)  #
    def del_in_stack(self) -> object:
        """
            Удаляет и возвращает элемент из вершины стека.

            :return: Удаленный элемент.
            :raises IndexError: Если очередь пуста.
        """
        if not self.is_empty_array(self.stack_obj):
            return heapq.heappop(self.stack_obj)
        raise IndexError('Список пуст! Невозможно извлечь задачу.')

    def size_queue(self) -> int:
        """
            Возвращает количество элементов в очереди.
            :return: Количество элементов в очереди.
        """

        self.validator(self.stack_obj, object)

        return self.siz_array(self.stack_obj)

    def __str__(self):

        return (
            f'{list(self.stack_obj)}'
        )


    def __repr__(self) -> str:

        return (
            f'{self.__class__.__name__}. '
            f'Стек: {list(self.stack_obj)}'
        )
