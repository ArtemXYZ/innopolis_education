"""
    Модуль содержит алгоритмы поиска по list[tuple].
"""




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
