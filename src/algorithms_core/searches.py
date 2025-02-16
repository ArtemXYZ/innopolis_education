"""
    Модуль содержит алгоритмы поиска по list[tuple].
"""

from src.services.tools import ServiceTols
from src.algorithms_core.sorts import SortByInstanceClasses


# ----------------------------------------------------------------------------------------------------------------------
class SearchByListTuple:
    """
        Класс содержит алгоритмы поиска по list[tuple].
    """

    def __init__(self):
        pass

    @staticmethod
    def _linear(
            tuple_list: list[tuple],
            search_element: int | str,
            key_tuple: int
    ) -> int | None:
        """
            *** Алгоритм линейного поиска индекса заданного элемента. ***

            :param tuple_list: Входной массив кортежей (присутствуют None).
            :param search_element: Значение, которое требуется найти.
            :param key_tuple: Индекс ключа в кортеже для поиска.
            :return: Возвращает индекс искомого элемента или None, если элемент отсутствует.
            :rtype: None | int.
        """

        # Валидация входных данных:
        if not tuple_list:
            raise ValueError(f'Ошибка, переданный массив пуст, операция не может быть выполнена! {tuple_list}.')

        # Поиск элемента в массиве:
        for index, _tuple in enumerate(tuple_list):

            try:
                if _tuple[key_tuple] == search_element:
                    return index
            except IndexError:
                # Если индекс key_tuple отсутствует в кортеже, пропускаем этот кортеж.
                # Сработает при наличии хотя бы одного в массиве.
                raise IndexError(
                    f'В итерируемом массиве list[tuple]: {tuple_list}, элемент tuple: {_tuple} '
                    f'с индексом {index} вызывает ошибку при обращении по индексу {key_tuple} к искомому элементу '
                    f' в кортеже (не содержит заданный для поиска индекс в кортеже) операция не может быть выполнена!'
                )

        # Если элемент не найден после прохода по всему списку
        print(f'Заданный элемент "{search_element}" для поиска не найден в массиве! {tuple_list}.')
        return None

    @staticmethod
    def _binary(
            tuple_list: list[tuple],
            search_element: int | str,
            key_tuple: int
    ) -> int | None:
        """
            *** Алгоритм бинарного поиска индекса заданного элемента в отсортированном массиве с пропусками. ***

            :param tuple_list: Входной массив кортежей (присутствуют None).
            :param search_element: Значение, которое требуется проверить.
            :param key_tuple: Индекс ключа в кортеже для сравнения.
            :return: Возвращает индекс искомого элемента или None, если элемент отсутствует.
            :rtype: None | int.
        """

        # Валидация входных данных:
        if not tuple_list:
            raise ValueError(f'Ошибка, переданный массив пуст, операция не может быть выполнена! {tuple_list}.')

        # Определение границ:
        left, right = 0, len(tuple_list) - 1

        # Перебор массива:
        while left <= right:
            # Индекс среднего элемента последовательности (округляет в сторону меньшего числа):
            midl_index: int = (left + right) // 2

            # Обработка пропусков:
            # Если элемент в середине равен None, ищем ближайший ненулевой элемент:
            if tuple_list[midl_index] is None:
                low, high = midl_index - 1, midl_index + 1
                while True:
                    if low >= left and tuple_list[low] is not None:
                        midl_index = low
                        break
                    if high <= right and tuple_list[high] is not None:
                        midl_index = high
                        break
                    low -= 1
                    high += 1
                    if low < left and high > right:
                        return -1  # Все элементы в пределах left и right равны None

            # Основной алгоритм:
            # Проверка среднего элемента (Если сразу же совпало, возвращаем результат):
            if tuple_list[midl_index][key_tuple] == search_element:
                return midl_index

            # Если искомый элемент больше среднего, игнорируем левую половину:
            elif tuple_list[midl_index][key_tuple] < search_element:
                # Сдвигаем левую границу (проверили середину, теперь следующее число от средины будет начальной границей).
                left = midl_index + 1

            # Если искомый элемент меньше среднего, игнорируем правую половину:
            else:
                # Сдвигаем правую границу (проверили середину, теперь предыдущее число от средины будет конечной границей).
                right = midl_index - 1

        # Элемент не найден:
        # print(f'Ошибка, переданный элемент не найден!: {search_element}.')
        return None

    def __str__(self):
        return f'{self.__class__.__name__}'

    def __repr__(self):
        return f'{self.__class__.__name__}'


