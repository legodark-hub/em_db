from datetime import datetime
from database import get_async_session
from xls_truncate import xls_truncate
import pandas

SELELCTED_COLUMNS = [
    "Код\nИнструмента",
    "Наименование\nИнструмента",
    "Базис\nпоставки",
    "Объем\nДоговоров\nв единицах\nизмерения",
    "Обьем\nДоговоров,\nруб.",
    "Количество\nДоговоров,\nшт.",
]
COLUMNS_RENAME = {
    "Код\nИнструмента": "exchange_product_id",
    "Наименование\nИнструмента": "exchange_product_name",
    "Базис\nпоставки": "delivery_basis_name",
    "Объем\nДоговоров\nв единицах\nизмерения": "volume",
    "Обьем\nДоговоров,\nруб.": "total",
    "Количество\nДоговоров,\nшт.": "count",
}


async def xls_to_db(path: str, date: datetime):
    """
    Saves the given Excel file to the database as a pandas DataFrame.

    The file is truncated to the range of rows between MARKER_BEGIN and MARKER_END and columns specified by the first row.

    The function is designed to work with Excel files downloaded from spimex.com.

    :param path: The path to the Excel file
    :param date: The date of the given Excel file
    """
    trades = pandas.read_excel(path)
    truncated = xls_truncate(trades)
    trades_selected = truncated[SELELCTED_COLUMNS]
    trades_selected = trades_selected.rename(
        columns=COLUMNS_RENAME
    )
    trades_selected["oil_id"] = trades_selected["exchange_product_id"].str[:4]
    trades_selected["delivery_basis_id"] = trades_selected["exchange_product_id"].str[
        4:7
    ]
    trades_selected["delivery_type_id"] = trades_selected["exchange_product_id"].str[-1]
    trades_selected["date"] = date.date()

    async with get_async_session() as session:
        conn = await session.connection()
        await conn.run_sync(
            lambda sync_conn: trades_selected.to_sql(
                name="spimex_trading_results",
                schema="oil_trades",
                con=sync_conn,
                if_exists="append",
                index=False,
            )
        )
        session.commit()

    print(f"в БД записаны данные за {date.date()}")
