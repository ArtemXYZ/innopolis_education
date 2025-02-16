"""
    Учебная реализация программы для анализа и обработки данных логистической компании.
    Программа хранит данные о поставках, сортировать их по различным критериям, обрабатывать запросы на получение
    информации и оптимизирует процесс обработки с помощью различных алгоритмов.
"""


# import time
from dataclasses import dataclass


from src.algorithms_core.main import AlgorithmsForeInstanceClasses
from src.services.tools import ServiceTols




# ----------------------------------------------------------------------------------------------------------------------
@dataclass(order=True)
class Delivery:
    """
        Класс-представление данных о доставке.

        Используем магические методы для определения сравнения их по атрибутам с помощью встроенного модуля dataclasses.
        Он автоматически генерирует такие методы как (__eq__, __repr__, * __lt__, __le__, __gt__, __ge__) и другие
        на основе атрибутов класса.
        Это избавляет вас от необходимости писать методы вручную. Параметр order=True определяет поведение при котором
        будут созданы все методы сравнения на основе атрибутов класса. По умолчанию генерируются только методы:
        __eq__ и __repr__.

    """

    def __init__(
            # Все атрибуты по умолчанию None, что бы можно было наследоваться без явной передачи аргументов.
            self,
            delivery_id=None,
            from_point=None,
            to_point=None,
            weight_cargo=None,
            time_delivery=None,
            task_name=None,
    ):

        self.delivery_id = delivery_id      # id доставки.
        self.from_point = from_point        # Пункт отправления.
        self.to_point = to_point            # Пункт назначения.
        self.weight_cargo = weight_cargo    # Вес груза.
        self.time_delivery = time_delivery  # Время доставки.
        self.task_name = task_name          # Название задачи:


    @property
    def _count_attrs(self):
        """
            Считает количество параметров в классе, характеризующих книгу.
            Со временем характеристики могут добавляться, поэтому данный метод предназначен для точного определения
            их количества.
        """

        return len(vars(self))

    @property
    def get_tuple_view_delivery(self) -> tuple:
        """
            Возвращаем данные о книге в кортеже (обеспечиваем защиту от изменений, немутабельность).
            Кроме того, это позволит обращаться точно по индексу к требуемому типу информации,
            а для сортировки будет выведен строковый эквивалент.
        """

        return (
            self.delivery_id,  # id доставки.
            self.from_point,  # Пункт отправления.
            self.to_point,  # Пункт назначения.
            self.weight_cargo,  # Вес груза.
            self.time_delivery,  # Время доставки.
            self.task_name,  # Название задачи:
        )

    def __str__(self):
        return (
            f'{self.__class__.__name__}: '
            f'id доставки: {self.delivery_id}, '
            f'пункт отправления: {self.from_point}, '
            f'пункт назначения: {self.to_point},'
            f'вес груза: {self.weight_cargo}, '
            f'время доставки: {self.time_delivery}, '
            f'название задачи: {self.task_name}, '
        )

    # Переопределяем после dataclass:
    def __repr__(self):
        return (
            f'{self.__class__.__name__}: '
            f'id доставки: {self.delivery_id}, '
            f'пункт отправления: {self.from_point}, '
            f'пункт назначения: {self.to_point},'
            f'вес груза: {self.weight_cargo}, '
            f'время доставки: {self.time_delivery}, '
            f'название задачи: {self.task_name}, '
        )


