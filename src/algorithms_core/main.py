"""
    Модуль содержит представление всех доступных алгоритмов в проекте.
"""

from src.algorithms_core.searches import SearchByInstanceClasses
from src.algorithms_core.sorts import SortByInstanceClasses


class AlgorithmsForeInstanceClasses(SearchByInstanceClasses, SortByInstanceClasses):
    """
        Класс-представление объединяет все алгоритмы.
    """

    def __init__(self):
        super().__init__()

    def __str__(self):
        return f'{self.__class__.__name__}'

    def __repr__(self):
        return f'{self.__class__.__name__}'
