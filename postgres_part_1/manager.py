"""
    Модуль управления консольной логикой.
"""
from sqlalchemy import text

from postgres_part_1.init_db import InitDB
from configs import LOCDB_SESSION
from postgres_part_1.sqls import *

# ======================================================================================================================
class PostgeManager:
    """
        Класс управления консольной логикой (функционал добавления, изменения, удаления, а также чтения из базы данных).
    """

    def __init__(self):
        self._session = LOCDB_SESSION
        self._initer_db = InitDB(self._session, SQL_CREATE_TABLE, SQL_DROP_TABLE)

    def start_db(self):
        """
           Запуск базы данных / создание.
        """

        self._initer_db.create_db()

    def finish_db(self):
        """
            Удаление базы данных.
        """

        self._initer_db.drop_db()

    def get_students_data(self, last_name: str | None = None) -> list:
        """
            Предоставляет данные о студентах из базы данных. Запрос предоставляет все данные о студенте по фамилии.
            :return: Список картежей (fetchall()).
        """

        _params = last_name or None

        if not last_name:
            result = self._session.execute(text(SQL_SELECT_STUDENTS))
        else:
            result = self._session.execute(text(SQL_SELECT_STUDENTS_BY_NAME), params={'last_name_value': _params})

        return result.fetchall()

    def insert_student_data(
            self,
            first_name: str,
            last_name: str,
            course_number: int,
            age: int
    ) -> None:
        """
            Записывает данные о студентах в базу данных.
            :return: None.
        """

        if first_name and last_name and course_number and age:

            # Формируем набор данных для подстановки в SQL.
            params_value = {
                'first_name_value': first_name,
                'last_name_value': last_name,
                'course_number_value': course_number,
                'age_value': age
            }

            self._session.execute(text(SQL_INSERT_ROW_STUDENTS), params=params_value)
            self._session.commit()

            print(f'Запись успешно создана!')
        else:
            raise ValueError(f'Метод ожидает передачи всех обязательных аргументов!')

    def delete_student_data(self, last_name: str) -> bool:
        """
            Удаляет строку, предварительно проверив наличия такой записи.
            :return: True | False.
        """

        if last_name:
            # Формируем набор данных для подстановки в SQL.
            params_value = {'last_name_value': last_name}

            # Проверка на существование такой записи:
            if self.get_students_data(last_name=last_name):
                self._session.execute(text(SQL_DELETE_ROW_STUDENTS), params=params_value)
                self._session.commit()
                print('Запись успешно удалена!')
                return True
            else:
                print('Такой записи не существует!')
                return False
        else:
            raise ValueError(f'Метод ожидает передачи всех обязательных аргументов!')

    def update_student_data(self, last_name: str, new_course_number_value: int) -> bool:
        """
            Апдейтит строку, предварительно проверив наличия такой записи.
            :return: True | False.
        """

        if last_name and new_course_number_value:
            # Формируем набор данных для подстановки в SQL.
            params_value = {'last_name_value': last_name, 'course_number_value': new_course_number_value}

            # Проверка на существование такой записи:
            if self.get_students_data(last_name=last_name):
                self._session.execute(text(SQL_UPDATE_ROW_STUDENTS), params=params_value)
                self._session.commit()
                print('Запись успешно обновлена!')
                return True
            else:
                print('Такой записи не существует!')
                return False
        else:
            raise ValueError(f'Метод ожидает передачи всех обязательных аргументов!')





# ww = PostgeManager()
# ww.start_db()
# ww.insert_student_data(
#     first_name="Артем",
#     last_name="Познышев",
#     course_number=5,
#     age=30)
# print(ww.get_students_data(last_name='Познышев'))
# print(ww.get_students_data())
# print(ww.get_students_data(last_name='Артем'))
# print(ww.update_student_data(last_name='Познышев', new_course_number_value=6))

# tuple_list = [tuple(row) for row in result.fetchall()]
