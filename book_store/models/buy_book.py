from base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

class BuyBook(Base):
    __tablename__ = "buy_book"

    buy_book_id: Mapped[int] = mapped_column(primary_key=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey("buy.buy_id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("books.book_id"))
    amount: Mapped[int]