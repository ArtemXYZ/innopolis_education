"""
    Учебная реализация программы для анализа и обработки данных логистической компании.
    Программа хранит данные о поставках, сортировать их по различным критериям, обрабатывать запросы на получение
    информации и оптимизирует процесс обработки с помощью различных алгоритмов.
"""

from dataclasses import dataclass


from src.algorithms_core.main import AlgorithmsForeInstanceClasses
from src.services.tools import ServiceTols

from src.queues.queues_by_instance_classes import QueueByInstanceClasses
from src.stacks.stack_by_instance_classes import StackByInstanceClasses


# ----------------------------------------------------------------------------------------------------------------------
@dataclass(order=True)
class Delivery(ServiceTols):
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
            delivery_id: int = None,  # id доставки.
            from_point: str = None,  # Пункт отправления.
            to_point: str = None,  # Пункт назначения.
            weight_cargo: int | float = None,  # Вес груза.
            time_delivery: int = None,  # Время доставки.
            task_name: str = None,  # Название задачи:
            priority: int = None,  # Приоритетность задачи:

    ) -> None:
        super().__init__()
        self.delivery_id = delivery_id if self._validator(delivery_id, int | None) else ...
        self.from_point = from_point if self._validator(from_point, str | None) else ...
        self.to_point = to_point if self._validator(to_point, str | None) else ...
        self.weight_cargo = weight_cargo if self._validator(weight_cargo, float | int | None) else ...
        self.time_delivery = time_delivery if self._validator(time_delivery, int | None) else ...
        self.task_name = task_name if self._validator(task_name, str | None) else ...
        self.priority = priority if self._validator(priority, int | None) else ...

    @property
    def _count_attrs(self):
        """
            Считает количество параметров в классе, характеризующих книгу.
            Со временем характеристики могут добавляться, поэтому данный метод предназначен для точного определения
            их количества.
        """

        return len(vars(self))

    def __str__(self):
        return (
            # f'{self.__class__.__name__}: '
            f'id доставки: {self.delivery_id}, '
            f'пункт отправления: {self.from_point}, '
            f'пункт назначения: {self.to_point}, '
            f'вес груза: {self.weight_cargo}, '
            f'время доставки: {self.time_delivery}, '
            f'название задачи: {self.task_name}, '
            f'приоритет задачи: {self.priority}.'
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
            f'приоритет задачи: {self.priority}.'
        )


class LogisticsMachine(Delivery, ServiceTols, AlgorithmsForeInstanceClasses):
    """
        Система управления поставками.
    """

    def __init__(self):
        super().__init__()
        # Основное хранилище данных. Все задачи по доставке добавляются в этот список и обрабатываются из него.
        self.delivery_list: list[Delivery] = []
        self.normal_queue = QueueByInstanceClasses()
        self.stack = StackByInstanceClasses()

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
            self,
            _from_point: str,
            _to_point: str,
            _weight_cargo: int | float,
            _time_delivery: int,
            _task_name: str,
            _priority: int
    ) -> None:
        """
            Метод добавления задачи на доставку (Task). Автоматически определяет айди для новой задачи.

            :param _priority:
            :param _from_point: Пункт отправления.
            :param _to_point: Пункт назначения.
            :param _weight_cargo: Вес груза.
            :param _time_delivery: Время доставки.
            :param _task_name: Название задачи.

            :note delivery_id: Id доставки (+1 к последнему id).

            :return: None
        """

        delivery_inst = Delivery(
            delivery_id=self._get_new_delivery_id_value(),
            from_point=_from_point,
            to_point=_to_point,
            weight_cargo=_weight_cargo,
            time_delivery=_time_delivery,
            task_name=_task_name,
            priority=_priority
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
            self.delivery_list, search_element, attribute_name, 'binary'
        )

        # Удаление из общего хранилища данных по индексу:
        self.delivery_list.pop(index_elem)

        # Удаление из стека и очереди по индексу:
        # pass

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

    def process_stack(self):
        """
            Реализация работы очереди (FIFO) при обработке списка на доставку.
            После выполнения задачи удаляет её из очереди.
        """

        self.stack.set_stack_array(self.delivery_list)

        # ----------------------------------------------------
        if not self.stack.stack_obj:
            print('Стек пустой! Работа метода "process_stack" остановлена.')  # raise ValueError

        # ----------------------------------------------------
        print(f'Запуск обработки данных стека длинной в {self.normal_queue.size_queue()} элементов:')

        while not self.is_empty_array(self.stack.stack_obj):
            heappop_obj = self.normal_queue.del_in_queue()
            print(f'Отработана задача: {heappop_obj}')

        print(f'Обработка данных очереди завершена.')

    def process_normal_queue(self):
        """
            Реализация работы очереди (FIFO) при обработке списка на доставку.
            После выполнения задачи удаляет её из очереди.
        """

        self.normal_queue.set_queue_array(self.delivery_list)
        normal_queue_obj = self.normal_queue.queue_obj

        # ----------------------------------------------------
        if not normal_queue_obj:
            print('Очередь пуста! Работа метода "process_normal_queue" остановлена.')  # raise ValueError

        # ----------------------------------------------------
        print(f'Запуск обработки данных очереди длинной в {self.normal_queue.size_queue()} элементов:')

        while not self.is_empty_array(normal_queue_obj):
            popleft_obj = self.normal_queue.del_in_queue()
            print(f'Отработана задача: {popleft_obj}')

        print(f'Обработка данных очереди завершена.')







#
# test = LogisticsMachine()
# test.add_delivery_task('Орск', 'Москва', 123.21, 45, 'Стиральная машинка', 23)
# test.process_normal_queue()

