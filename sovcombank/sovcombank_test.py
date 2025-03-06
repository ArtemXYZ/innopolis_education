"""
    pass
"""

import signal
import time
from fractions import Fraction
from typing import Generator

# Входные данные (множество рациональных чисел)
rational_numbs = [1.5, 3, 6, 1.5]

# Исходные данные
# numb_days = 2  # Количество дней
# max_lots = 2  # Максимальное количество лотов в день
# capital = 8000  # Начальный капитал


class SharedEquityConstruction:
    """
        Класс расчетных задач в рамках тестового задания.
    """

    def __init__(self):
        self.max_time = 5

    def timeout_handler(self, signum, frame):
        raise TimeoutError(f'Ошибка, превышен лимит времени на выполнение! Допустимое значение: "{self.max_time}".')

    @staticmethod
    def _calculate_percentages(_array: list) -> list:
        """
            Вычисляет процентное выражение для каждого числа из входного списка с использованием Fraction.

            Описание алгоритма:
                1. Проверка типа входного аргумента: если это не список, выбрасывается исключение TypeError.
                2. Вычисление общей суммы всех элементов списка.
                3. Для каждого элемента списка вычисляется его процентное отношение к общей сумме с использованием
                    Fraction для точности.
                4. Результат округляется до трех знаков после запятой и возвращается в виде списка.

            Доказательством его корректности:
                - Использование Fraction гарантирует точность вычислений, избегая ошибок округления при работе с float.
                - Проверка типа входного аргумента обеспечивает корректность входных данных.
                - Генераторное выражение гарантирует, что каждый элемент обрабатывается независимо и корректно.

            Вычислительная сложность алгоритма:
                - O(n), где n — количество элементов в списке. Суммирование элементов и вычисление процентного
                отношения выполняются за линейное время.

            Оценка необходимой памяти:
                - O(n), так как создается новый список с результатами, размер которого пропорционален входному списку.

            Затраченное время на реализацию:
                1 ч (больше ушло на оформление и описание зависимостей, на разработку логики 20 мин).

            :param _array: Список рациональных чисел (долей).
            :type _array: list
            :return: Список процентных выражений, округленных до трех знаков после запятой.
            :rtype: list
        """

        if not isinstance(_array, list):
            raise TypeError(
                f'Недопустимый тип данных: "{type(_array).__name__}", '
                f'для аргумента: "{_array}".'
            )

        # Вычисляем общую сумму долей:
        total = sum(_array)

        # Используем генераторное выражение для вычисления процентных значений
        return [round(float((Fraction(num) / total) * 100), 3) for num in _array]

    def calculate_percentages(self, rational_numbs_array: list) -> list:
        """
            Оборачивает логику  "_calculate_percentages" с учетом ограничений по времени на работу,
            выбрасывая ошибку при превышении лимита.

            :param rational_numbs_array: Список рациональных чисел (долей).
            :type rational_numbs_array: list
            :return: Список процентных выражений, округленных до трех знаков после запятой.
            :rtype: list
        """

        signal.alarm(self.max_time)
        signal.signal(signal.SIGALRM, self.timeout_handler)

        try:

            return self._calculate_percentages(rational_numbs_array)
        except TimeoutError as e:
            print(e)
        finally:
            signal.alarm(0)


class Metatrader:
    """
        Класс расчетных задач в рамках тестового задания.
    """

    def __init__(self, numb_days, max_lots, capital, array):

        self.numb_days = numb_days
        self.max_lots = max_lots
        self.capital = capital
        self.array = array
        # self.lots_list: list = [lots for lots in self.get_line_when_read(self.array)]

    @staticmethod
    def get_line_when_read(array: list[str]) -> Generator[tuple]:
        """
            Обрабатывает входные данные и возвращает генератор кортежей.

            Каждая строка должна быть в формате:
                <день> <название облигации> <цена> <количество>

            :param array: Список строк с данными о лотах.
            :return: Генератор кортежей (день, название, цена, количество).
            :raises TypeError: Если входной массив пуст.
        """

        if not array:
            raise TypeError(f'Ошибка, пустой массив: "{array}".')

        for line in array:

            # Пропуск пустой строки:
            if not line:
                continue

            # Разделение строки на компоненты
            parts = line.split()

            day, name, price, quantity, *extra = parts
            if extra:
                print(f'Предупреждение: строка "{line}" содержит лишние элементы: {extra}')

            # lots_list.append((int(day), name, Fraction(price), int(quantity)))
            # lots.append((int(day), name, float(price), int(quantity)))
            yield int(day), name, Fraction(price), int(quantity)



        #


    def calculate_max_profit(self):
        """
            Рассчитывает максимальный доход и список купленных лотов.

            :param numb_days: Количество дней.
            :param max_lots: Максимальное количество лотов в день.
            :param capital: Начальный капитал.
            :param lots: Список лотов в формате (день, название, цена, количество).
            :return: Максимальный доход и список купленных лотов.
        """

        # Рассчитываем доход для каждого лота
        lot_profits = []

        for lot in self.get_line_when_read(self.array):
            day, name, price, quantity = lot
            cost = price * 10 * quantity  # Стоимость лота
            coupon_income = quantity * 1 * (self.numb_days + 30 - day)  # Доход от купонов
            redemption_income = quantity * 1000  # Доход от погашения
            total_income = coupon_income + redemption_income
            lot_profits.append((total_income, cost, lot))

        # Сортируем лоты по убыванию доходности (доход / стоимость)
        lot_profits.sort(key=lambda x: x[0] / x[1], reverse=True)

        # Покупаем лоты, начиная с самых доходных
        total_income = 0
        purchased_lots = []
        remaining_cash = self.capital

        for profit, cost, lot in lot_profits:
            if cost <= remaining_cash:
                purchased_lots.append(lot)
                total_income += profit
                remaining_cash -= cost

        return total_income, purchased_lots

    @staticmethod
    def print_output(total_income, purchased_lots):
        """
            Вывод результата
        """

        for lot in purchased_lots:
            print(f"{lot[0]} {lot[1]} {lot[2]} {lot[3]}")
        print()




# if __name__ == "__main__":
#     pass


# Описание алгоритма:
# Доказательством его корректности:
# Вычислительная сложность алгоритма
# Оценка необходимой памяти:
# Субъективная оценка сложности задачи по шкале от 1 до 10 (1 - просто, 10 сложно):
# Затраченное время на реализацию:
#     1 ч (больше ушло на оформление и описание зависимостей, на разработку логики 20 мин).