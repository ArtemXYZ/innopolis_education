"""
    Модуль содержит алгоритмы сортировки по list[tuple].
"""


class SortByListTuple:
    """
        Класс содержит алгоритмы сортировки по list[tuple].
    """

    def __init__(self):
        pass

    def _quick_sort(self, tuple_list: list[tuple], key_tuple: int):
        """
            Быстрая сортировка (quick_sort).
            Принимает список кортежей и сортирует его по значению, указанному в key_tuple.
            Возвращает отсортированный список кортежей.
            Выдача списка отсортированного.
        """

        # Базовый случай: если список пуст или содержит один элемент, возвращаем его
        if len(tuple_list) <= 1:
            return tuple_list

        # Выбираем опорный элемент (pivot) как средний элемент списка
        pivot = tuple_list[len(tuple_list) // 2]

        # Разделяем список на три части:
        # left - элементы меньше опорного
        # middle - элементы равные опорному
        # right - элементы больше опорного
        left = [x for x in tuple_list if x[key_tuple] < pivot[key_tuple]]
        middle = [x for x in tuple_list if x[key_tuple] == pivot[key_tuple]]
        right = [x for x in tuple_list if x[key_tuple] > pivot[key_tuple]]

        # Рекурсивно сортируем левую и правую части и объединяем результат:
        return self._quick_sort(left, key_tuple) + middle + \
            self._quick_sort(right, key_tuple)

    def _merge_sort(self, tuple_list: list[tuple], key_tuple: int):
        """
            Сортировка слиянием (merge_sort).
            Принимает список кортежей и сортирует его по значению, указанному в key_tuple.
            Возвращает отсортированный список кортежей.
        """

        # Базовый случай: если список пуст или содержит один элемент, возвращаем его
        if len(tuple_list) <= 1:
            return tuple_list

        # Находим середину списка
        mid = len(tuple_list) // 2

        # Рекурсивно сортируем левую и правую части
        left = self._merge_sort(tuple_list[:mid], key_tuple)
        right = self._merge_sort(tuple_list[mid:], key_tuple)

        # Объединяем отсортированные части
        return self._sub_merge(left, right, key_tuple)

    @staticmethod
    def _sub_merge(left: list[tuple], right: list[tuple], key_tuple: int):
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

    def _heap_sort(self, tuple_list: list[tuple], key_tuple: int):
        """
            Пирамидальная сортировка (heap_sort).
            Принимает список кортежей и сортирует его по значению, указанному в key_tuple.
            Возвращает отсортированный список кортежей.
        """

        n = len(tuple_list)

        # Построение max-heap
        for i in range(n // 2 - 1, -1, -1):
            self._sub_heapify(tuple_list, n, i, key_tuple)

        # Извлечение элементов из кучи один за другим
        for i in range(n - 1, 0, -1):
            # Перемещаем текущий корень в конец
            tuple_list[i], tuple_list[0] = tuple_list[0], tuple_list[i]
            # Вызываем heapify на уменьшенной куче
            self._sub_heapify(tuple_list, i, 0, key_tuple)

        return tuple_list

    def _sub_heapify(self, arr: list[tuple], n: int, i: int, key_tuple: int):
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
            self._sub_heapify(arr, n, largest, key_tuple)

    def __str__(self):
        return f'{self.__class__.__name__}'

    def __repr__(self):
        return f'{self.__class__.__name__}'
