"""
    Shell_sorting example.
"""


class Employee:
    """
        Класс-представление данных сотрудника.
        Является каркасом-формирователем структуры данных для отдельного сотрудника.
    """

    def __init__(self, family_name: str, name: str, patronymic: str, ege: int, salary: int):
        # В текущей реализации делаем все параметры обязательными для упрощения.
        self.family_name = family_name
        self.name = name
        self.patronymic = patronymic
        self.ege = ege
        self.salary = salary

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
            Employee(family_name='Перов', name='Александр', patronymic='Семенович', ege=23, salary=150),
            Employee(family_name='Иванов', name='Артур', patronymic='Александрович', ege=23, salary=250),
            Employee(family_name='Сидоров', name='Дмитрий', patronymic='Валерьянович', ege=23, salary=75),
            Employee(family_name='Прохоров', name='Виталий', patronymic='Геннадиевич', ege=23, salary=50),
        ]

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

        return [employee.get_employee_data_str for employee  in self._employees_data_list]

    @property
    def get_employees_data_tuples(self) -> list[tuple]:
        """
            Возвращает все имеющиеся данные сотрудников списком кортежей (list[tuple]).
        """

        return [employee.get_employee_data_tuple for employee  in self._employees_data_list]


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


class SortingTools:
    """
        Класс содержит инструменты сортировки адаптированные под структуры и типы данных (Employees и Employee).

        Заметка.  фамилия и имя нужно сортировать по алфавиту.
        картеж в послед
    """

    def __init__(self):
        pass


    @staticmethod
    def shell_sort(employees: type, key):
        """
            Должен принимать картеж и обеспечивать сортировку по его ключам. Выдача списка отсортированного.
        """

        n = len(employees)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = employees[i]
                j = i
                while j >= gap and key(employees[j - gap]) > key(temp):
                    employees[j] = employees[j - gap]
                    j -= gap
                employees[j] = temp
            gap //= 2


class Company(Employees):
    """
        Класс - фасад для предоставления всех итоговых данных.
    """

    def __init__(self):
        super().__init__()
        employees_data_tuples = self.get_employees_data_tuples
        employees_data_tuples = self.get_employees_data_strs

        # self.employees = Employees()
        # self.tools = SortingTools







    # def get_employees_list(self,):
    #     """
    #         Выдает все имеющиеся данные списком.
    #         Предоставляет информацию пользователю о Компании.
    #         На более низком уровне: преобразует список картежей (данных сотрудника в список).
    #     """
    #
    #     employees_data = self.employees.get_employees_raw_data











    # def shell_sorting_dict(arr):
    #     n = len(arr)
    #     gap = n // 2
    #
    #     while gap > 0:
    #         for i in range(gap, n):
    #             temp = arr[i]
    #             j = i
    #             while j >= gap and arr[j - gap] > temp:
    #                 arr[j] = arr[j - gap]
    #                 j -= gap
    #             arr[j] = temp
    #         gap //= 2
    #
    #     return arr


# print(Employees().get_employee_data_tuple)

# def shell_sorting_dict(dict_:dict):
#     pass

# print(Employees()._employees_data_list)

# for r in Employees()._employees_data_list:
#     q = r[0]
#     print(q)


# print(Employees())
# print(Employees().get_employees_data_str)










# =============================================================================
#     def __init__(self):
#         # Значения по умолчанию:
#         self._employees_data_list = [
#             Employee(
#                 family_name='Перов', name='Александр', patronymic='Семенович', ege=23, salary=150
#             ).get_employee_data_tuple,
#             Employee(
#                 family_name='Иванов', name='Артур', patronymic='Александрович', ege=23, salary=250
#             ).get_employee_data_tuple,
#             Employee(
#                 family_name='Сидоров', name='Дмитрий', patronymic='Валерьянович', ege=23, salary=75
#             ).get_employee_data_tuple,
#             Employee(
#                 family_name='Прохоров', name='Виталий', patronymic='Геннадиевич', ege=23, salary=50
#             ).get_employee_data_tuple,
#         ]
