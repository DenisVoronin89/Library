import json
from app.models import Book
from typing import List

BOOKS_DB_FILE = "books.json"

def load_books() -> List[Book]:
    """Загружаеткниги из books.json."""
    try:
        with open(BOOKS_DB_FILE, "r") as file:
            data = json.load(file)
            return [Book(**book) for book in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_books(books: List[Book]) -> None:
    """Сохраняет книги в books.json."""
    with open(BOOKS_DB_FILE, "w") as file:
        json.dump([book.__dict__ for book in books], file, indent=4)

