# ----------------------------------------------------------------------------------------------------------------------
import time

from midl_attestation_2.manage import TaskManager


class ApplicationInterface:
    """
        Инструмент взаимодействия с пользователем.
    """

    def __init__(self):
        self.manager = TaskManager()

    async def power(self):
        # Приветствие и список команд (отображается один раз при запуске)
        print(
            f'Добро пожаловать в систему управления "TaskManager"!\n\n'
            f'Выберите действие:\n'
            f'1. Показать список задач.\n'
            f'2. Найти задачу по идентификатору.\n'
            f'3. Добавить задачу.\n'
            f'4. Удалить задачу.\n'
            f'5. Запустить все задачи.\n'
            f'6. Выйти\n'
        )

        while True:

            input_value: str = input('Введите команду: ')

            if input_value == '1':
                print(self.manager.get_sorting_tasks)
                continue

            elif input_value == '2':

                # Вложенный цикл для подменю
                while True:
                    print(
                        f'Вы находитесь в разделе поиска задач.\n\n'
                        f'Выберите действие:\n'
                        f'1. Ввести идентификатор для поиска.\n'
                        f'2. Выйти в главное меню.\n'
                    )

                    sub_input_value: str = input('Введите команду: ')

                    if sub_input_value == '1':

                        sub_sub_input_value: str = input('Введите идентификатор задачи: ')

                        try:
                            print(self.manager.search_task(task_id=int(sub_sub_input_value)))
                        except Exception as r:
                            print(f'Ошибка: {r}')
                            time.sleep(2)
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
                        f'Вы находитесь в разделе создания задач.\n\n'
                        f'Выберите действие:\n'
                        f'1. Ввести название задачи для создания.\n'
                        f'2. Выйти в главное меню.\n'
                    )

                    # Запрос действия от пользователя:
                    sub_input_value: str = input('Введите команду: ')

                    if sub_input_value == '1':

                        sub_sub_input_value: str = input('Введите название задачи: ')

                        try:
                            task = self.manager.create_task(title=sub_sub_input_value)
                            print(f'Задача успешно создана {task}')
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
                        f'Вы находитесь в разделе удаления задач.\n\n'
                        f'Выберите действие:\n'
                        f'1. Ввести идентификатор задачи для удаления.\n'
                        f'2. Выйти в главное меню.\n'
                    )

                    # Запрос действия от пользователя:
                    sub_input_value: str = input('Введите команду: ')

                    if sub_input_value == '1':

                        sub_sub_input_value: str = input('Введите идентификатор задачи: ')

                        try:
                            self.manager.delete_task(task_id=int(sub_sub_input_value))
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

                try:
                    await self.manager.run_all_tasks()
                    continue
                except Exception as r:
                    print(f'Ошибка: {r}')
                    time.sleep(2)
                    continue

            elif input_value == '6':
                print('Выход из системы.')
                break

            else:
                print('Неверный ввод. Пожалуйста, выберите действие от 1 до 11.')

            time.sleep(1)

    def __str__(self):
        return (f'{self.__class__.__name__}')

    def __repr__(self):
        return (f'{self.__class__.__name__}')




