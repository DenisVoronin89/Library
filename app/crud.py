from app.database import load_books, save_books
from app.models import Book
from typing import List, Optional

def add_book(title: str, author: str, year: int) -> Book:
    """Добавляет книгу в библиотеку"""
    books = load_books()
    new_id = max([book.id for book in books], default=0) + 1
    new_book = Book(id=new_id, title=title, author=author, year=year, status="в наличии")
    books.append(new_book)
    save_books(books)
    return new_book

def delete_book(book_id: int) -> Optional[Book]:
    """Удаляет книгу по ID."""
    books = load_books()
    book_to_delete = next((book for book in books if book.id == book_id), None)
    if book_to_delete:
        books.remove(book_to_delete)
        save_books(books)
        return book_to_delete
    return None

def find_books(query: str) -> List[Book]:
    """Ищет книги по title, author или year."""
    books = load_books()
    return [book for book in books if query.lower() in book.title.lower() or query.lower() in book.author.lower() or str(book.year) == query]

def change_status(book_id: int, status: str) -> Optional[Book]:
    """Изменяет статус книги по ID."""
    books = load_books()
    book_to_update = next((book for book in books if book.id == book_id), None)
    if book_to_update:
        book_to_update.status = status
        save_books(books)
        return book_to_update
    return None

def list_books() -> List[Book]:
    """Возвращает список всех книг."""
    return load_books()

