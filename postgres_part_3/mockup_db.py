"""
    ОРМ макет базы данных.
    Содержит перечень всех полей базы данных.
"""

# -------------------------------- Стандартные модули
# -------------------------------- Сторонние библиотеки
# - image LargeBinary, Float, Integer, Text, Boolean,
from sqlalchemy import (DateTime, String, func, ForeignKey, CheckConstraint)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# -------------------------------- Локальные модули


# ======================================================================================================================
# class Base(DeclarativeBase):
#     """
#         Базовая настройка всех полей в бд.
#         Все создаваемые таблицы по умолчанию будут иметь данные поля (дата создания и обновления).
#     """
#
#     # Эти поля (в родительском классе) автоматически унаследуются дочерним классам (все ниже).
#     created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
#     updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())

class Base(DeclarativeBase):
    pass


class Book(Base):
    """
        Таблица для хранения книг.
    """

    __tablename__ = 'books'
    __table_args__ = (
        CheckConstraint('quantity >= 0', name='check_quantity_positive'),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)  # (значение обязательно)
    author: Mapped[str] = mapped_column(String(50), nullable=False)  # (значение обязательно)
    published_year: Mapped[int] = mapped_column(nullable=True)
    quantity: Mapped[int] = mapped_column(nullable=False)  # CHECK (quantity >= 0)

    # Отношение "один ко многим" с BorrowedBooks
    borrow_records: Mapped[list['BorrowedBook']] = relationship(
        "BorrowedBook",
        back_populates="book",
        cascade="all, delete-orphan"
    )

    # def __str__(self) -> str:
    #     return (
    #         f"Book(id={self.id}, "
    #         f"title='{self.title}', "
    #         f"author='{self.author}', "
    #         f"year={self.published_year}, "
    #         f"quantity={self.quantity}, "
    #         f"available={'yes' if self.quantity > 0 else 'no'})"
    #     )




class Reader(Base):
    """
       Таблица для хранения читателей.
    """

    __tablename__ = 'readers'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)  # (значение обязательно)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=True)

    # Отношение "один ко многим" с BorrowedBooks
    borrow_records: Mapped[list['BorrowedBook']] = relationship(
        "BorrowedBook",
        back_populates="reader",
        cascade="all, delete-orphan"
    )


class BorrowedBook(Base):
    """
       Таблица для регистрации выдачи книг.
    """

    __tablename__ = 'borrowed_books'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id'), nullable=False, index=True)  # Fk
    reader_id: Mapped[int] = mapped_column(ForeignKey('readers.id'), nullable=False, index=True)  # Fk
    borrow_date: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), nullable=False)
    return_date: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), nullable=True)

    # Отношение "многие к одному" с Books
    book: Mapped['Book'] = relationship("Book", back_populates="borrow_records")

    # Отношение "многие к одному" с Readers
    reader: Mapped['Reader'] = relationship("Reader", back_populates="borrow_records")
