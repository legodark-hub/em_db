from base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Book(Base):
    __tablename__ = "books"

    book_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author_id: Mapped[str] = mapped_column(ForeignKey("authors.author_id"))
    genre_id: Mapped[int] = mapped_column(ForeignKey("genres.genre_id"))
    price: Mapped[int]
    amount: Mapped[int]
