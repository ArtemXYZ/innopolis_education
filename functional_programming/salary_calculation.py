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
    pass
    tls.validator(percentage, int)


def final_salary(base_salary, bonus):
    """
        Функция.
    """
    tls.validator(percentage, int)
    pass


def calculate_hours(hours_per_day, days):
    """
        Функция.
    """
    tls.validator(percentage, int)
    pass

def calculate_gross_salary(hours, hourly_rate):
    """
        Функция.
    """
    tls.validator(percentage, int)
    pass

def composed_salary_function(hours_per_day, days, hourly_rate):
    """
        Функция.
    """
    tls.validator(percentage, int)
    pass

def calculate_net_salary(gross_salary):
    """
        Функция.
    """
    tls.validator(percentage, int)
    pass

def apply_bonus(salary, bonus):
    """
        Функция.
    """
    tls.validator(percentage, int)
    pass


def final_salary_composition(gross_salary, bonus):
    """
        Функция.
    """
    tls.validator(percentage, int)
    pass


# 1
print(hours_per_day(8)(20))

# 2
print(bonus_percentage(10)(3000))