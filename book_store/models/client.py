from base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Client(Base):
    __tablename__ = "clients"

    client_id: Mapped[int] = mapped_column(primary_key=True)
    name_client: Mapped[str]
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.city_id"))
    email: Mapped[str]
