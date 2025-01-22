"""
    Модуль содержит алгоритмам бинарного поиска, O(log n).
"""


# import time
# import sys

from typing import TypeVar

# # import matplotlib.pyplot as plt
# import numpy as np
# import pytest


# Устанавливаем максимальное количество цифр для строкового представления целого числа
# sys.set_int_max_str_digits(10000)


any_types = TypeVar('any_types')  # Создаем обобщённый тип данных.
# ----------------------------------------------------------------------------------------------------------------------
def _validator(value: any_types, *check_type: type[any]) -> any_types:
    """
        *** Функция валидации аргументов. ***

        Предназначен для проверки корректной передачи аргументов в соответствии с требуемым типом данных.

        * Описание механики:
            В соответствии с переданным набором допустимых типов данных через параметр "*check_type",
            осуществляется сверка проверяемого аргумента "value" на основе метода "isinstance()".
            В случае соответствия хотя бы одному из набора типов данных, возвращается переданный аргумент "value",
            иначе, вызывается исключение TypeError.

        ***

        * Пример вызова:

            params = _validator(_params, dict)

        ***

        :param value: Значение, которое требуется проверить.
        :param check_type: Один или несколько типов данных, допустимых для значения value.
        :return: Возвращает значение value, если оно соответствует одному из типов check_type.
        :rtype: any_types, возвращается тип исходный тип данных проверяемого аргумента.
        :raises TypeError: Если значение value не соответствует ни одному из указанных типов данных.
    """

    if isinstance(value, check_type):
        return value
    else:
        raise TypeError(f'Недопустимый тип данных: "{type(value).__name__}", для аргумента: "{value}".')

def get_index_element_array(array_list: list, element: int) -> int:
    """
        *** Алгоритм бинарного поиска индекса заданного элемента в отсортированном массиве с пропусками. ***

        :param array_list: Входной массив, (присутствуют None).
        :param element: Значение, которое требуется проверить.
        :return: Возвращает искомый элемент или значение "-1", если элемент отсутствует.
        :rtype: int.
!
    """

    # Валидация входных данных:
    valid_array_list = _validator(array_list, list)
    valid_element = _validator(element, int)

    # Если не пустой массив:
    if not valid_array_list:
        raise ValueError(f'Ошибка, переданный массив пуст, операция не может быть выполнена!: {valid_array_list}.')

    # ---------------------------------- Определение границ:
    left = 0
    right = len(valid_array_list) - 1

    # ---------------------------------- Перебор массива:


    while left <= right:

        # Индекс среднего элемента последовательности:
        midl_index: int = (left + right) // 2

        # Элемент массива по индексу среднего элемента:
        element_by_midl_index = valid_array_list[midl_index]

        # Если средний элемент массива (его части) не None:
        if element_by_midl_index:
            print(f'Значение следующего среднего элемента массива: "{element_by_midl_index}".')




            # Проверка среднего элемента:
            if element_by_midl_index == valid_element:
                print(f'Сравнение среднего элемента "{element_by_midl_index}" с искомым.')
                return midl_index

            # Если искомый элемент (valid_element) больше среднего, игнорируем левую половину:
            elif element_by_midl_index < valid_element:

                left = midl_index + 1
                print(f'Если искомый элемент "{element_by_midl_index}" больше среднего.')


            # Если искомый элемент (valid_element) меньше среднего, игнорируем правую половину
            else:
                right = midl_index - 1
                print(f'Если искомый элемент "{element_by_midl_index}" меньше среднего.')

        else:
            print(f'Пропуск итерации для None {element_by_midl_index}.')
            left = midl_index + 1




    # Элемент не найден
    return -1

def _get_index_element_array(array_list: list, element: int) -> int:
    """
    Находит индекс заданного элемента в отсортированном массиве с пропущенными значениями (None).

    :param array_list: Список, содержащий значения и None.
    :param element: Элемент, который нужно найти.
    :return: Индекс элемента или -1, если элемент отсутствует.
    """
    left = 0
    right = len(array_list) - 1

    while left <= right:
        # Определяем середину
        mid = (left + right) // 2

        # Если середина указывает на None, ищем ближайший ненулевой элемент
        if array_list[mid] is None:
            low = mid - 1
            high = mid + 1

            # Движение влево и вправо до ближайшего ненулевого значения
            while low >= left and array_list[low] is None:
                low -= 1
            while high <= right and array_list[high] is None:
                high += 1

            # Если ни слева, ни справа нет подходящего элемента, выходим
            if low < left and high > right:
                return -1

            # Сравниваем с ближайшими элементами
            if low >= left:
                mid = low
            elif high <= right:
                mid = high

        # Сравнение найденного элемента
        if array_list[mid] == element:
            return mid
        elif array_list[mid] < element:
            left = mid + 1
        else:
            right = mid - 1

    # Если элемент не найден
    return -1






# ----------------------------------------------------------------------------------------------------------------------
# Исходные данные:
array: list =  [1, 2, None, None, 5, 6, 7, None, 10, 11]


# Вызов функции:
index_element = get_index_element_array(array, 6)
print(index_element)





# Тесты:
# def test_get_avg_in_array():
#     # 1
#     assert get_avg_in_array(array) == 4.0
#     # 2
#     with pytest.raises(ValueError, match='Ошибка, переданный массив пуст, операция не может быть выполнена!:'):
#         get_avg_in_array([])
#     # 3
#     with pytest.raises(TypeError, match='Недопустимый тип данных для аргумента:'):
#         get_avg_in_array({})



