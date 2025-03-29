"""
    Простой калькулятор, выполняющий:
        Сложение
        Вычитание
        Умножение
        Деление
"""

import math



class Calculator:
    """
        Класс калькулятор (сложение, вычитание, умножение, деление).
    """

    def add(self, a, b):
        """ Сложение двух чисел"""
        return a + b

    def subtract(self, a, b):
        """Вычитание двух чисел"""
        return a - b

    def multiply(self, a, b):
        """Умножение двух чисел"""
        return a * b

    def divide(self, a, b):
        """Деление двух чисел"""
        if b == 0:
            raise ValueError("Нельзя делить на ноль!")
        return a / b

    def power(self, a, b):
        """Возведение числа a в степень b"""
        return a ** b

    def sqrt(self, a):
        """Извлечение квадратного корня из числа a"""
        if a < 0:
            raise ValueError("Нельзя извлечь корень из отрицательного числа!")
        return math.sqrt(a)

    def percent(self, a, b):
        """Вычисление b процентов от числа a"""
        return (a * b) / 100

    def factorial(self, a):
        """Вычисление факториала числа a"""
        if a < 0:
            raise ValueError("Факториал определен только для неотрицательных чисел!")
        return math.factorial(int(a))

def main():
    calc = Calculator()

    print("Добро пожаловать в калькулятор!")
    print("Доступные операции:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Квадратный корень")
    print("7. Процент от числа")
    print("8. Факториал")

    try:
        choice = int(input("Выберите операцию (1-8): "))

        if choice in (1, 2, 3, 4, 5):
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))

            if choice == 1:
                result = calc.add(num1, num2)
                print(f"Результат: {num1} + {num2} = {result}")
            elif choice == 2:
                result = calc.subtract(num1, num2)
                print(f"Результат: {num1} - {num2} = {result}")
            elif choice == 3:
                result = calc.multiply(num1, num2)
                print(f"Результат: {num1} * {num2} = {result}")
            elif choice == 4:
                result = calc.divide(num1, num2)
                print(f"Результат: {num1} / {num2} = {result}")
            elif choice == 5:
                result = calc.power(num1, num2)
                print(f"Результат: {num1} ^ {num2} = {result}")

        elif choice in (6, 8):
            num = float(input("Введите число: "))

            if choice == 6:
                result = calc.sqrt(num)
                print(f"Квадратный корень из {num} = {result}")
            elif choice == 8:
                result = calc.factorial(num)
                print(f"Факториал {num}! = {result}")

        elif choice == 7:
            num = float(input("Введите число: "))
            percent = float(input("Введите процент: "))
            result = calc.percent(num, percent)
            print(f"{percent}% от {num} = {result}")

        else:
            print("Неверный выбор операции!")

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()