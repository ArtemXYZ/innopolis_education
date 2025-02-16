"""
    Учебная реализация программы для анализа и обработки данных логистической компании.
    Программа хранит данные о поставках, сортировать их по различным критериям, обрабатывать запросы на получение
    информации и оптимизирует процесс обработки с помощью различных алгоритмов.
"""


import heapq
import time




class Stack:
    """
        Класс-представление стека.
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("удаление из пустого стека")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("получение из пустого стека")

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None  # Начало списка

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


class CircularStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
            self.top.next = self.top  # Указывает сам на себя, замыкая список
        else:
            new_node.next = self.top.next  # Новый узел указывает на первый узел
            self.top.next = new_node  # Последний узел (старый top) указывает на новый узел
            self.top = new_node  # Обновляем top

    def pop(self):
        if self.is_empty():
            raise IndexError("удаление из пустого стека")
        popped_node = self.top.next  # Первый узел (top.next) будет удален
        if self.top == self.top.next:
            # Если в списке только один элемент
            self.top = None
        else:
            self.top.next = popped_node.next  # Последний узел указывает на следующий после удаленного
        return popped_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("получение из пустого стека")
        return self.top.next.data  # Возвращаем данные первого узла


class Delivery:
    """
        Класс-представление данных о доставке.
        Используем магические методы для определения сравнения их по атрибутам.
    """

    def __init__(
            self,
            delivery_id,
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
            f'{self.__class__.__name__} '
            f'id доставки: {self.delivery_id}, '
            f'пункт отправления: {self.from_point}, '
            f'пункт назначения: {self.to_point},'
            f'вес груза: {self.weight_cargo}, '
            f'время доставки: {self.time_delivery}, '
            f'название задачи: {self.task_name}, '
        )

    def __repr__(self):
        return (
            f'{self.__class__.__name__} '
            f'id доставки: {self.delivery_id}, '
            f'пункт отправления: {self.from_point}, '
            f'пункт назначения: {self.to_point},'
            f'вес груза: {self.weight_cargo}, '
            f'время доставки: {self.time_delivery}, '
            f'название задачи: {self.task_name}, '
        )





class TaskScheduler(Delivery):
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


class LogisticsMachine(Algorithms, ):
    """
        Система управления поставками.
    """

    def __init__(self):
        super().__init__()


class Interface(LogisticsMachine):

    def __init__(self):
        super().__init__()

        # Программа должна предоставлять удобный интерфейс для взаимодействия с пользователем.
        # Должны быть реализованы функции для тестирования добавления, сортировки, поиска и обработки запросов.
        # Продемонстрируйте работу программы на примере нескольких поставок и запросов.