
# Вам необходимо разработать систему для учета рабочего времени сотрудников и расчета их зарплаты,
# используя каррирование и композицию функций. Система должна включать функции для расчета часов,
# применения налогов и бонусов, а также форматирования информации о зарплате.

# 1. Создание каррированных функций:

# Функция для расчета отработанных часов
# Напишите каррированную функцию hours_per_day(hours) которая возвращает функцию,
# которая умножает количество отработанных дней на заданное количество часов в день.
# Например, hours_per_day(8)(20) должно возвращать 160, так как 8 часов в день умножить на 20 дней равно 160.

def hours_per_day(hours):
    # Ваш код

# Пример использования
result = hours_per_day(8)(20)  # 160


# Функция для расчета бонусов
# Напишите каррированную функцию bonus_percentage(percentage) которая возвращает функцию,
# которая вычисляет бонус от зарплаты. Например, bonus_percentage(10)(3000) должно возвращать 300,
# так как бонус 10% от 3000 — это 300.

def bonus_percentage(percentage):
    # Ваш код

# Пример использования
result = bonus_percentage(10)(3000)  # 300


# 2. Частичное применение:

# Функция для расчета чистой зарплаты
# Напишите функцию net_salary(gross_salary, tax_rate) для расчета чистой зарплаты после вычета налогов.
# Используйте functools.partial для создания функции с фиксированной налоговой ставкой, например, 20%.

from functools import partial

def net_salary(gross_salary, tax_rate):
    # Ваш код

# Создаем функцию с фиксированным налогом 20%
tax_20 = partial(net_salary, tax_rate=0.20)
result = tax_20(5000)  # 5000 - (5000 * 0.20) = 4000


# Функция для расчета итоговой зарплаты с учетом бонусов
# Напишите функцию final_salary(base_salary, bonus) для расчета итоговой зарплаты с учетом бонусов.
# Используйте functools.partial для создания функции с фиксированным бонусом, например, 500.

from functools import partial

def final_salary(base_salary, bonus):
    # Ваш код

# Создаем функцию с фиксированным бонусом 500
bonus_500 = partial(final_salary, bonus=500)
result = bonus_500(3000)  # 3000 + 500 = 3500


# 3. Композиция функций

# Функции для расчета заработной платы
# Напишите функции calculate_hours(hours_per_day, days) и calculate_gross_salary(hours, hourly_rate),
# где calculate_hours вычисляет общее количество отработанных часов,
# а calculate_gross_salary вычисляет заработную плату до вычета налогов.
# Затем создайте композицию этих функций, чтобы получить конечную зарплату до вычета налогов.

def calculate_hours(hours_per_day, days):
    # Ваш код

def calculate_gross_salary(hours, hourly_rate):
    # Ваш код
def composed_salary_function(hours_per_day, days, hourly_rate):
    # Ваш код

# Пример использования
result = composed_salary_function(8, 20, 25)  # (8 * 20) * 25 = 4000

# Функции для итогового расчета
# Напишите функции calculate_net_salary(gross_salary) и apply_bonus(salary, bonus).
# Создайте композицию этих функций, чтобы получить чистую зарплату после применения бонусов и вычета налогов.

def calculate_net_salary(gross_salary):
    # Ваш код

def apply_bonus(salary, bonus):
    # Ваш код


def final_salary_composition(gross_salary, bonus):
    # Ваш код

# Пример использования
result = final_salary_composition(4000, 300)  # (4000 + 300) - (4000 * 0.20) = 3800