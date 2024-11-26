import sys
from typing import List

from fastapi import FastAPI, HTTPException, Query
from app.models import Book
from app.crud import add_book, delete_book, find_books, change_status, list_books
from app.views import add_new_book, delete_existing_book, search_books, display_books, change_book_status

app = FastAPI(title="Library Management System", description="API для управления библиотекой", version="1.0.0")


@app.get("/books", response_model=List[Book])
def get_books():
    """
    Получение списка всех книг.
    """
    books = list_books()
    if not books:
        raise HTTPException(status_code=404, detail="Книги отсутствуют")
    return books


@app.post("/books", response_model=Book, status_code=201)
def create_book(title: str, author: str, year: int):
    """
    Добавление новой книги.
    """
    try:
        book = add_book(title, author, year)
        return book
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка при добавлении книги: {e}")


@app.delete("/books/{book_id}", response_model=Book)
def remove_book(book_id: int):
    """
    Удаление книги по ID.
    """
    book = delete_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book


@app.get("/books/search", response_model=List[Book])
def search_for_books(query: str = Query(..., description="Поисковый запрос")):
    """
    Поиск книги по названию, автору или году.
    """
    books = find_books(query)
    if not books:
        raise HTTPException(status_code=404, detail="Книги не найдены")
    return books


@app.patch("/books/{book_id}", response_model=Book)
def update_book_status(book_id: int, status: str):
    """
    Изменение статуса книги.
    """
    valid_statuses = ["в наличии", "выдана"]
    if status not in valid_statuses:
        raise HTTPException(
            status_code=400,
            detail=f"Неверный статус. Доступные значения: {valid_statuses}"
        )
    book = change_status(book_id, status)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book


# === КОНСОЛЬНОЕ МЕНЮ ===

def print_menu():
    """
    Печатает меню для пользователя.
    """
    print("\n1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Найти книгу")
    print("4. Показать все книги")
    print("5. Изменить статус книги")
    print("6. Выход")


def main():
    """
    Главная функция, которая управляет циклом меню.
    """
    while True:
        print_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            add_new_book()
        elif choice == "2":
            delete_existing_book()
        elif choice == "3":
            search_books()
        elif choice == "4":
            try:
                books = list_books()
                display_books(books)
            except Exception as e:
                print(f"Ошибка при получении списка книг: {e}")
        elif choice == "5":
            change_book_status()
        elif choice == "6":
            print("Выход из программы.")
            sys.exit()
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    # Возможность юзать приложение как API или консольное меню
    print("Запущено консольное меню для управления библиотекой.")
    main()

