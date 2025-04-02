"""
    Менеджер управления задачами.
"""

import asyncio
import time

from midl_attestation_2.commands import PingCommand
from src.algorithms_core.main import AlgorithmsForeInstanceClasses
from midl_attestation_2.tasks import Task
from src.services.tools import ServiceTols


class TaskManager(Task, ServiceTols, AlgorithmsForeInstanceClasses):
    """
        Менеджер управления задачами.
        Реализация паттерна "Одиночка".
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """
            :args task_list: Имитация базы данных, основное хранилище данных.
        """

        super().__init__()
        self.task_list: list[Task] = []
        self.ping = PingCommand()

    @property
    def _auto_increment(self) -> int:
        """
            Метод автоматически рассчитывает task_id для новой задачи.

            :rtype int.
            :return task_id (1 - случае пустого списка задач или + 1 к айди последней задачи).
        """

        return 1 if self.is_empty_array(self.task_list) else self.task_list[-1].task_id + 1

    @property
    def _get_timestamp(self):
        """
            Получение текущего времени в timestamp (float).
        """

        return time.time()  # Пример: 1711987265.123456

    def create_task(self, title, time_delta):
        """
            Добавление новой задачи в список.
        """

        task_obj = Task(
            task_id=self._auto_increment,
            creation_time=self._get_timestamp,
            title=title,
            command=self.ping,
        )

        self.task_list.append(task_obj)

    def delete_task(self, task_id: int) -> None:
        """
            Удаление задачи по её идентификатору.
        """

        self.validator(task_id, int)
        index = self._searcher(self.task_list, task_id, 'task_id')
        self.task_list.pop(index)

    async def run_all_tasks(self):
        """
            Запуск всех задач (асинхронно).
        """

        if self.task_list:
            # Создаем список корутин, вызывая execute() для каждой задачи
            coroutines = [task.execute() for task in self.task_list]
            await asyncio.gather(*coroutines)
        else:
            print('В системе не зарегистрировано ни одной задачи, запуск остановлен.')

    # view_tasks_list
    def get_sorting_tasks(self) -> list:
        """
            Просмотр списка задач, отсортированного по времени создания.
        """

        return self._selection_sort(self.task_list, 'creation_time')

    def search_task(self, task_id) -> str:
        """
            Поиск задачи по идентификатору. Метод поиска: линейный.
            :rtype, str.
            :return: Описание задачи.
        """

        self.validator(task_id, int)
        index = self._searcher(self.task_list, task_id, 'task_id')

        return self.task_list[index].title
