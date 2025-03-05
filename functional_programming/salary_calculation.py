"""
    Система расчета зарплаты.
    Предназначена для учета рабочего времени сотрудников и расчета их зарплаты, расчета часов,
    применения налогов и бонусов, а также форматирования информации.
"""

from src.services.tools import ServiceTols
from functools import partial

tls = ServiceTols()

# class ServiceTols:
#     """
#         Класс содержит данные по книгам в виде списка.
#     """
#
#     def __init__(self):
#        pass
#
#     @staticmethod
#     def validator(value: any, *check_type: type[any]) -> bool:
#         """
#             *** Функция валидации аргументов. ***
#         """
#
#         if not isinstance(value, check_type):
#             raise TypeError(f'Недопустимый тип данных: "{type(value).__name__}", для аргумента: "{value}".')

def hours_per_day(hours: int):
    """
        Функция для расчета отработанных часов.

         Каррированная функция: умножает количество отработанных дней на заданное количество часов в день.
        :param hours:
        :return:
    """
    tls.validator(hours, int)

    def days_job(days: int):
        """
            Вложенная функция.
            :param days:
            :return:
        """
        tls.validator(days, int)
        return hours * days

    return days_job


def bonus_percentage(percentage: int):
    """
        Функция вычисляет бонус от зарплаты.
    """
    tls.validator(percentage, int)

    def salary_employee(salary: int | float):
        """
            Вложенная функция.
        """

        tls.validator(salary, int | float)

        return salary / 100 * percentage if salary and percentage else None

    return salary_employee


def net_salary(gross_salary, tax_rate):
    """
        Функция для расчета чистой зарплаты.
    """

    tls.validator(gross_salary, int)
    tls.validator(tax_rate, float)

    return gross_salary - (gross_salary * tax_rate)

def final_salary(base_salary, bonus):
    """
        Функция для расчета итоговой зарплаты с учетом бонусов.
    """
    tls.validator(base_salary, int)
    tls.validator(bonus, int)

    return base_salary + bonus

# _________________________________________ 3. Композиция функций
def calculate_hours(hours_per_day, days):
    """
        Функция для расчета вычисляет общее количество отработанных часов.
    """
    tls.validator(hours_per_day, int)
    tls.validator(days, int)

    return hours_per_day * days

def calculate_gross_salary(hours, hourly_rate):
    """
        Функция вычисляет заработную плату до вычета налогов.
    """
    tls.validator(hours, int)
    tls.validator(hourly_rate, int)

    return hours * hourly_rate

def composed_salary_function(hours_per_day, days, hourly_rate):
    """
        Функция для расчета конечной зарплаты до вычета налогов.
    """

    return calculate_gross_salary(calculate_hours(hours_per_day, days), hourly_rate)

# _________________________________________
def calculate_net_salary(gross_salary):
    """
        Функция.
    """

    tls.validator(gross_salary, int)

    return gross_salary * 0.20

def apply_bonus(salary, bonus):
    """
        Функция расчета зарплаты с учетом бонусов.
    """

    tls.validator(salary, int)
    tls.validator(bonus, int)

    return salary + bonus


def final_salary_composition(gross_salary, bonus):
    """
        Функция для расчета чистой зарплаты после применения бонусов и вычета налогов.
    """

    tls.validator(gross_salary, int)
    tls.validator(bonus, int)

    salary_with_bonus = apply_bonus(gross_salary, bonus)
    net_salary = calculate_net_salary(gross_salary)

    return salary_with_bonus - net_salary


# 1 Функция для расчета отработанных часов:
print(hours_per_day(8)(20))

# 2 Функция для расчета бонусов:
print(bonus_percentage(10)(3000))

# 3 Создаем функцию с фиксированным налогом 20%:
tax_20 = partial(net_salary, tax_rate=0.20)
print(tax_20(5000))

# 4 Создаем функцию с фиксированным бонусом 500:
bonus_500 = partial(final_salary, bonus=500)
print(bonus_500(3000))

# 5 Функции для расчета заработной платы:
print(composed_salary_function(8, 20, 25))

# 6 Функции для итогового расчета:
print(final_salary_composition(4000, 300))
