from datetime import datetime
from sqlalchemy import ForeignKey, MetaData
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    metadata = MetaData(schema="book_store")


class Book(Base):
    __tablename__ = "books"

    book_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    author_id: Mapped[str] = mapped_column(ForeignKey("authors.author_id"))
    genre_id: Mapped[int] = mapped_column(ForeignKey("genres.genre_id"))
    price: Mapped[int] = mapped_column()
    amount: Mapped[int] = mapped_column()

    def __repr__(self):
        return f"{self.book_id}, {self.title}, {self.author_id}, {self.genre_id}, {self.price}, {self.amount}"


class Genre(Base):
    __tablename__ = "genres"

    genre_id: Mapped[int] = mapped_column(primary_key=True)
    name_genre: Mapped[str] = mapped_column()

    def __repr__(self):
        return f"{self.genre_id}, {self.genre_id}"


class Author(Base):
    __tablename__ = "authors"

    author_id: Mapped[int] = mapped_column(primary_key=True)
    name_author: Mapped[str] = mapped_column()

    def __repr__(self):
        return f"{self.author_id}, {self.name_author}"


class Client(Base):
    __tablename__ = "clients"

    client_id: Mapped[int] = mapped_column(primary_key=True)
    name_client: Mapped[str] = mapped_column()
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.city_id"))
    email: Mapped[str] = mapped_column()

    def __repr__(self):
        return f"{self.client_id}, {self.name}, {self.surname}, {self.patronymic}, {self.address}, {self.phone}"


class City(Base):
    __tablename__ = "cities"

    city_id: Mapped[int] = mapped_column(primary_key=True)
    name_city: Mapped[str] = mapped_column()
    days_delivery: Mapped[int] = mapped_column()

    def __repr__(self):
        return f"{self.city_id}, {self.name_city}, {self.days_delivery}"


class Buy(Base):
    __tablename__ = "buy"

    buy_id: Mapped[int] = mapped_column(primary_key=True)
    buy_description: Mapped[str] = mapped_column()
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.client_id"))

    def __repr__(self):
        return f"{self.buy_id}, {self.buy_description}, {self.client_id}"


class BuyBook(Base):
    __tablename__ = "buy_book"

    buy_book_id: Mapped[int] = mapped_column(primary_key=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey("buy.buy_id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("books.book_id"))
    amount: Mapped[int] = mapped_column()

    def __repr__(self):
        return f"{self.buy_book_id}, {self.buy_id}, {self.book_id}, {self.amount}"


class BuyStep(Base):
    __tablename__ = "buy_step"

    buy_step_id: Mapped[int] = mapped_column(primary_key=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey("buy.buy_id"))
    step_id: Mapped[int] = mapped_column(ForeignKey("step.step_id"))
    date_step_beg: Mapped[datetime] = mapped_column()
    date_step_end: Mapped[datetime] = mapped_column()

    def __repr__(self):
        return f"{self.buy_step_id}, {self.buy_id}, {self.step_id}, {self.date_step_beg}, {self.date_step_end}"


class Step(Base):
    __tablename__ = "step"

    step_id: Mapped[int] = mapped_column(primary_key=True)
    name_step: Mapped[str] = mapped_column()

    def __repr__(self):
        return f"{self.step_id}, {self.name_step}"
