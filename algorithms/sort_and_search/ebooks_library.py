"""
    Shell_sorting example.
"""


class Employee:
    """
        Класс-представление данных сотрудника.
        Является каркасом-формирователем структуры данных для отдельного сотрудника.
    """

    def __init__(
            self,
            family_name: str = None,
            name: str = None,
            patronymic: str = None,
            ege: int = None,
            salary: int = None
    ):
        self.family_name = family_name
        self.name = name
        self.patronymic = patronymic
        self.ege = ege
        self.salary = salary

    @property
    def count_attrs(self):
        """
            Считает количество параметров в классе, характеризующих сотрудника.
            Со временем характеристики могут добавляться, поэтому данный метод предназначен для точного определения
            их количества.
        """

        return len(vars(self))

    @property
    def get_employee_data_tuple(self) -> tuple:
        """
            Возвращаем данные сотрудника в кортеже (обеспечиваем защиту от изменений, немутабельность).
            Кроме того, это позволит обращаться точно по индексу к требуемому типу информации (фамилия или возраст),
            а для сортировки будет выведен строковый эквивалент.
        """

        return self.family_name, self.name, self.patronymic, self.ege, self.salary

    @property
    def get_employee_data_str(self) -> str:
        """
            Возвращаем данные сотрудника в кортеже (обеспечиваем защиту от изменений, немутабельность).
            Кроме того, это позволит обращаться точно по индексу к требуемому типу информации (фамилия или возраст),
            а для сортировки будет выведен строковый эквивалент.
        """
        return f'{self.family_name}, {self.name}, {self.patronymic}, {self.ege}, {self.salary}'

    def __str__(self):
        return (
            # f'{self.__class__.__name__} '
            f'Фамилия: {self.family_name}, Имя: {self.name}, '
            f'Отчество: {self.patronymic}, Возраст: {self.ege}, '
            f'Зарплата: {self.salary}'
        )

    def __repr__(self):
        return (
            # f'{self.__class__.__name__} '
            f'Фамилия: {self.family_name}, Имя: {self.name}, '
            f'Отчество: {self.patronymic}, Возраст: {self.ege}, '
            f'Зарплата: {self.salary}'
        )


class Employees:
    """
        Класс содержит данные по всем сотрудникам в виде списка.
    """

    def __init__(self):
        # Значения по умолчанию:
        self._employees_data_list = [
            Employee(family_name='Перов', name='Александр', patronymic='Семенович', ege=33, salary=150),
            Employee(family_name='Иванов', name='Артур', patronymic='Александрович', ege=43, salary=250),
            Employee(family_name='Сидоров', name='Дмитрий', patronymic='Валерьянович', ege=25, salary=75),
            Employee(family_name='Прохоров', name='Виталий', patronymic='Геннадиевич', ege=23, salary=50),
        ]
        self.count_attrs_employee = Employee.count_attrs

    @property
    def get_employees_raw_data(self) -> list[Employee]:
        """
            Возвращает все имеющиеся данные сотрудников списком (list[tuple]).
        """
        return self._employees_data_list

    @property
    def get_employees_data_strs(self) -> list[str]:
        """
            Возвращает все имеющиеся данные сотрудников списком строк (объединенные данные сотрудника в строку)
            (list[str]).
        """

        return [employee.get_employee_data_str for employee in self._employees_data_list]

    @property
    def get_employees_data_tuples(self) -> list[tuple]:
        """
            Возвращает все имеющиеся данные сотрудников списком кортежей (list[tuple]).
        """

        return [employee.get_employee_data_tuple for employee in self._employees_data_list]

    def add_employee(self, family_name: str, name: str, patronymic: str, ege: int, salary: int):
        """
            Опциональный метод. Добавляет нового сотрудника в список всех сотрудников.
        """

        # Валидацию опускаем.

        new_employee = Employee(family_name, name, patronymic, ege, salary)
        self._employees_data_list.append(new_employee)

    def __str__(self):
        return f'{self.__class__.__name__} {self.get_employees_raw_data}'

    def __repr__(self):
        return f'{self.__class__.__name__} {self.get_employees_raw_data}'


