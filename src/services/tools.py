"""
    Модуль содержит вспомогательные методы для обеспечения работы других участков кода, содержащих основную логику.
"""


class ServiceTols:
    """
        Класс содержит данные по книгам в виде списка.
    """

    def __init__(self):
       pass

    @staticmethod
    def validator(value: any, *check_type: type[any]) -> bool:
        """
            *** Функция валидации аргументов. ***
        """

        if not isinstance(value, check_type):
            raise TypeError(f'Недопустимый тип данных: "{type(value).__name__}", для аргумента: "{value}".')

        return True
    @staticmethod
    def is_empty_array(array) -> bool:
        """
            Проверяет, пуст ли массив: вернет True, если пуст.
        """

        return len(array) == 0  # True

    @staticmethod
    def siz_array(array) -> int:
        """
            Возвращает количество элементов в массиве.
        """
        return len(array)
