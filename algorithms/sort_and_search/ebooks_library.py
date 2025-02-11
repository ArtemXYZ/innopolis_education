"""
     example.
"""
import os
import time
# import re
from typing import TypeVar

any_types = TypeVar('any_types')  # Создаем обобщённый тип данных.


class Ebook:
    """
        Класс-представление данных о книге (электронной книге).
    """

    def __init__(
            self,
            title: str = None,
            author: str = None,
            year: int = None,

    ):
        self.title = title
        self.author = author
        self.year = year

    @property
    def count_attrs(self):
        """
            Считает количество параметров в классе, характеризующих книгу.
            Со временем характеристики могут добавляться, поэтому данный метод предназначен для точного определения
            их количества.
        """

        return len(vars(self))

    @property
    def get_ebook_data_tuple(self) -> tuple:
        """
            Возвращаем данные о книге в кортеже (обеспечиваем защиту от изменений, немутабельность).
            Кроме того, это позволит обращаться точно по индексу к требуемому типу информации,
            а для сортировки будет выведен строковый эквивалент.
        """

        return self.title, self.author, self.year

    @property
    def get_ebook_data_str(self) -> str:
        """
            Возвращаем данные сотрудника в строке.
        """
        return f'{self.title}, {self.author}, {self.year}'

    def __str__(self):
        return (
            # f'{self.__class__.__name__} '
            f'Название: {self.title}, Автор: {self.author}, Год издания: {self.year}'
        )

    def __repr__(self):
        return (
            # f'{self.__class__.__name__} '
            f'Название: {self.title}, Автор: {self.author}, Год издания: {self.year}'
        )


class Ebooks:
    """
        Класс содержит данные по книгам в виде списка.
    """

    def __init__(self):
        # Значения по умолчанию:
        self._ebooks_data_list = [
            Ebook(title='Пять травм, которые мешают быть самим собой', author='Лиз Бурбо', year=2010),
            Ebook(title='Я читаю ваши мысли', author='Лиллиан Гласс', year=2003),
            Ebook(title='Богатый папа, бедный папа', author='Роберт Кийосаки', year=1994),
            Ebook(title='Прогноз глобального потепления, сделанный 50 лет назад', author='Михаил Будыко', year=1972),
            Ebook(title='Кадавры', author='Алексей Поляринов', year=2024),
            Ebook(title='Ворон. Культурная история', author='Мишель Пастуро', year=2025),
            Ebook(title='Вагнеризм: искусство и политика в тени музыки', author='Алекс Росс', year=2025),
            Ebook(title='Блокада и кино', author='Любовь Аркус', year=2025),
            Ebook(title='История цвета', author='Мишель Пастуро', year=2023),
            Ebook(title='Тайны древнего мира', author='Сергей Кузнецов', year=2021),
        ]

        self.count_attrs_ebook = Ebook().count_attrs

    @staticmethod
    def _validator(value: any_types, *check_type: type[any]) -> any_types:
        """
            *** Функция валидации аргументов. ***
        """

        if isinstance(value, check_type):
            return value
        else:
            raise TypeError(f'Недопустимый тип данных: "{type(value).__name__}", для аргумента: "{value}".')

    @property
    def get_ebooks_raw_data(self) -> list[Ebook]:
        """
            Возвращает все имеющиеся данные сотрудников списком (list[tuple]).
        """

        return self._ebooks_data_list

    @property
    def get_ebooks_data_strs(self) -> list[str]:
        """
            Возвращает все имеющиеся данные книг списком строк (объединенные данные в строку по каждому элементу),
            (list[str]).
        """

        return [ebook.get_ebook_data_str for ebook in self._ebooks_data_list]

    @property
    def get_ebooks_data_tuples(self) -> list[tuple]:
        """
            Возвращает все имеющиеся данные по книгам списком кортежей (list[tuple]).
        """

        return [ebook.get_ebook_data_tuple for ebook in self._ebooks_data_list]

    def add_ebook(self, title: str, author: str, year: int):
        """
           Опциональный метод. Добавляет новую книгу в список всех сотрудников.
        """

        # Валидация.
        _title = self._validator(title, str)
        _author = self._validator(author, str)
        _year = self._validator(year, int)

        # Книга может быть добавлена только при наличии полных данных:
        if _title and _author and _year:

            new_ebook = Ebook(_title, _author, _year)
            self._ebooks_data_list.append(new_ebook)
        else:
            print('Книга не может быть добавлена -  заполните все обязательные параметры!')

    def __str__(self):
        return f'{self.__class__.__name__} {self.get_ebooks_raw_data}'

    def __repr__(self):
        return f'{self.__class__.__name__} {self.get_ebooks_raw_data}'


