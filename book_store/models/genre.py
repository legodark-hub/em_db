from base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Genre(Base):
    __tablename__ = "genres"

    genre_id: Mapped[int] = mapped_column(primary_key=True)
    name_genre: Mapped[str]
