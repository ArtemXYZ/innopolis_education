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

    def __init__(self, name = None, duration = None):
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
            f'Имя задачи: {self.name}, Время выполнения в секундах: {self.duration}'
        )

    def __repr__(self):
        return (
            # f'{self.__class__.__name__} '
            f'Имя задачи: {self.name}, Время выполнения в секундах: {self.duration}'
        )





class TaskScheduler(Task):
    """
        Класс управления очередью задач.
    """

    def __init__(self):
        super().__init__()
        self.queue_list = []

    def add_task(self, name, duration):
        """
            Добавляет задачу в очередь с приоритетом.
        """
        task = Task(name=name, duration=duration)
        heapq.heappush(self.queue_list, task)

    def del_task(self) -> Task:
        """
            Удаляет и возвращает элемент с наивысшим приоритетом.
        """
        if not self.is_empty():
            task: Task = heapq.heappop(self.queue_list)

            # Имитация работы:
            time.sleep(task.duration)

            print(
                f'Задача {task.name} удалена из очереди, время выполнения: {task.duration}. '
                f'Осталось элементов : {self.task_count()}.'
            )
            return task


        raise IndexError("dequeue from empty queue")

    def is_empty(self) -> bool:
        """
            Проверяет, пуста ли очередь задач.
        """

        return len(self.queue_list) == 0

    def task_count(self) -> int:
        """Возвращает количество задач в очереди."""
        return len(self.queue_list)


    def execute_tasks(self):
        """
            Последовательно выполняет все задачи в очереди.
            Каждая задача занимает определенное время (duration).
            После выполнения задачи удаляет её из очереди.
        """

        status = 'Pending'
        'In Progress'
        'Completed'

        if self.is_empty():
            print('Очередь пуста! Работа метода "execute_tasks" остановлена.')  # raise ValueError

        print(f'Обработка данных очереди:')
        while not self.is_empty():

            task: Task = self.del_task()



            # print(
            #     f'Задача {task.name} завершена, время выполнения: {task.duration}. '
            #     f'Осталось элементов в очереди: {self.task_count()}.'
            # )


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



# Обработка данных очереди:
# Задача tasks_4 удалена из очереди, время выполнения: 33. Осталось элементов : 5.
# Задача tasks_5 удалена из очереди, время выполнения: 123. Осталось элементов : 4.
# Задача tasks_3 удалена из очереди, время выполнения: 456. Осталось элементов : 3.
# Задача tasks_1 удалена из очереди, время выполнения: 665. Осталось элементов : 2.
# Задача tasks_6 удалена из очереди, время выполнения: 2234. Осталось элементов : 1.
# Задача tasks_2 удалена из очереди, время выполнения: 5235. Осталось элементов : 0.
# tasks.execute_tasks()