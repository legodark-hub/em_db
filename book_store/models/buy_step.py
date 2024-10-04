from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from base import Base

class BuyStep(Base):
    __tablename__ = "buy_step"

    buy_step_id: Mapped[int] = mapped_column(primary_key=True)
    buy_id: Mapped[int] = mapped_column(ForeignKey("buy.buy_id"))
    step_id: Mapped[int] = mapped_column(ForeignKey("step.step_id"))
    date_step_beg: Mapped[datetime]
    date_step_end: Mapped[datetime]