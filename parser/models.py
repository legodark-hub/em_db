from datetime import datetime
from sqlalchemy import MetaData, DateTime, func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    metadata = MetaData(schema="oil_trades")


class OilTrade(Base):
    __tablename__ = "spimex_trading_results"
    id: Mapped[int] = mapped_column(primary_key=True)
    exchange_product_id: Mapped[str] = mapped_column()
    exchange_product_name: Mapped[str] = mapped_column()
    oil_id: Mapped[str] = mapped_column()
    delivery_basis_id: Mapped[str] = mapped_column()
    delivery_basis_name: Mapped[str] = mapped_column()
    delivery_type_id: Mapped[str] = mapped_column()
    volume: Mapped[int] = mapped_column()
    total: Mapped[int] = mapped_column()
    count: Mapped[int] = mapped_column()
    date: Mapped[datetime] = mapped_column()
    created_on: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
    updated_on: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )
