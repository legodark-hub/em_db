from datetime import datetime, timedelta
import os
from downloader import download_file
from database import create_db
from xls_to_db import xls_to_db
import time
import asyncio

BASE_URL = "https://spimex.com/upload/reports/oil_xls/oil_xls_"

DOWNLOAD_DIR = "parser/xls_files"

today = datetime.today()
date_range = today - timedelta(days=30)


async def main():
    tasks = []
    
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    await create_db()
    current_date = date_range
    while current_date < today:
        # пропуск выходных дней
        if current_date.weekday() >= 5:
            current_date += timedelta(days=1)
            continue

        date_str = current_date.strftime("%Y%m%d")

        file_url = f"{BASE_URL}{date_str}162000.xls"
        file_name = f"oil_xls_{date_str}.xls"
        
        download_task = await download_file(file_url, file_name, DOWNLOAD_DIR)
        task = asyncio.create_task(xls_to_db(download_task, current_date))
        tasks.append(task)
        
        current_date += timedelta(days=1)
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    print(f"Время выполнения: {end_time - start_time} сек.")