class Algorithms:
    """
        Класс содержит инструменты сортировки адаптированные под структуры и типы данных (Ebooks и Ebook).
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


class EbooksLibrary(Ebooks, Algorithms):
    """
        Класс - фасад для взаимодействия с данными (вывода, сортировки, добавления).
    """

    def __init__(self):
        super().__init__()

        # self.sort_by_title = None

    @staticmethod
    def _generator_str(arey: list[tuple]):

        return [', '.join([str(n) for n in i]) for i in arey]

    def _check_params_by_count(self, param_key: int):
        """
            Проверка валидности переданного индекса параметра (не больше, не меньше, чем есть в классе атрибутов)
            :param param_key:  Индекс в кортеже к которому обращаемся для извлечения одного из типа данных по
            книге.
        """

        if param_key >= 0:
            # Определение границ диапазона допустимого индекса:
            index_limit = self.count_attrs_ebook - 1

            # Проверка на допустимый диапазон (по количеству параметров для book):
            if param_key >= 0 and param_key <= index_limit:  # 0-2

                return param_key

            raise ValueError(
                f'Ошибка передачи индекса: недопустимый диапазон! '
                f'Получено значение: {param_key}, допустимый предел: от 0 до {index_limit}.'
            )

    # -----------------------------------------------
    def sort_books_by_title(self, service_mode=False):
        """
            Сортировка по названию книги (по алфавиту).
        """

        # Убеждаемся, что попадаем в диапазон допустимых индексов в кортеже данных по классу Бук.
        param_key_valid = self._check_params_by_count(param_key=0)

        # Получаем отсортированный кортеж:
        result_tmp = self.quick_sort(self.get_ebooks_data_tuples, param_key_valid)

        if service_mode:
            result = result_tmp
        else:
            result = self._generator_str(result_tmp)

        return result

    def sort_books_by_author(self, service_mode=False):
        """
            Сортировка по имени автора книги (по алфавиту).
        """

        # Убеждаемся, что попадаем в диапазон допустимых индексов в кортеже данных по классу Бук.
        param_key_valid = self._check_params_by_count(param_key=1)

        # Получаем отсортированный кортеж:
        result_tmp = self.merge_sort(self.get_ebooks_data_tuples, param_key_valid)

        if service_mode:
            result = result_tmp
        else:
            result = self._generator_str(result_tmp)

        return result

    def sort_books_by_year(self, service_mode=False):
        """
            Сортировка по году издания книги (по алфавиту).
        """

        # Убеждаемся, что попадаем в диапазон допустимых индексов в кортеже данных по классу Бук.
        param_key_valid = self._check_params_by_count(param_key=2)

        # Получаем отсортированный кортеж:
        result_tmp = self.heap_sort(self.get_ebooks_data_tuples, param_key_valid)

        if service_mode:
            result = result_tmp
        else:
            result = self._generator_str(result_tmp)

        return result

    # -----------------------------------------------
    def search_books_by_autor(self, param: str):
        """
            Поиск книг по заданному параметру.
            В текущей реализации или по автору, или по названию.
        """

        # 1. Сортируем массив перед поиском:
        sort_books_tuple = self.sort_books_by_author(service_mode=True)

        # 2. Поиск индекса искомого элемента:
        _index = self.get_index_element_array(sort_books_tuple, param, 1)

        if _index:
            # 3. Извлечение искомого элемента по найденному индексу:
            element = self._generator_str([sort_books_tuple[_index]])
        else:
            print(f'Искомое значение не найдено!: {_index}.')
            element = None

        return element

    def search_books_by_title(self, param: str):
        """
            Поиск книг по заданному параметру.
            В текущей реализации или по автору, или по названию.
        """

        # 1. Сортируем массив перед поиском:
        sort_books_tuple = self.sort_books_by_title(service_mode=True)

        # 2. Поиск индекса искомого элемента:
        _index = self.get_index_element_array(sort_books_tuple, param, 0)

        if _index:
            # 3. Извлечение искомого элемента по найденному индексу:
            element = self._generator_str([sort_books_tuple[_index]])
        else:
            print(f'Искомое значение не найдено!: {_index}.')
            element = None

        return element

    # -----------------------------------------------

    def del_ebook(self, title: str = None, author: str = None):
        """
           Удаляет книгу из списка книг.
        """

        # # Инициализируем переменные по умолчанию
        title_v = None
        author_v = None

        # Проверяем переданы ли аргументы для поиска:
        if title or author:

            if title:
                # Валидация.
                title_v = self._validator(title, str)

            if author:
                author_v = self._validator(author, str)

        else:
            raise TypeError(
                f'Ошибка, параметры поиска не были заданы. '
                f'Необходимо передать, хотя бы один критерий для поиска: название, автор!'
            )

        # Проходимся циклом обычным (линейный поиск) обращаясь к атрибутам:
        for index, ebook in enumerate(self._ebooks_data_list):
            array_len = len(self._ebooks_data_list)
            max_index = array_len - 1
            _title = ebook.title
            _author = ebook.author
            # _year = ebook.year

            # Проверяем, содержится ли строка в подстроке (регистронезависимо),
            # если пользователь ввел только часть значения:
            # re_title = re.search(re.escape(title_v), _title, re.IGNORECASE)
            # re_author = re.search(re.escape(author_v), _author, re.IGNORECASE)

            # Проверяем условие, когда хотя бы по одному критерию поиска найдено совпадение:
            if _title == title_v or _author == author_v:
                # if re_title or re_author:
                self._ebooks_data_list.pop(index)

                print(f'Книга {ebook.__str__()} удалена!')
                break

            if index == max_index:
                print(f'Книга не найдена, проверьте параметры поиска (название: {title}, автор: {author})!')

    # -----------------------------------------------
    def load_ebooks_from_file(self, name_file: str = 'new_books'):
        """
           Загружает список книг из текстового файла в общую библиотеку
           (добавляет в общий список книг self._ebooks_data_list).
           path_file: str = '../docs/new_books.txt'
        """

        # Валидатор:
        name_file = self._validator(name_file, str)

        name_file: str = f'{name_file}.txt'
        # Путь к текстовому файлу с данными о книгах.
        path_file: str = f'../../docs/{name_file}'

        bag_list = []
        plus_list = []
        minus_list = []

        # Проверка существования файла (если файла нет):
        if not os.path.isfile(path_file):
            raise FileNotFoundError(
                f'Ошибка открытия файла! Возможно файл не существует или путь невалидный, проверьте корректность '
                f'указанных данных: {path_file}.'
            )

        # Если путь валидный:

        # Режим работы с файлом ('r' - чтение, 'w' - запись).
        with open(path_file, 'r', encoding='utf-8') as file:

            # Перебираем строки в текстовом файле:
            for index, line in enumerate(file, start=1):

                # Пропуск, если строка пустая (исключаем ошибку):
                if not line.strip():
                    continue

                # Разделяем строку по символу ';'
                book_data = line.strip().split(';')

                if len(book_data) == 3:  # Проверяем, что строка содержит все три поля

                    title, author, year = book_data

                    # Пробуем преобразовать год в число
                    try:
                        year = int(year.strip())
                        self.add_ebook(title=title.strip(), author=author.strip(), year=year)
                        plus_list.append(index)
                    except ValueError:
                        minus_list.append(index)
                        bag_list.append(book_data)
                        print(f"Ошибка: год '{year}' в строке {index} не является числом.")

                    # Создаем объект Ebook и добавляем его в список
                    self.add_ebook(title=title.strip(), author=author.strip(), year=year)

                    plus_list.append(index)

                else:
                    minus_list.append(index)
                    bag_list.append(book_data)

            print(
                f'Обработка файла завершена! Обработано книг - {index}, '
                f'из них: загружено - {plus_list[-1] if plus_list else 0}, '
                f'исключены из выборки по причине неполных данных - {minus_list[-1] if minus_list else 0}.\n'
                f' Проблемные данные: {bag_list}.'
            )

    def save_ebooks_in_file(self, name_file: str = 'saved_books'):
        """
           Сохраняет список книг библиотеки в текстовый файл.
        """

        # Валидатор:
        name_file = self._validator(name_file, str)

        name_file: str = f'{name_file}.txt'
        path_file: str = f'../../docs/{name_file}'

        # Проверка существования файла (если файл уже существует):
        if os.path.isfile(path_file):
            raise FileNotFoundError(
                f'Ошибка создания файла! Файл с таким именем уже существует, укажите другое имя.'
            )

        ebooks_data_list = self.get_ebooks_data_strs

        # Режим работы с файлом ('r' - чтение, 'w' - запись).
        with open(path_file, 'w', encoding='utf-8') as file:
            # Сохраняем в колонку все записи (каждая книга на новой строке):
            file.write('\n'.join(ebooks_data_list))

        print(f"Файл '{path_file}' успешно создан и данные записаны.")


class Interface(EbooksLibrary):
    """
        Инструмент взаимодействия с пользователем.
    """

    def __init__(self):
        super().__init__()
        # self.power = False
        # self.ebooks =

    def power(self):
        # Приветствие и список команд (отображается один раз при запуске)
        print(
            f'Добро пожаловать в систему управления "EbooksLibrary"!\n\n'
            f'Выберите действие:\n'
            f'1. Показать все книги\n'
            f'2. Сортировать книги по названию\n'
            f'3. Сортировать книги по автору\n'
            f'4. Сортировать книги по году издания\n'
            f'5. Найти книгу по названию\n'
            f'6. Найти книгу по автору\n'
            f'7. Добавить книгу\n'
            f'8. Удалить книгу\n'
            f'9. Сохранить книги в файл.\n'
            f'9. Выйти\n'
        )

        while True:

            input_value: int = input('Введите команду: ')

            if input_value == '1':
                print(self.get_ebooks_data_strs)

            elif input_value == '2':
                print(self.sort_books_by_title())

            elif input_value == '3':
                print(self.sort_books_by_author())

            elif input_value == '4':
                print(self.sort_books_by_year())

            elif input_value == '5':

                input_value: str = input('Введите название книги: ')

                print(self.search_books_by_title(input_value))

            elif input_value == '6':

                input_value: str = input('Введите название книги: ')

                print(self.search_books_by_autor(input_value))

            elif input_value == '7':
                while True:  # Вложенный цикл для подменю
                    print(
                        f'Вы находитесь в разделе загрузки новых книг.\n\n'
                        f'Если вы можете загрузить список книг из файла или ввести данные вручную.\n'
                        f'Выберите действие:\n'
                        f'1. Ввести данные вручную.\n'
                        f'2. Загрузить список книг из файла.\n'
                        f'3. Выйти в главное меню.\n'
                    )

                    # Запрос действия от пользователя:
                    sub_input_value: int = input('Введите команду: ')

                    # Обработка команд подменю
                    if sub_input_value == '1':
                        print('Вы выбрали ввод данных вручную.')
                        title: str = input('Введите название книги: ')
                        author: str = input('Введите автора книги: ')
                        # Ввод года с проверкой
                        while True:  # Цикл для повторного ввода года
                            try:
                                year: int = int(input('Введите год издания книги: '))
                                break
                            except ValueError:
                                print('Ошибка: Введено не число. Пожалуйста, введите числовое значение.')

                        self.add_ebook(title, author, year)
                        print('Книга успешно сохранена!')
                        continue

                    elif sub_input_value == '2':
                        while True:
                            print('Вы выбрали загрузку списка книг из файла (из папки docs проекта).')
                            file: str = input(
                                f'Введите имя файла без расширения или нажмите интер - '
                                f'это применит значение по умолчанию: '
                            )

                            if file:  # Проверяем, что строка не пустая
                                try:
                                    self.load_ebooks_from_file(file)
                                    break
                                except Exception as r:
                                    print(f'Операция не выполнена! {r}')
                                    continue
                            else:
                                self.load_ebooks_from_file()
                            break

                    elif sub_input_value == '3':
                        print('Возврат в главное меню.')
                        break  # Выход из вложенного цикла и возврат в главное меню
                    else:
                        print('Неверная команда. Пожалуйста, выберите 1, 2 или 3.')

            elif input_value == '8':
                while True:
                    print(f'Вы в меню удаления книг.\n'
                          f'Если вы хотите удалить книгу, введите хотя бы один параметр поиска.')
                    title: str = input('Введите название книги или нажмите "enter" (если необходим поиск по автору): ')
                    author: str = input('Введите автора книги: ')

                    if title or author:

                        self.del_ebook(title, author)
                        print('Книга успешно удалена!')
                        break
                    else:
                        continue
                continue

            elif input_value == '9':
                while True:
                    print(f'Вы в меню сохранения книг в текстовый файл.\n'
                          f'Если вы хотите сохранить список книгу, введите имя файла или нажмите "enter" '
                          f'- это применит имя файла по умолчанию.'
                          f'Однако, при повторном действии уже необходимо будет вводить новое имя иначе ошибка.')

                    file: str = input('Введите имя файла: ')

                    try:
                        self.save_ebooks_in_file(file)
                        print('Книги успешно сохранены!')
                        break
                    except Exception as r:
                        print(f'Ошибка: {r}')

            elif input_value == '10':
                print('Выход из системы.')
                break

            else:
                print('Неверный ввод. Пожалуйста, выберите действие от 1 до 10.')

            time.sleep(1)

    def __str__(self):
        return (f'{self.__class__.__name__}')

    def __repr__(self):
        return (f'{self.__class__.__name__}')


run = Interface()
run.power()



# Добро пожаловать в систему управления "EbooksLibrary"!
#
# Выберите действие:
# 1. Показать все книги
# 2. Сортировать книги по названию
# 3. Сортировать книги по автору
# 4. Сортировать книги по году издания
# 5. Найти книгу по названию
# 6. Найти книгу по автору
# 7. Добавить книгу
# 8. Удалить книгу
# 9. Сохранить книги в файл.
# 9. Выйти
#
# Введите команду: 1
# ['Пять травм, которые мешают быть самим собой, Лиз Бурбо, 2010', 'Я читаю ваши мысли, Лиллиан Гласс, 2003', 'Богатый папа, бедный папа, Роберт Кийосаки, 1994', 'Прогноз глобального потепления, сделанный 50 лет назад, Михаил Будыко, 1972', 'Кадавры, Алексей Поляринов, 2024', 'Ворон. Культурная история, Мишель Пастуро, 2025', 'Вагнеризм: искусство и политика в тени музыки, Алекс Росс, 2025', 'Блокада и кино, Любовь Аркус, 2025', 'История цвета, Мишель Пастуро, 2023', 'Тайны древнего мира, Сергей Кузнецов, 2021']
# Введите команду: 2
# ['Блокада и кино, Любовь Аркус, 2025', 'Богатый папа, бедный папа, Роберт Кийосаки, 1994', 'Вагнеризм: искусство и политика в тени музыки, Алекс Росс, 2025', 'Ворон. Культурная история, Мишель Пастуро, 2025', 'История цвета, Мишель Пастуро, 2023', 'Кадавры, Алексей Поляринов, 2024', 'Прогноз глобального потепления, сделанный 50 лет назад, Михаил Будыко, 1972', 'Пять травм, которые мешают быть самим собой, Лиз Бурбо, 2010', 'Тайны древнего мира, Сергей Кузнецов, 2021', 'Я читаю ваши мысли, Лиллиан Гласс, 2003']
# Введите команду: 3
# ['Вагнеризм: искусство и политика в тени музыки, Алекс Росс, 2025', 'Кадавры, Алексей Поляринов, 2024', 'Пять травм, которые мешают быть самим собой, Лиз Бурбо, 2010', 'Я читаю ваши мысли, Лиллиан Гласс, 2003', 'Блокада и кино, Любовь Аркус, 2025', 'Прогноз глобального потепления, сделанный 50 лет назад, Михаил Будыко, 1972', 'История цвета, Мишель Пастуро, 2023', 'Ворон. Культурная история, Мишель Пастуро, 2025', 'Богатый папа, бедный папа, Роберт Кийосаки, 1994', 'Тайны древнего мира, Сергей Кузнецов, 2021']
# Введите команду: 4
# ['Прогноз глобального потепления, сделанный 50 лет назад, Михаил Будыко, 1972', 'Богатый папа, бедный папа, Роберт Кийосаки, 1994', 'Я читаю ваши мысли, Лиллиан Гласс, 2003', 'Пять травм, которые мешают быть самим собой, Лиз Бурбо, 2010', 'Тайны древнего мира, Сергей Кузнецов, 2021', 'История цвета, Мишель Пастуро, 2023', 'Кадавры, Алексей Поляринов, 2024', 'Вагнеризм: искусство и политика в тени музыки, Алекс Росс, 2025', 'Ворон. Культурная история, Мишель Пастуро, 2025', 'Блокада и кино, Любовь Аркус, 2025']
# Введите команду: 5
# Введите название книги: Богатый папа, бедный папа
# ['Богатый папа, бедный папа, Роберт Кийосаки, 1994']
# Введите команду: 6
# Введите название книги: Роберт Кийосаки
# ['Богатый папа, бедный папа, Роберт Кийосаки, 1994']

# Введите команду: 7
# Вы находитесь в разделе загрузки новых книг.
#
# Если вы можете загрузить список книг из файла или ввести данные вручную.
# Выберите действие:
# 1. Ввести данные вручную.
# 2. Загрузить список книг из файла.
# 3. Выйти в главное меню.
#
# Введите команду: 1
# Вы выбрали ввод данных вручную.
# Введите название книги: test
# Введите автора книги: artem
# Введите год издания книги: 1989
# Книга успешно сохранена!
# Вы находитесь в разделе загрузки новых книг.
#
# Если вы можете загрузить список книг из файла или ввести данные вручную.
# Выберите действие:
# 1. Ввести данные вручную.
# 2. Загрузить список книг из файла.
# 3. Выйти в главное меню.
#
# Введите команду: 2
# Вы выбрали загрузку списка книг из файла (из папки docs проекта).
# Введите имя файла без расширения или нажмите интер - это применит значение по умолчанию:
# Обработка файла завершена! Обработано книг - 10, из них: загружено - 10, исключены из выборки по причине неполных данных - 0.
#  Проблемные данные: [].
# Вы находитесь в разделе загрузки новых книг.
#
# Если вы можете загрузить список книг из файла или ввести данные вручную.
# Выберите действие:
# 1. Ввести данные вручную.
# 2. Загрузить список книг из файла.
# 3. Выйти в главное меню.
#
# Введите команду: 3
# Возврат в главное меню.
# Введите команду: 8
# Вы в меню удаления книг.
# Если вы хотите удалить книгу, введите хотя бы один параметр поиска.
# Введите название книги или нажмите "enter" (если необходим поиск по автору): test
# Введите автора книги:
# Книга Название: test, Автор: artem, Год издания: 1989 удалена!
# Книга успешно удалена!
# Введите команду:
# ======================================================================================================================

# e = Ebook()
# print(e.count_attrs)

# ebooks = EbooksLibrary()
# print(ebooks.get_ebooks_data_strs)
# ebooks.save_ebooks_in_file()
# e_library.del_ebook(title='Пять травм, которые мешают быть самим ')

# # print(e_library.count_attrs_ebook)
# print(e_library._check_params_by_count(5))

# print(e_library.sort_employees_by_salary)

# print(e_library.sort_employees_by_ege)

# print(e_library.sort_employees_by_patronymic)

#  print(e_library.sort_employees_by_name)

# print(e_library.sort_employees_by_family_name)
