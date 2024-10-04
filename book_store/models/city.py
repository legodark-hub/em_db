from base import Base
from sqlalchemy.orm import Mapped, mapped_column


class City(Base):
    __tablename__ = "cities"

    city_id: Mapped[int] = mapped_column(primary_key=True)
    name_city: Mapped[str]
    days_delivery: Mapped[int]