class ToolsSort:
    """
        Класс содержит инструменты сортировки адаптированные под структуры и типы данных (Employees и Employee).

        Заметка.  фамилия и имя нужно сортировать по алфавиту.
        картеж в послед
    """

    def __init__(self):
        pass

    @staticmethod
    def shell_sorting_dict(employees_tuple_list: list[tuple], key_tuple: int):
        """
            Должен принимать картеж и обеспечивать сортировку по его ключам. Выдача списка отсортированного.
        """

        # Определяем длину массива:
        n = len(employees_tuple_list)

        # Определяем шаг:
        gap = n // 2


        while gap > 0:
            # Перебираем индексы элементов в шаге:
            for i in range(gap, n):

                # Обращаемся в списке к кортежу по индексу и его элементу (по ключу) \
                # фактически сравниваем значение из кортежа, а не весь кортеж:
                temp_1 = employees_tuple_list[i][key_tuple]      # [key_tuple]
                temp_2 = employees_tuple_list[i]
                j = i

                # Аналогично вытягиваем значение из картежа по ключу:
                while j >= gap and employees_tuple_list[j - gap][key_tuple]  > temp_1:
                    employees_tuple_list[j] = employees_tuple_list[j - gap]

                    j -= gap

                employees_tuple_list[j] = temp_2
            gap //= 2

        return employees_tuple_list


class Company(Employees, ToolsSort):
    """
        Класс - фасад для взаимодействия с данными (вывода, сортировки, добавление опускаю).
    """

    def __init__(self):
        super().__init__()
        # self.employees_data_tuples = self.get_employees_data_tuples
        # self.employees_data_tuples = self.get_employees_data_strs

        # self.employees = Employees()
        # self.tools = SortingTools

    @staticmethod
    def _generator_str(arey: list[tuple]):

        return [', '.join([str(n) for n in i]) for i in arey]

    def _sort_employees_by_params(self, param_key: int):
        """
            Сортировка по заданному параметру (ядро, основная логика хранится в этом методе).
            :param param_key:  Индекс в кортеже к которому обращаемся для извлечения одного из типа данных по
            пользователю (Имя или фамилия ...).

        """

        # Валидацию опускаем что бы не усложнять.
        # Проверяем, что только int

        if param_key >= 0:

            # Проверка на допустимый диапазон (по количеству параметров для сотрудника):
            if param_key >= 0 or param_key <= self.count_attrs_employee - 5:  # 0-4

                return self.shell_sorting_dict(self.get_employees_data_tuples, param_key)

    @property
    def sort_employees_by_family_name(self):
        """
            Сортировка по фамилии (по алфавиту).
        """

        result_tmp = self._sort_employees_by_params(param_key=0)
        return self._generator_str(result_tmp)

    @property
    def sort_employees_by_name(self, ):
        """
            Сортировка по имени (по алфавиту).
        """

        result_tmp = self._sort_employees_by_params(param_key=1)
        return self._generator_str(result_tmp)

    @property
    def sort_employees_by_patronymic(self):
        """
            Сортировка по отчеству (по алфавиту).
        """

        result_tmp = self._sort_employees_by_params(param_key=2)
        return self._generator_str(result_tmp)

    @property
    def sort_employees_by_ege(self):
        """
            Сортировка по возрасту.

        """
        result_tmp = self._sort_employees_by_params(param_key=3)
        return self._generator_str(result_tmp)


    @property
    def sort_employees_by_salary(self):
        """
            Сортировка по зарплате.
        """

        result_tmp = self._sort_employees_by_params(param_key=4)
        return self._generator_str(result_tmp)


# ['Прохоров, Виталий, Геннадиевич, 23, 50', 'Сидоров, Дмитрий, Валерьянович, 25, 75', 'Перов, Александр, Семенович, 33, 150', 'Иванов, Артур, Александрович, 43, 250']
# print(company.sort_employees_by_salary)

# ['Прохоров, Виталий, Геннадиевич, 23, 50', 'Сидоров, Дмитрий, Валерьянович, 25, 75', 'Перов, Александр, Семенович, 33, 150', 'Иванов, Артур, Александрович, 43, 250']
# print(company.sort_employees_by_ege)

# ['Иванов, Артур, Александрович, 43, 250', 'Сидоров, Дмитрий, Валерьянович, 25, 75', 'Прохоров, Виталий, Геннадиевич, 23, 50', 'Перов, Александр, Семенович, 33, 150']
# print(company.sort_employees_by_patronymic)

# ['Перов, Александр, Семенович, 33, 150', 'Иванов, Артур, Александрович, 43, 250', 'Прохоров, Виталий, Геннадиевич, 23, 50', 'Сидоров, Дмитрий, Валерьянович, 25, 75']
# print(company.sort_employees_by_name)

# ['Иванов, Артур, Александрович, 43, 250', 'Перов, Александр, Семенович, 33, 150', 'Прохоров, Виталий, Геннадиевич, 23, 50', 'Сидоров, Дмитрий, Валерьянович, 25, 75']
# print(company.sort_employees_by_family_name)