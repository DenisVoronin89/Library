from typing import List
from app.crud import add_book, delete_book, find_books, change_status, list_books
from app.models import Book

def display_books(books: List[Book]) -> None:
    """Отображает все книги."""
    if not books:
        print("Нет книг в библиотеке.")
    for book in books:
        print(book)

def get_book_details() -> tuple:
    """Получает данные книги от юзера"""
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = int(input("Введите год издания книги: "))
    return title, author, year

def add_new_book() -> None:
    """Добавляет новую книгу"""
    title, author, year = get_book_details()
    book = add_book(title, author, year)
    print(f"Книга добавлена: {book}")

def delete_existing_book() -> None:
    """Удаляет книгу по ID"""
    try:
        book_id = int(input("Введите ID книги для удаления: "))
        book = delete_book(book_id)
        if book:
            print(f"Книга удалена: {book}")
        else:
            print("Книга не найдена.")
    except ValueError:
        print("Неверный формат ID.")

def search_books() -> None:
    """Ищет книги по запросу"""
    query = input("Введите название, автора или год книги для поиска: ")
    books = find_books(query)
    if books:
        print("Найденные книги:")
        display_books(books)
    else:
        print("Книги не найдены.")

def change_book_status() -> None:
    """Изменяет статус книги по ID"""
    try:
        book_id = int(input("Введите ID книги для изменения статуса: "))
        status = input("Введите новый статус книги (в наличии/выдана): ")
        book = change_status(book_id, status)
        if book:
            print(f"Статус книги изменен: {book}")
        else:
            print("Книга не найдена.")
    except ValueError:
        print("Неверный формат ID.")

