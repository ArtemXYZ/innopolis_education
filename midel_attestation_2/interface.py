

# ----------------------------------------------------------------------------------------------------------------------
import time

from midel_attestation_2.tasks import TaskManager


class ApplicationInterface(TaskManager):
    """
        Инструмент взаимодействия с пользователем.
    """

    def __init__(self):
        super().__init__()

    def power(self):
        # Приветствие и список команд (отображается один раз при запуске)
        print(
            f'Добро пожаловать в систему управления "LogisticsMachine"!\n\n'
            f'Выберите действие:\n'
            f'1. Показать список задач на доставку.\n'
            f'2. Сортировать список задач на доставку по весу груза.\n'
            f'3. Сортировать список задач на доставку по времени доставки.\n'
            f'4. Сортировать список задач на доставку по номеру доставки.\n'
            f'5. Найти задачу на доставку по времени доставки.\n'
            f'6. Найти задачу на доставку по по номеру доставки.\n'
            f'7. Добавить задачу.\n'
            f'8. Удалить задачу.\n'
            f'9. Запустить доставку по очереди.\n'
            f'10. Запустить доставку по приоритету.\n'
            f'11. Выйти\n'
        )

        while True:

            input_value: int = input('Введите команду: ')

            if input_value == '1':
                print(self.delivery_list)

            elif input_value == '2':
                print(self.sort_delivery_list_by_weight_cargo())

            elif input_value == '3':
                print(self.sort_delivery_list_by_time_delivery())

            elif input_value == '4':
                print(self.sort_delivery_list_by_delivery_id())

            elif input_value == '5':

                input_value: str = input('Введите time_delivery: ')

                print(self.search_delivery_elem_by_time_delivery(int(input_value)))

            elif input_value == '6':

                input_value: str = input('Введите delivery_id: ')

                print(self.search_delivery_elem_by_delivery_id(int(input_value)))

            elif input_value == '7':
                while True:  # Вложенный цикл для подменю
                    print(
                        f'Вы находитесь в разделе оформления заказов на доставку.\n\n'
                        f'Выберите действие:\n'
                        f'1. Ввести данные.\n'
                        f'2. Выйти в главное меню.\n'
                    )

                    # Запрос действия от пользователя:
                    sub_input_value: int = input('Введите команду: ')

                    # Обработка команд подменю
                    if sub_input_value == '1':
                        # Цикл для повторного ввода
                        while True:
                            print('Вы выбрали ввод данных.')

                            #
                            from_point: str = input('Введите место отправления: ')
                            to_point: str = input('Введите место назначения: ')
                            weight_cargo: int | float = float(input('Введите вес груза: '))
                            time_delivery: int = int(input('Введите время доставки: '))
                            task_name: str = input('Введите пометку для груза (название): ')
                            priority: int = int(input('Введите приоритет: '))
                            try:
                                self.add_delivery_task(
                                    from_point,
                                    to_point,
                                    weight_cargo,
                                    time_delivery,
                                    task_name,
                                    priority
                                )
                                print('Данные успешно сохранены!')
                                break
                            except Exception as e:
                                print(f'Ошибка: {e}.')

                        continue

                    elif sub_input_value == '2':
                        print('Возврат в главное меню.')
                        break  # Выход из вложенного цикла и возврат в главное меню
                    else:
                        print('Неверная команда. Пожалуйста, выберите 1, 2.')

            elif input_value == '8':
                while True:
                    print(f'Вы в меню удаления задач.')
                    search_delivery_id: int = int(input(f'Если вы хотите удалить книгу, введите номер доставки: '))

                    if search_delivery_id:

                        self.remove_delivery_task('delivery_id', search_delivery_id)
                        print('Задача успешно удалена!')
                        break
                    else:
                        continue
                continue

            elif input_value == '9':
                while True:
                    print(f'Вы в меню запуска доставки по очереди.\n')

                    try:
                        self.process_normal_queue()
                        break
                    except Exception as r:
                        print(f'Ошибка: {r}')


            elif input_value == '10':
                print(f'Вы в меню запуска доставки по приоритету.\n')
                try:
                    self.process_stack()
                    break
                except Exception as r:
                    print(f'Ошибка: {r}')


            elif input_value == '11':
                print('Выход из системы.')
                break


            else:
                print('Неверный ввод. Пожалуйста, выберите действие от 1 до 11.')

            time.sleep(1)

    def __str__(self):
        return (f'{self.__class__.__name__}')

    def __repr__(self):
        return (f'{self.__class__.__name__}')



# test = Interface()
# test.power()

