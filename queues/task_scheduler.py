"""
    * Учебная реализация симуляции работы планировщика с использованием очереди.
                                        ***
    Система планировщика задач для небольшого сервера.
    Приложение умеет добавлять задачи в очередь и обрабатывать их в порядке поступления.
    Каждая задача имеет определенное время выполнения.
"""

import heapq
import time


class Task:
    """
        Класс-представление отдельной задачи.
        Используем магические методы для определения сравнения их по атрибутам.
    """

    def __init__(self, name=None, duration=None):
        # Название задачи:
        self.name: str = name if name else None
        #  Время выполнения задачи в секундах.
        self.duration: int = duration if duration else None

    def __lt__(self, other):
        """
            Определение сравнения объектов: "если меньше".
        """
        return self.duration < other.duration

    def __gt__(self, other):
        """
            Определение сравнения объектов: "если больше".
        """
        return self.duration > other.duration

    def __eq__(self, other):
        """
            Определение сравнения объектов: "если равно".
        """
        return self.duration == other.duration

    def __str__(self):
        return (
            # f'{self.__class__.__name__} '
            f'Имя задачи: {self.name}, время выполнения в секундах: {self.duration}'
        )

    def __repr__(self):
        return (
            # f'{self.__class__.__name__} '
            f'Имя задачи: {self.name}, время выполнения в секундах: {self.duration}'
        )


class TaskScheduler(Task):
    """
        Класс управления очередью задач.
    """

    def __init__(self):
        super().__init__()
        self.queue_list = []
        self.status_data = {1: 'Pending', 2: 'In Progress...', 3: 'Completed'}

    def add_task(self, name, duration):
        """
            Добавляет задачу в очередь с приоритетом.
        """
        task = Task(name=name, duration=duration)
        heapq.heappush(self.queue_list, task)

    def del_task(self, status: bool = False, sleep_time: bool = False) -> Task:
        """
            Удаляет и возвращает элемент с наивысшим приоритетом.
            :param status: Режим вывода на печать статуса.
            :param sleep_time: Режим при котором учитывается время выполнения.
        """
        if not self.is_empty:

            sleep_time_value = self.get_task.duration

            if status:
                print(f'Статус: {self.status_data.get(1)}, {self.get_task.__str__}.')

            if status:
                print(f'Статус: {self.status_data.get(2)}')

            if sleep_time:
                time.sleep(sleep_time_value)

            task: Task = heapq.heappop(self.queue_list)

            if status:
                print(f'Статус: {self.status_data.get(3)}.')



    @property
    def get_task(self) -> Task | None:
        """
            Возвращает элемент с наивысшим приоритетом.
        """
        # print(self.is_empty)

        if not self.is_empty:
            # print(self.is_empty)
            # first_element
            return self.queue_list[0]
        raise IndexError('Список пуст! Невозможно извлечь задачу.')

    @property
    def is_empty(self) -> bool:
        """
            Проверяет, пуста ли очередь задач.

        """
        return len(self.queue_list) == 0

    @property
    def task_count(self) -> int:
        """Возвращает количество задач в очереди."""
        return len(self.queue_list)

    def execute_tasks(self):
        """
            Последовательно выполняет все задачи в очереди.
            Каждая задача занимает определенное время (duration).
            После выполнения задачи удаляет её из очереди.
        """

        # ----------------------------------------------------
        if self.is_empty:
            print('Очередь пуста! Работа метода "execute_tasks" остановлена.')  # raise ValueError

        # ----------------------------------------------------
        print(f'Запуск обработки данных очереди длинной в {self.task_count} элементов:')

        while not self.is_empty:

            task: Task = self.del_task(status=True, sleep_time=False)

        print(f'Обработка данных очереди завершена.')

    def __str__(self):
        return (
            f'{self.__class__.__name__}. '
            f'Список задач: {self.queue_list}'
        )

    def __repr__(self):
        return (
            f'{self.__class__.__name__}. '
            f'Список задач: {self.queue_list}'
        )


# Пример использования
tasks = TaskScheduler()
tasks.add_task('tasks_1', 9)
tasks.add_task('tasks_2', 4)
tasks.add_task('tasks_3', 2)
tasks.add_task('tasks_4', 5)
tasks.add_task('tasks_5', 6)
tasks.add_task('tasks_6', 7)

# 6
# print(tasks.task_count())

# TaskScheduler. Список задач: [Имя задачи: tasks_4, Время выполнения в секундах: 33, ...]
# print(tasks)


# Задача tasks_4 удалена из очереди, время выполнения: 33. Осталось элементов : 5.
# tasks.del_task()



# Запуск обработки данных очереди длинной в 6 элементов:
# Статус: Pending, <bound method Task.__str__ of Имя задачи: tasks_3, время выполнения в секундах: 2>.
# Статус: In Progress...
# Статус: Completed.
# Статус: Pending, <bound method Task.__str__ of Имя задачи: tasks_2, время выполнения в секундах: 4>.
# Статус: In Progress...
# Статус: Completed.
# Статус: Pending, <bound method Task.__str__ of Имя задачи: tasks_4, время выполнения в секундах: 5>.
# Статус: In Progress...
# Статус: Completed.
# Статус: Pending, <bound method Task.__str__ of Имя задачи: tasks_5, время выполнения в секундах: 6>.
# Статус: In Progress...
# Статус: Completed.
# Статус: Pending, <bound method Task.__str__ of Имя задачи: tasks_6, время выполнения в секундах: 7>.
# Статус: In Progress...
# Статус: Completed.
# Статус: Pending, <bound method Task.__str__ of Имя задачи: tasks_1, время выполнения в секундах: 9>.
# Статус: In Progress...
# Статус: Completed.
# Обработка данных очереди завершена.
tasks.execute_tasks()
