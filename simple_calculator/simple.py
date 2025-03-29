"""
    Простой калькулятор, выполняющий:
        Сложение
        Вычитание
        Умножение
        Деление
"""

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


def main():
    calc = Calculator()

    print("Добро пожаловать в калькулятор!")
    print("Доступные операции:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

    try:
        choice = int(input("Выберите операцию (1/2/3/4): "))
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
        else:
            print("Неверный выбор операции!")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()