"""
    Учебная реализация программы для анализа и обработки данных логистической компании.
    Программа хранит данные о поставках, сортировать их по различным критериям, обрабатывать запросы на получение
    информации и оптимизирует процесс обработки с помощью различных алгоритмов.
"""


import heapq
import time

class ServiceTols:
    """
        Класс содержит данные по книгам в виде списка.
    """

    def __init__(self):
       ...

    @staticmethod
    def _validator(value: any, *check_type: type[any]) -> None:
        """
            *** Функция валидации аргументов. ***
        """

        if not isinstance(value, check_type):
            raise TypeError(f'Недопустимый тип данных: "{type(value).__name__}", для аргумента: "{value}".')


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

    # def __lt__(self, other):
    #     """
    #         Определение сравнения объектов: "если меньше".
    #     """
    #     return self.duration < other.duration
    #
    # def __gt__(self, other):
    #     """
    #         Определение сравнения объектов: "если больше".
    #     """
    #     return self.duration > other.duration
    #
    # def __eq__(self, other):
    #     """
    #         Определение сравнения объектов: "если равно".
    #     """
    #     return self.duration == other.duration

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


class Algorithms:
    """
        Класс содержит инструменты сортировки.
    """

    def __init__(self):
        pass

    def quick_sort(self, ebooks_tuple_list: list[tuple], key_tuple: int):
        """
            Быстрая сортировка (quick_sort).
            Принимает список кортежей и сортирует его по значению, указанному в key_tuple.
            Возвращает отсортированный список кортежей.
            Выдача списка отсортированного.
        """

        # Базовый случай: если список пуст или содержит один элемент, возвращаем его
        if len(ebooks_tuple_list) <= 1:
            return ebooks_tuple_list

        # Выбираем опорный элемент (pivot) как средний элемент списка
        pivot = ebooks_tuple_list[len(ebooks_tuple_list) // 2]

        # Разделяем список на три части:
        # left - элементы меньше опорного
        # middle - элементы равные опорному
        # right - элементы больше опорного
        left = [x for x in ebooks_tuple_list if x[key_tuple] < pivot[key_tuple]]
        middle = [x for x in ebooks_tuple_list if x[key_tuple] == pivot[key_tuple]]
        right = [x for x in ebooks_tuple_list if x[key_tuple] > pivot[key_tuple]]

        # Рекурсивно сортируем левую и правую части и объединяем результат:
        return self.quick_sort(left, key_tuple) + middle + \
            self.quick_sort(right, key_tuple)

    def merge_sort(self, ebooks_tuple_list: list[tuple], key_tuple: int):
        """
            Сортировка слиянием (merge_sort).
            Принимает список кортежей и сортирует его по значению, указанному в key_tuple.
            Возвращает отсортированный список кортежей.
        """

        # Базовый случай: если список пуст или содержит один элемент, возвращаем его
        if len(ebooks_tuple_list) <= 1:
            return ebooks_tuple_list

        # Находим середину списка
        mid = len(ebooks_tuple_list) // 2

        # Рекурсивно сортируем левую и правую части
        left = self.merge_sort(ebooks_tuple_list[:mid], key_tuple)
        right = self.merge_sort(ebooks_tuple_list[mid:], key_tuple)

        # Объединяем отсортированные части
        return self._merge(left, right, key_tuple)

    @staticmethod
    def _merge(left: list[tuple], right: list[tuple], key_tuple: int):
        """
            Вспомогательная функция для слияния двух отсортированных списков.
            Возвращает объединенный отсортированный список.
        """
        result = []
        i = j = 0

        # Слияние двух списков
        while i < len(left) and j < len(right):
            if left[i][key_tuple] < right[j][key_tuple]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Добавляем оставшиеся элементы из левого списка (если они есть)
        while i < len(left):
            result.append(left[i])
            i += 1

        # Добавляем оставшиеся элементы из правого списка (если они есть)
        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    def heap_sort(self, ebooks_tuple_list: list[tuple], key_tuple: int):
        """
            Пирамидальная сортировка (heap_sort).
            Принимает список кортежей и сортирует его по значению, указанному в key_tuple.
            Возвращает отсортированный список кортежей.
        """

        n = len(ebooks_tuple_list)

        # Построение max-heap
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(ebooks_tuple_list, n, i, key_tuple)

        # Извлечение элементов из кучи один за другим
        for i in range(n - 1, 0, -1):
            # Перемещаем текущий корень в конец
            ebooks_tuple_list[i], ebooks_tuple_list[0] = ebooks_tuple_list[0], ebooks_tuple_list[i]
            # Вызываем heapify на уменьшенной куче
            self._heapify(ebooks_tuple_list, i, 0, key_tuple)

        return ebooks_tuple_list

    def _heapify(self, arr: list[tuple], n: int, i: int, key_tuple: int):
        """
            Вспомогательная функция для построения max-heap.
            arr: список кортежей
            n: размер кучи
            i: индекс корня поддерева
            key_tuple: индекс ключа для сравнения
        """
        largest = i  # Инициализируем наибольший элемент как корень
        left = 2 * i + 1  # Левый дочерний элемент
        right = 2 * i + 2  # Правый дочерний элемент

        # Если левый дочерний элемент существует и больше корня
        if left < n and arr[left][key_tuple] > arr[largest][key_tuple]:
            largest = left

        # Если правый дочерний элемент существует и больше текущего наибольшего
        if right < n and arr[right][key_tuple] > arr[largest][key_tuple]:
            largest = right

        # Если наибольший элемент не корень
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Меняем местами
            # Рекурсивно преобразуем затронутое поддерево в max-heap
            self._heapify(arr, n, largest, key_tuple)

    @staticmethod
    def get_index_element_array(
            ebooks_tuple_list: list[tuple],
            search_element: int | str,
            key_tuple: int
    ) -> int | None:
        """
            *** Алгоритм бинарного поиска индекса заданного элемента в отсортированном массиве с пропусками. ***

            :param ebooks_tuple_list: Входной массив кортежей (присутствуют None).
            :param search_element: Значение, которое требуется проверить.
            :param key_tuple: Индекс ключа в кортеже для сравнения.
            :return: Возвращает индекс искомого элемента или None, если элемент отсутствует.
            :rtype: None | int.
        """

        # Валидация входных данных:
        if not ebooks_tuple_list:
            raise ValueError(f'Ошибка, переданный массив пуст, операция не может быть выполнена! {ebooks_tuple_list}.')

        # Определение границ:
        left, right = 0, len(ebooks_tuple_list) - 1

        # Перебор массива:
        while left <= right:
            # Индекс среднего элемента последовательности (округляет в сторону меньшего числа):
            midl_index: int = (left + right) // 2

            # Обработка пропусков:
            # Если элемент в середине равен None, ищем ближайший ненулевой элемент:
            if ebooks_tuple_list[midl_index] is None:
                low, high = midl_index - 1, midl_index + 1
                while True:
                    if low >= left and ebooks_tuple_list[low] is not None:
                        midl_index = low
                        break
                    if high <= right and ebooks_tuple_list[high] is not None:
                        midl_index = high
                        break
                    low -= 1
                    high += 1
                    if low < left and high > right:
                        return -1  # Все элементы в пределах left и right равны None

            # Основной алгоритм:
            # Проверка среднего элемента (Если сразу же совпало, возвращаем результат):
            if ebooks_tuple_list[midl_index][key_tuple] == search_element:
                return midl_index

            # Если искомый элемент больше среднего, игнорируем левую половину:
            elif ebooks_tuple_list[midl_index][key_tuple] < search_element:
                # Сдвигаем левую границу (проверили середину, теперь следующее число от средины будет начальной границей).
                left = midl_index + 1

            # Если искомый элемент меньше среднего, игнорируем правую половину:
            else:
                # Сдвигаем правую границу (проверили середину, теперь предыдущее число от средины будет конечной границей).
                right = midl_index - 1

        # Элемент не найден:
        # print(f'Ошибка, переданный элемент не найден!: {search_element}.')
        return None


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