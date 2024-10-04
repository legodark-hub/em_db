from base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Author(Base):
    __tablename__ = "authors"

    author_id: Mapped[int] = mapped_column(primary_key=True)
    name_author: Mapped[str]