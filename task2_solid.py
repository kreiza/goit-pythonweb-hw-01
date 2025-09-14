"""
Завдання 2: Рефакторинг коду бібліотеки згідно принципів SOLID
"""
import logging
from abc import ABC, abstractmethod
from typing import List, Optional

# Налаштування логування
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


class Book:
    """Клас для представлення книги (SRP)"""

    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    """Інтерфейс для бібліотеки (ISP)"""

    @abstractmethod
    def add_book(self, title: str, author: str, year: str) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> bool:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass

    @abstractmethod
    def get_books(self) -> List[Book]:
        pass


class Library(LibraryInterface):
    """Реалізація бібліотеки (LSP, OCP)"""

    def __init__(self) -> None:
        self._books: List[Book] = []

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self._books.append(book)
        logger.info(f"Книгу '{title}' додано до бібліотеки")

    def remove_book(self, title: str) -> bool:
        for book in self._books:
            if book.title == title:
                self._books.remove(book)
                logger.info(f"Книгу '{title}' видалено з бібліотеки")
                return True
        logger.info(f"Книгу '{title}' не знайдено")
        return False

    def show_books(self) -> None:
        if not self._books:
            logger.info("Бібліотека порожня")
            return
        logger.info("Книги в бібліотеці:")
        for book in self._books:
            logger.info(str(book))

    def get_books(self) -> List[Book]:
        return self._books.copy()


class LibraryManager:
    """Менеджер для управління бібліотекою (DIP)"""

    def __init__(self, library: LibraryInterface) -> None:
        self._library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        self._library.add_book(title, author, year)

    def remove_book(self, title: str) -> None:
        self._library.remove_book(title)

    def show_books(self) -> None:
        self._library.show_books()


def main() -> None:
    """Головна функція програми"""
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
