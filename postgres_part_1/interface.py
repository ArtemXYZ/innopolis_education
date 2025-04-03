
import time

from postgres_part_1.manager import PostgeManager

# ======================================================================================================================
class PostgeInterface:
    """
        Инструмент взаимодействия с пользователем.
    """

    def __init__(self):
        self.manager = PostgeManager()

    def power(self):

        # Приветствие и список команд (отображается один раз при запуске)
        print(
            f'Добро пожаловать в систему управления базой данных "PostgeManager"!\n\n'
            f'Выберите действие:\n'
            f'1. Показать данные имеющиеся студентов.\n'
            f'2. Найти данные студента по фамилии.\n'
            f'3. Добавить данные о студенте.\n'
            f'4. Удалить данные студента.\n'
            f'5. Обновить данные студента (номер курса).\n'
            f'6. Выйти\n'
        )

        # Создание базы данных, наполнение, если ее еще не существует.
        self.manager.start_db()

        while True:

            input_value: str = input('Введите команду: ')

            if input_value == '1':
                # Все студенты:
                print(self.manager.get_students_data())
                continue

            elif input_value == '2':

                # Вложенный цикл для подменю
                while True:
                    print(
                        f'Вы находитесь в разделе поиска студентов по фамилии.\n\n'
                        f'Выберите действие:\n'
                        f'1. Ввести фамилию для поиска.\n'
                        f'2. Выйти в главное меню.\n'
                    )

                    sub_input_value: str = input('Введите команду: ')

                    if sub_input_value == '1':

                        sub_sub_input_value: str = input('Введите фамилию: ')

                        try:
                            print(self.manager.get_students_data(last_name=sub_sub_input_value))
                        except Exception as r:
                            print(f'Ошибка: {r}')
                            time.sleep(1)
                            continue

                    elif sub_input_value == '2':
                        break
                    else:
                        print('Неверный ввод. Пожалуйста, выберите действие:')
                    time.sleep(1)

            elif input_value == '3':

                # Вложенный цикл для подменю
                while True:
                    print(
                        f'Вы находитесь в разделе добавления новых данных.\n\n'
                        f'Выберите действие:\n'
                        f'1. Приступить к созданию записи.\n'
                        f'2. Выйти в главное меню.\n'
                    )

                    # Запрос действия от пользователя:
                    sub_input_value: str = input('Введите команду: ')

                    if sub_input_value == '1':

                        first_name: str = input('Введите имя: ')
                        last_name: str = input('Введите фамилию: ')
                        course_number: str = input('Введите номер курса: ')
                        age: str = input('Введите возраст: ')

                        try:
                            self.manager.insert_student_data(
                                first_name=first_name,
                                last_name=last_name,
                                course_number=int(course_number),
                                age=int(age)
                            )
                            continue
                        except Exception as r:
                            print(f'Ошибка: {r}')
                            time.sleep(2)
                            continue

                    elif sub_input_value == '2':
                        break
                    else:
                        print('Неверный ввод. Пожалуйста, выберите действие:')
                    time.sleep(1)

            elif input_value == '4':

                # Вложенный цикл для подменю
                while True:
                    print(
                        f'Вы находитесь в разделе удаления записей.\n\n'
                        f'Выберите действие:\n'
                        f'1. Ввести фамилию студента для удаления.\n'
                        f'2. Выйти в главное меню.\n'
                    )

                    # Запрос действия от пользователя:
                    sub_input_value: str = input('Введите команду: ')

                    if sub_input_value == '1':

                        last_name: str = input('Введите фамилию: ')

                        try:
                            self.manager.delete_student_data(last_name=last_name)
                            continue
                        except Exception as r:
                            print(f'Ошибка: {r}')
                            time.sleep(2)
                            continue

                    elif sub_input_value == '2':
                        break
                    else:
                        print('Неверный ввод. Пожалуйста, выберите действие:')
                    time.sleep(1)

            elif input_value == '5':

                # Вложенный цикл для подменю
                while True:
                    print(
                        f'Вы находитесь в разделе обновления записей.\n\n'
                        f'Выберите действие:\n'
                        f'1. Ввести фамилию студента для обновления.\n'
                        f'2. Выйти в главное меню.\n'
                    )

                    # Запрос действия от пользователя:
                    sub_input_value: str = input('Введите команду: ')

                    if sub_input_value == '1':

                        last_name: str = input('Введите фамилию: ')
                        course_number: str = input('Введите номер курса: ')

                        try:
                            self.manager.update_student_data(last_name, int(course_number))
                            continue
                        except Exception as r:
                            print(f'Ошибка: {r}')
                            time.sleep(2)
                            continue

                    elif sub_input_value == '2':
                        break
                    else:
                        print('Неверный ввод. Пожалуйста, выберите действие:')
                    time.sleep(1)

            elif input_value == '6':
                print('Выход из системы.')
                break

            else:
                print('Неверный ввод. Пожалуйста, выберите действие от 1 до 6.')

            time.sleep(1)

    def __str__(self):
        return (f'{self.__class__.__name__}')

    def __repr__(self):
        return (f'{self.__class__.__name__}')




