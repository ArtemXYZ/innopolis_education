"""
    Модуль содержит алгоритмам бинарного поиска, O(log n).
"""

import pytest
from typing import TypeVar

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


def get_index_element_array(array_list: list, serch_element: int) -> int:
    """
        *** Алгоритм бинарного поиска индекса заданного элемента в отсортированном массиве с пропусками. ***

        :param array_list: Входной массив, (присутствуют None).
        :param serch_element: Значение, которое требуется проверить.
        :return: Возвращает искомый элемент или значение "-1", если элемент отсутствует.
        :rtype: int.
!
    """

    # Валидация входных данных:
    valid_array_list = _validator(array_list, list)
    valid_element = _validator(serch_element, int)

    # Если не пустой массив:
    if not valid_array_list:
        raise ValueError(f'Ошибка, переданный массив пуст, операция не может быть выполнена! {valid_array_list}.')

    # ---------------------------------- Определение границ:
    left, right = 0, len(valid_array_list) - 1

    # ---------------------------------- Перебор массива:
    while left <= right:
        # Индекс среднего элемента последовательности (округляет в сторону меньшего числа):
        midl_index: int = (left + right) // 2

        # -------------------------------- Обработка пропусков:
        # Если элемент в середине равен None, ищем ближайший ненулевой элемент:
        if valid_array_list[midl_index] is None:
            low, high = midl_index - 1, midl_index + 1
            while True:
                if low >= left and valid_array_list[low] is not None:
                    midl_index = low
                    break
                if high <= right and valid_array_list[high] is not None:
                    midl_index = high
                    break
                low -= 1
                high += 1
                if low < left and high > right:
                    return -1  # Все элементы в пределах left и right равны None

        # --------------------------------- Основной алгоритм:
        # Проверка среднего элемента (Если сразу же совпало, возвращаем результат):
        if valid_array_list[midl_index] == valid_element:
            return midl_index

        # Если искомый элемент больше среднего, игнорируем левую половину:
        elif valid_array_list[midl_index] < valid_element:
            # Сдвигаем левую границу (проверили середину, теперь следующее число от средины будет начальной границей).
            left = midl_index + 1

        # Если искомый элемент меньше среднего, игнорируем правую половину:
        else:
            # Сдвигаем правую границу (проверили середину, теперь предыдущее число от средины будет конечной границей).
            right = midl_index - 1

    # ---------------------------------------- Элемент не найден:
    print(f'Ошибка, переданный елемент не найден!: {valid_element}.')
    return -1


# ----------------------------------------------------------------------------------------------------------------------
# Исходные данные: 9 индекс последн.
array: list = [1, 2, None, None, 5, 6, 7, None, 10, 11]

# Вызов функции:
index_element = get_index_element_array(array, 7)
print(index_element)

# ------------------------------------------------ Тесты:
@pytest.mark.parametrize(
    # Передаваемые значения аргументов.
    # expected_result — ожидаемый результат (индекс найденного элемента).
    # expected_exception — ожидаемое исключение (если элемент не найден).
    # match — сообщение исключения (проверяется при его возникновении).
    "array_list, serch_value, expected_result, expected_exception, match",
    [
        (array, 1, 0, None, None),
        (array, 2, 1, None, None),
        (array, 3, -1, None, None),
        (array, 4, -1, None, None),
        (array, 5, 4, None, None),
        (array, 6, 5, None, None),
        (array, 7, 6, None, None),
        (array, 8, -1, None, None),
        (array, 9, -1, None, None),
        (array, 10, 8, None, None),
        ([], 11, 9, ValueError, 'Ошибка, переданный массив пуст, операция не может быть выполнена!'),
        ((4,), 11, 9, TypeError, 'Недопустимый тип данных:'),
        (array, 13, -1, None, None),
    ]
)
def test_get_index_element_array(array_list, serch_value, expected_result, expected_exception, match):
        if expected_exception:
            with pytest.raises(expected_exception=expected_exception, match=match):
                get_index_element_array(array_list=array_list, serch_element=serch_value)
        else:
            assert get_index_element_array(array_list=array_list, serch_element=serch_value) == expected_result






#     # 1
#     assert get_avg_in_array(array) == 4.0
#     # 2
#     with pytest.raises(ValueError, match='Ошибка, переданный массив пуст, операция не может быть выполнена!:'):
#         get_avg_in_array([])
#     # 3
#     with pytest.raises(TypeError, match='Недопустимый тип данных для аргумента:'):
#         get_avg_in_array({})