class LogisticsMachine(Delivery, ServiceTols, AlgorithmsForeInstanceClasses, ):
    """
        Система управления поставками.
    """

    def __init__(self):
        super().__init__()
        # Основное хранилище данных. Все задачи по доставке добавляются в этот список и обрабатываются из него.
        self.delivery_list: list[Delivery] = []

    # --------------------------------- Вспомогательные методы:
    def _check_last_id_value(self) -> int:
        """
            Метод проверки delivery_id при добавлении новой таски. Позволяет исключить дублирования айди,
            что соответствует "нормальному" принципу хранения данных в базах данных.

            :rtype int.
            :return delivery_id (0 - случае пустого списка задач или айди последней задачи).
        """

        # Если пустой список задач по доставке, присваиваем "delivery_id" = 1:
        if self.is_empty_array(self.delivery_list):
            last_id = 0

        # Если не пустой, берем "delivery_id" последней таски на доставку:
        else:
            last_id = self.delivery_list[-1].delivery_id

        return last_id

    def _get_new_delivery_id_value(self) -> int:
        """
            Метод автоматически предоставляет delivery_id для новой таски при ее добавлении в список на доставку.
            Позволяет исключить дублирования айди, что соответствует "нормальному" принципу хранения данных.

            :rtype int.
            :return delivery_id (1 - случае пустого списка задач или + 1 к айди последней задачи).
        """

        return 1 + self._check_last_id_value()


    # --------------------------------- Основные методы:
    def add_delivery_task(
            self, _from_point, _to_point, _weight_cargo, _time_delivery, _task_name
    ) -> None:
        """
            Метод добавления задачи на доставку (Task). Автоматически определяет айди для новой задачи.

            :param _from_point: Пункт отправления.
            :param _to_point: Пункт назначения.
            :param _weight_cargo: Вес груза.
            :param _time_delivery: Время доставки.
            :param _task_name: Название задачи.

            :note delivery_id: Id доставки (+1 к последнему id).

            :return: None
        """

        delivery_inst = Delivery(
            delivery_id=self._get_new_delivery_id_value,
            from_point=_from_point,
            to_point=_to_point,
            weight_cargo=_weight_cargo,
            time_delivery=_time_delivery,
            task_name=_task_name
        )

        self.delivery_list.append(delivery_inst)


    def remove_delivery_task(self, attribute_name, search_element):
        """
             Метод удаления задачи на доставку.

            :param search_element:
            :param attribute_name:
            :return:
        """

        index_elem = self._searcher(
            self.delivery_list, search_element,  attribute_name, 'binary'
        )

        # Удаление из общего хранилища данных по индексу:
        self.delivery_list.pop(index_elem)

        # Удаление из стека и очереди по индексу:
        pass


    # ------------------------------------------------ Сортировки:
    def sort_delivery_list_by_weight_cargo(self):
        """
             Метод (экземпляра класса) сортировки списка поставок по весу груза.
             Метод сортировки: слиянием.
        """

        # sorted_list
        return self._merge_sort(self.delivery_list, 'weight_cargo')


    def sort_delivery_list_by_time_delivery(self):
        """
             Метод (экземпляра класса) сортировки списка поставок по времени доставки.
             Метод сортировки: быстрая.
        """

        # sorted_list
        return self._quick_sort(self.delivery_list, 'time_delivery')


    def sort_delivery_list_by_delivery_id(self):
        """
             Метод (экземпляра класса) сортировки списка поставок по номеру доставки.
             Метод сортировки: пирамидальная.
        """

        # sorted_list
        return self._heap_sort(self.delivery_list, 'delivery_id')

    # ------------------------------------------------ Поиск:
    def search_delivery_elem_by_delivery_id(self, _delivery_id: int):
        """
             Метод (экземпляра класса) поиска доставки по номеру.
             Метод поиска: линейный.
        """

        self._validator(_delivery_id, int)

        # sorted_list
        return self._searcher(self.delivery_list, _delivery_id, 'delivery_id')

    def search_delivery_elem_by_time_delivery(self, _time_delivery: int):
        """
             Метод (экземпляра класса) поиска доставки по времени доставки.
             Метод поиска: бинарный.
        """

        self._validator(_time_delivery, int)

        # sorted_list
        return self._searcher(
            self.delivery_list, _time_delivery, 'time_delivery', 'binary'
        )




    # def process_urgent_requests(self):
    #     # Обработка срочных запросов через стек
    #     stack = deque(self.delivery_list)
    #     while stack:
    #         delivery = stack.pop()
    #         # Обработка доставки
    #
    # def process_normal_requests(self):
    #     # Обработка обычных запросов через очередь
    #     queue = deque(self.delivery_list)
    #     while queue:
    #         delivery = queue.popleft()
    #         # Обработка доставки
    #
    # def search_by_id(self, delivery_id):
    #     # Линейный поиск по ID
    #     for delivery in self.delivery_list:
    #         if delivery.id == delivery_id:
    #             return delivery
    #     return None






