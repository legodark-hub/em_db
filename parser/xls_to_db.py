from datetime import datetime
from database import engine
import pandas


def xls_to_db(path: str, date: datetime):
    trades = pandas.read_excel(path)
    # обрезка начала таблицы
    marker = "Единица измерения: Метрическая тонна"
    start_index = trades[trades["Форма СЭТ-БТ"] == marker].index[0]
    trades = trades.iloc[start_index + 1 :].reset_index(drop=True)
    trades.columns = trades.iloc[0]
    trades = trades.drop([0, 1]).reset_index(drop=True)
    # обрезка конца таблицы
    end_index = trades[trades["Код\nИнструмента"] == "Итого:"].index[0]
    trades = trades.iloc[:end_index]
    trades = trades.drop(
        trades[trades["Количество\nДоговоров,\nшт."] == "-"].index
    ).reset_index(drop=True)

    trades_selected = trades[
        [
            "Код\nИнструмента",
            "Наименование\nИнструмента",
            "Базис\nпоставки",
            "Объем\nДоговоров\nв единицах\nизмерения",
            "Обьем\nДоговоров,\nруб.",
            "Количество\nДоговоров,\nшт.",
        ]
    ]
    trades_selected = trades_selected.rename(
        columns={
            "Код\nИнструмента": "exchange_product_id",
            "Наименование\nИнструмента": "exchange_product_name",
            "Базис\nпоставки": "delivery_basis_name",
            "Объем\nДоговоров\nв единицах\nизмерения": "volume",
            "Обьем\nДоговоров,\nруб.": "total",
            "Количество\nДоговоров,\nшт.": "count",
        }
    )
    trades_selected["oil_id"] = trades_selected["exchange_product_id"].str[:4]
    trades_selected["delivery_basis_id"] = trades_selected["exchange_product_id"].str[
        4:7
    ]
    trades_selected["delivery_type_id"] = trades_selected["exchange_product_id"].str[-1]
    trades_selected["date"] = date.date()

    trades_selected.to_sql(
        name="spimex_trading_results",
        schema="oil_trades",
        con=engine,
        if_exists="append",
        index=False,
    )
    print(f"в БД записаны данные за {date.date()}")
