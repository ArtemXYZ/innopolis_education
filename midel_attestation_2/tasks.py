"""
    Менеджер управления задачами.
"""
import time

from src.algorithms_core.main import AlgorithmsForeInstanceClasses
from src.services.tools import ServiceTols
from src.queues.queues_by_instance_classes import QueueByInstanceClasses



# ----------------------------------------------------------------------------------------------------------------------
class Task(ServiceTols):
    """
        Модель объекта "Задача".
    """

    def __init__(
            self,
            task_id: int = None,
            creation_time: float = None,
            title: str = None
    ) -> None:
        """
            Все атрибуты по умолчанию None, что бы можно было наследоваться без явной передачи аргументов.

            :arg task_id: id задачи.
            :arg creation_time: Время создания задачи.
            :arg title: Название задачи.
        """

        super().__init__()
        self.task_id = task_id if self.validator(task_id, int | None) else ...
        self.creation_time = creation_time if self.validator(creation_time, float | None) else ...
        self.title = title if self.validator(title, str | None) else ...

    @property
    def _count_attrs(self):
        """
            Считает количество параметров в классе.
            Со временем характеристики могут добавляться, поэтому данный метод предназначен для точного определения
            их количества.
        """

        return len(vars(self))

    def __str__(self):
        # return [(k, v) for k, v in  vars(self).items()]
        return vars(self).__str__()

    # Переопределяем после dataclass:
    def __repr__(self):
        return vars(self).__str__()


class TaskManager(Task, ServiceTols, AlgorithmsForeInstanceClasses):
    """
        Менеджер управления задачами.
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
        self.normal_queue = QueueByInstanceClasses()


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

    def create_task(self, title):
        """
            Добавление новой задачи в список.
        """

        task_obj = Task(
            task_id=self._auto_increment,
            creation_time=self._get_timestamp,
            title=title,
        )

        self.task_list.append(task_obj)

    def delete_task(self, task_id: int) -> None:
        """
            Удаление задачи по её идентификатору.
        """

        self.validator(task_id, int)
        index = self._searcher(self.task_list, task_id, 'task_id')
        self.task_list.pop(index)

    def run_all_tasks(self):
        """
            Запуск всех задач (асинхронно).
        """

        pass

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




d = Task()

print(d)
