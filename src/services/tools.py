"""
    Модуль содержит вспомогательные методы для обеспечения работы других участков кода, содержащих основную логику.
"""


class ServiceTols:
    """
        Класс содержит данные по книгам в виде списка.
    """

    def __init__(self):
       ...

    @staticmethod
    def _validator(value: any, *check_type: type[any]) -> None:
        """
            *** Функция валидации аргументов. ***
        """

        if not isinstance(value, check_type):
            raise TypeError(f'Недопустимый тип данных: "{type(value).__name__}", для аргумента: "{value}".')



    def _check_params_by_count(self, param_key: int):
        """
            Проверка валидности переданного индекса параметра (не больше, не меньше, чем есть в классе атрибутов)
            :param param_key:  Индекс в кортеже к которому обращаемся для извлечения одного из типа данных по
            книге.
        """

        if param_key >= 0:
            # Определение границ диапазона допустимого индекса:
            index_limit = self.count_attrs_ebook - 1

            # Проверка на допустимый диапазон (по количеству параметров для book):
            if param_key >= 0 and param_key <= index_limit:  # 0-2

                return param_key

            raise ValueError(
                f'Ошибка передачи индекса: недопустимый диапазон! '
                f'Получено значение: {param_key}, допустимый предел: от 0 до {index_limit}.'
            )
