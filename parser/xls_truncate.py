import pandas

MARKER_BEGIN = "Единица измерения: Метрическая тонна"
MARKER_END = "Итого:"

def xls_truncate(trades: pandas.DataFrame) -> pandas.DataFrame:
    """
    Truncate the given DataFrame to the range of rows between MARKER_BEGIN and MARKER_END and columns specified by the first row.

    The function is designed to work with Excel files downloaded from spimex.com.

    :param df: The DataFrame to truncate
    :return: The truncated DataFrame
    """
    
    start_index = trades[trades["Форма СЭТ-БТ"] == MARKER_BEGIN].index[0]
    trades = trades.iloc[start_index + 1 :].reset_index(drop=True)
    trades.columns = trades.iloc[0]
    trades = trades.drop([0, 1]).reset_index(drop=True)
    end_index = trades[trades["Код\nИнструмента"] == MARKER_END].index[0]
    trades = trades.iloc[:end_index]
    trades = trades.drop(
        trades[trades["Количество\nДоговоров,\nшт."] == "-"].index
    ).reset_index(drop=True)
    
    return trades