from datetime import datetime, timedelta
import os
from downloader import download_file
from database import create_db
from xls_to_db import xls_to_db

create_db()

BASE_URL = "https://spimex.com/upload/reports/oil_xls/oil_xls_"

DOWNLOAD_DIR = "parser/xls_files"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

today = datetime.today()
date_range = today - timedelta(days=30)

current_date = date_range
while current_date < today:
    # пропуск выходных дней
    if current_date.weekday() >= 5:
        current_date += timedelta(days=1)
        continue

    date_str = current_date.strftime("%Y%m%d")

    file_url = f"{BASE_URL}{date_str}162000.xls"
    file_name = f"oil_xls_{date_str}.xls"

    download_file(file_url, file_name, DOWNLOAD_DIR)
    xls_to_db(f"{DOWNLOAD_DIR}/{file_name}", current_date)

    current_date += timedelta(days=1)
