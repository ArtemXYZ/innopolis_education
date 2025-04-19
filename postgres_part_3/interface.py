"""
    Модуль взаимодействия с пользователем (тесты).
"""

# from postgres_part_3.init_db import InitDB
from postgres_part_3.libra import LibraryManager
from postgres_part_3.configs import LOCDB_SESSION

# Создание бд и таблиц. +
# InitDB().create_db()

manager = LibraryManager(session=LOCDB_SESSION)

# manager.add_book(title='Тестовая книга', author='Познышев', published_year=1989, quantity=2)  # +

# [{'id': 1, 'title': 'Тестовая книга', 'author': 'Познышев', 'year': 1989, 'quantity': 2, 'available': True}] +
# print(manager.search_books(search_term='Тестовая книга'))


# [{'id': 1, 'title': 'Тестовая книга', 'author': 'Познышев', 'year': 1989, 'quantity': 2, 'available': True}] +
# print(manager.get_all_books_sorted())


# Новый читатель: Artem / email: @@@ +
# rr = manager.register_reader(name='Artem', email='@@@')
# print(f'Новый читатель: {rr.name} / email: {rr.email}')


# book_id: 1 / id: 2 / borrow_date: 2025-04-19 14:43:45
# rr = manager.borrow_book(book_id=1, reader_id=1)
# print(f'book_id: {rr.book_id} / id: {rr.id} / borrow_date: {rr.borrow_date}')

# # [] +
# rr = manager.get_active_borrowings()
# print(rr)

# +
# manager.delete_book(book_id=1)
