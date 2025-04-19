"""
    Модуль взаимодействия с бд.
"""

from sqlalchemy import select, update, delete, and_, or_, func
from sqlalchemy.orm import Session, joinedload
from datetime import datetime
from typing import List

from postgres_part_3.mockup_db import Book, Reader, BorrowedBook


class LibraryManager:
    """
        Основной класс для управления библиотечными операциями.
        Обеспечивает взаимодействие с таблицами книг, читателей и учета выдачи.
    """

    def __init__(self, session: Session):
        self.session = session

    def add_book(self, title: str, author: str, published_year: int | None = None, quantity: int = 1) -> Book:
        """
            Добавляет новую книгу в базу данных.

            Параметры:
                title: Название книги
                author: Автор книги
                published_year: Год публикации (опционально)
                quantity: Количество экземпляров (по умолчанию 1)

            Возвращает:
                Объект добавленной книги

            Исключения:
                ValueError: Если книга с таким названием и автором уже существует
        """

        query = select(Book).where(
            and_(
                func.lower(Book.title) == func.lower(title),
                func.lower(Book.author) == func.lower(author)
            )
        )
        existing_book = self.session.execute(query).scalar()

        if existing_book:
            raise ValueError("Книга с таким названием и автором уже существует")

        new_book = Book(
            title=title,
            author=author,
            published_year=published_year,
            quantity=quantity
        )
        self.session.add(new_book)
        self.session.commit()
        return new_book

    def delete_book(self, book_id: int) -> bool:
        """
            Удаляет книгу из базы данных, если она не выдана читателям.

            Параметры:
                book_id: ID книги для удаления

            Возвращает:
                True если удаление прошло успешно, False если книга не найдена

            Исключения:
                ValueError: Если книга в данный момент выдана читателю
        """

        query = select(BorrowedBook).where(
            and_(
                BorrowedBook.book_id == book_id,
                BorrowedBook.return_date.is_(None)
            )
        )

        active_borrowings = self.session.execute(query).scalar()

        if active_borrowings:
            raise ValueError("Нельзя удалить книгу, так как она выдана читателям")

        delete_stmt = delete(Book).where(Book.id == book_id)
        result = self.session.execute(delete_stmt)
        self.session.commit()

        return result.rowcount > 0

    def register_reader(self, name: str, email: str | None = None) -> Reader:
        """
            Регистрирует нового читателя в системе.

            Параметры:
                name: Имя читателя
                email: Email читателя (опционально)

            Возвращает:
                Объект зарегистрированного читателя

            Исключения:
                ValueError: Если читатель с таким email уже существует
        """

        if email:
            query = select(Reader).where(func.lower(Reader.email) == func.lower(email))
            existing_reader = self.session.execute(query).scalar()

            if existing_reader:
                raise ValueError("Читатель с таким email уже существует")

        new_reader = Reader(name=name, email=email)
        self.session.add(new_reader)
        self.session.commit()

        return new_reader

    def borrow_book(self, book_id: int, reader_id: int) -> BorrowedBook:
        """
            Оформляет выдачу книги читателю.

            Параметры:
                book_id: ID выдаваемой книги
                reader_id: ID читателя

            Возвращает:
                Объект записи о выдаче

            Исключения:
                ValueError: Если книга не найдена, нет доступных экземпляров
                           или читатель не найден
        """

        book = self.session.get(Book, book_id)

        if not book:
            raise ValueError("Книга не найдена")

        if book.quantity < 1:
            raise ValueError("Нет доступных экземпляров этой книги")

        reader = self.session.get(Reader, reader_id)
        if not reader:
            raise ValueError("Читатель не найден")

        book.quantity -= 1
        borrowing_record = BorrowedBook(
            book_id=book_id,
            reader_id=reader_id,
            # borrow_date=datetime.now()
        )

        self.session.add(borrowing_record)
        self.session.commit()

        return borrowing_record

    def get_all_books_sorted(self): # -> List[Book]
        """
            Возвращает список всех книг, отсортированных по году издания.

            Возвращает:
                Список объектов книг
        """

        query = select(Book).order_by(Book.published_year)
        books = self.session.execute(query).scalars().all()

        return [{
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'year': book.published_year,
            'quantity': book.quantity,
            'available': book.quantity > 0
        } for book in books]

    def search_books(self, search_term: str): #  -> List[Book]
        """
            Осуществляет поиск книг по названию или автору.

            Параметры:
                search_term: Строка для поиска

            Возвращает:
                Список найденных книг
        """

        search_pattern = f"%{search_term}%"
        query = select(Book).where(
            or_(
                Book.title.ilike(search_pattern),
                Book.author.ilike(search_pattern)
            )
        )

        books = self.session.execute(query).scalars().all()

        return [{
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'year': book.published_year,
            'quantity': book.quantity,
            'available': book.quantity > 0
        } for book in books]

    def get_active_borrowings(self) -> List[BorrowedBook]:
            """
                Возвращает список текущих выдач книг.

                Возвращает:
                    Список записей о выдаче с загруженными данными книг и читателей
            """

            query = select(BorrowedBook).options(
                joinedload(BorrowedBook.book),
                joinedload(BorrowedBook.reader)
            ).where(
                BorrowedBook.return_date.is_(None)
            )

            result = self.session.execute(query)

            return list(result.unique().scalars())