#      удалять
#      изменять поставки,
#      сортировать их по различным критериям,
#      обрабатывать запросы с использованием стека и очереди,
#      поиск по различным критериям.







# ----------------------------------------------------------------------------------------------------------------------

# class TaskScheduler(Delivery):
#     """
#         Класс управления очередью задач.
#     """
#
#     def __init__(self):
#         super().__init__()
#         self.queue_list = []
#         self.status_data = {1: 'Pending', 2: 'In Progress...', 3: 'Completed'}
#
#     def add_task(self, name, duration):
#         """
#             Добавляет задачу в очередь с приоритетом.
#         """
#         task = Task(name=name, duration=duration)
#         heapq.heappush(self.queue_list, task)
#
#     def del_task(self, status: bool = False, sleep_time: bool = False) -> Task:
#         """
#             Удаляет и возвращает элемент с наивысшим приоритетом.
#             :param status: Режим вывода на печать статуса.
#             :param sleep_time: Режим при котором учитывается время выполнения.
#         """
#         if not self.is_empty:
#
#             sleep_time_value = self.get_task.duration
#
#             if status:
#                 print(f'Статус: {self.status_data.get(1)}, {self.get_task.__str__}.')
#
#             if status:
#                 print(f'Статус: {self.status_data.get(2)}')
#
#             if sleep_time:
#                 time.sleep(sleep_time_value)
#
#             task: Task = heapq.heappop(self.queue_list)
#
#             if status:
#                 print(f'Статус: {self.status_data.get(3)}.')
#
#
#
#     @property
#     def get_task(self) -> Task | None:
#         """
#             Возвращает элемент с наивысшим приоритетом.
#         """
#         # print(self.is_empty)
#
#         if not self.is_empty:
#             # print(self.is_empty)
#             # first_element
#             return self.queue_list[0]
#         raise IndexError('Список пуст! Невозможно извлечь задачу.')
#
#     @property
#     def is_empty(self) -> bool:
#         """
#             Проверяет, пуста ли очередь задач.
#
#         """
#         return len(self.queue_list) == 0
#
#     @property
#     def task_count(self) -> int:
#         """Возвращает количество задач в очереди."""
#         return len(self.queue_list)
#
#     def execute_tasks(self):
#         """
#             Последовательно выполняет все задачи в очереди.
#             Каждая задача занимает определенное время (duration).
#             После выполнения задачи удаляет её из очереди.
#         """
#
#         # ----------------------------------------------------
#         if self.is_empty:
#             print('Очередь пуста! Работа метода "execute_tasks" остановлена.')  # raise ValueError
#
#         # ----------------------------------------------------
#         print(f'Запуск обработки данных очереди длинной в {self.task_count} элементов:')
#
#         while not self.is_empty:
#
#             task: Task = self.del_task(status=True, sleep_time=False)
#
#         print(f'Обработка данных очереди завершена.')
#
#     def __str__(self):
#         return (
#             f'{self.__class__.__name__}. '
#             f'Список задач: {self.queue_list}'
#         )
#
#     def __repr__(self):
#         return (
#             f'{self.__class__.__name__}. '
#             f'Список задач: {self.queue_list}'
#         )




















class Interface(LogisticsMachine):

    def __init__(self):
        super().__init__()

        # Программа должна предоставлять удобный интерфейс для взаимодействия с пользователем.
        # Должны быть реализованы функции для тестирования добавления, сортировки, поиска и обработки запросов.
        # Продемонстрируйте работу программы на примере нескольких поставок и запросов.


# class Df:
#
#     def __init__(self, a, d,):
#         self.a = a
#         self.d = d
#
# sdf_1 = Df('qeqqt',2)
# sdf_2 = Df('qeqqt' ,3)
#
# print(sdf_1.a == sdf_2.a)