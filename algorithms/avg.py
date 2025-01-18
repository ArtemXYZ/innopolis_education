"""
    Модуль содержит функции для работы с алгоритмами.
"""

import pytest


# ----------------------------------------------------------------------------------------------------------------------
def get_avg_in_array(array_list: list) -> int | float:
    """
        Алгоритм, который вычисляет и возвращает среднее значение элементов в списке чисел.
        :param array_list: Входной массив.
        :return: AVG.
    """

    # Валидация входных данных:
    if isinstance(array_list, list):
        if array_list:
            return sum(array_list) / len(array_list)
        else:
            raise ValueError(f'Ошибка, переданный массив пуст, операция не может быть выполнена!: {array_list}.')
    else:
        raise TypeError(f'Недопустимый тип данных для аргумента: {array_list}.')

# ----------------------------------------------------------------------------------------------------------------------
# Исходные данные:
array: list = [3, 1, 4, 1, 5, 9, 2, 6, 5]



# Вызов функции:
avg = get_avg_in_array(array)
print(avg)

# Тесты:
def test_get_avg_in_array():
    # 1
    assert get_avg_in_array(array) == 4.0
    # 2
    with pytest.raises(ValueError, match='Ошибка, переданный массив пуст, операция не может быть выполнена!:'):
        get_avg_in_array([])
    # 3
    with pytest.raises(TypeError, match='Недопустимый тип данных для аргумента:'):
        get_avg_in_array({})
