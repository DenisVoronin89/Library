from pydantic import BaseModel, Field
from typing import Optional

class Book(BaseModel):
    """
    Pydantic-модель для представления книг в библиотеке.
    """
    id: int = Field(..., description="Уникальный идентификатор книги")
    title: str = Field(..., description="Название книги")
    author: str = Field(..., description="Автор книги")
    year: int = Field(..., ge=0, le=2100, description="Год издания книги")
    status: Optional[str] = Field(default="в наличии", description="Статус книги (в наличии или выдана)")

    class Config:
        """
        Доп. конфиг модели.
        """
        from_attributes = True

    def __repr__(self):
        """
        Форматированный вывод книги.
        """
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}', year={self.year}, status='{self.status}')"