class SearchByInstanceClasses:
    """
        Класс содержит алгоритмы поиска по списку экземпляров классов.
    """

    def __init__(self):

        self.service_tools = ServiceTols
        self.sorts = SortByInstanceClasses()

    def _linear(
            self,
            array: list[object],
            search_element: int | str,
            attribute_name: str
    ) -> int | None:
        """
            *** Алгоритм линейного поиска индекса заданного элемента. ***

            :param array: Входной список экземпляров классов.
            :param search_element: Значение, которое требуется найти.
            :param attribute_name: Имя атрибута для по которому осуществляется поиск по списку экземпляров классов.
            :return: Возвращает индекс искомого элемента или None, если элемент отсутствует.
            :rtype: None | int.
        """

        # Валидация входных данных:
        if not array:
            raise ValueError(f'Ошибка, переданный массив пуст, операция не может быть выполнена! {array}.')

        # Поиск элемента в массиве:
        for index, element_array in enumerate(array):

            # Валидация:
            self.service_tools._validator(element_array, object)

            attribute_value = getattr(element_array, attribute_name)

            if attribute_value == search_element:
                return index

        # Если элемент не найден после прохода по всему списку
        print(f'Заданный элемент "{search_element}" для поиска не найден в массиве: {array}!')

        return None

    def _binary(
            self,
            array: list[object],
            search_element: int | str,
            attribute_name: str
    ) -> int | None:
        """
            *** Алгоритм бинарного поиска индекса заданного элемента в отсортированном массиве с пропусками. ***

            :param array: Входной список экземпляров классов.
            :param search_element: Значение, которое требуется найти.
            :param attribute_name: Имя атрибута, по которому осуществляется поиск по списку экземпляров классов.
            :return: Возвращает индекс искомого элемента или None, если элемент отсутствует.
            :rtype: None | int.
        """

        # Валидация входных данных:
        if not array:
            raise ValueError(f'Ошибка, переданный массив пуст, операция не может быть выполнена! {array}.')

        # Определение границ:
        left, right = 0, len(array) - 1

        # Перебор массива:
        while left <= right:
            # Индекс среднего элемента последовательности (округляет в сторону меньшего числа):
            midl_index: int = (left + right) // 2

            # Обработка пропусков:
            # Если элемент в середине равен None, ищем ближайший ненулевой элемент:
            if array[midl_index] is None:
                low, high = midl_index - 1, midl_index + 1
                while True:
                    if low >= left and array[low] is not None:
                        midl_index = low
                        break
                    if high <= right and array[high] is not None:
                        midl_index = high
                        break
                    low -= 1
                    high += 1
                    if low < left and high > right:
                        return None  # Все элементы в пределах left и right равны None

            # Получаем значение атрибута для сравнения:
            midl_element = array[midl_index]

            # Валидация:
            self.service_tools._validator(midl_element, object)

            attribute_value = getattr(midl_element, attribute_name)

            # Основной алгоритм:
            # Проверка среднего элемента (Если сразу же совпало, возвращаем результат):
            if attribute_value == search_element:
                return midl_index

            # Если искомый элемент больше среднего, игнорируем левую половину:
            elif attribute_value < search_element:
                # Сдвигаем левую границу (проверили середину, теперь следующее число от средины будет начальной границей).
                left = midl_index + 1

            # Если искомый элемент меньше среднего, игнорируем правую половину:
            else:
                # Сдвигаем правую границу (проверили середину, теперь предыдущее число от средины будет конечной границей).
                right = midl_index - 1

        # Элемент не найден:
        print(f'Заданный элемент "{search_element}" для поиска не найден в массиве: {array}!')
        return None

    def _searcher(self, array: list[object], _search_element, _attribute_name, mode='linear') -> int | None:
        """
            Универсальный поисковик. Содержит два метода поиска: линейный и бинарный.
            Необходимо установить флаг "mode" либо 'linear', либо 'binary'. По умолчанию linear'.

            :param array: Входной список экземпляров классов.
            :param _search_element:
            :param _attribute_name:
            :param mode: Флаг "mode" либо 'linear', либо 'binary'. По умолчанию linear'.

            :return:
        """

        if not _search_element and _attribute_name:
            raise TypeError(
                f'Ошибка, метод ожидает передачи обязательных параметров: "search_element": {_search_element}, '
                f'"attribute_name": {_attribute_name}.'
            )

        if mode == 'linear':
            index_elem = self._linear(
                array, search_element=_search_element, attribute_name=_attribute_name
            )


        elif mode == 'binary':

            # Для бинарного необходимо сначала выполнить сортировку:
            sorted_list = self.sorts._quick_sort(array, _attribute_name)

            index_elem = self._binary(
                sorted_list, search_element=_search_element, attribute_name=_attribute_name
            )

        else:

            raise ValueError(f'Ошибка, недопустимое значение для аргумента "mode": {mode}.')

        return index_elem

    def __str__(self):
        return f'{self.__class__.__name__}'

    def __repr__(self):
        return f'{self.__class__.__name__}'
