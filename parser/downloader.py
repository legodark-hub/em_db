from urllib import request, error
import os
import aiofiles
import aiohttp


async def download_file(file_url, file_name, download_dir="downloaded_files"):
    """
    Downloads a file from the given URL and saves it to the given directory.

    Args:
        file_url (str): The URL of the file to download.
        file_name (str): The name of the file to save.
        download_dir (str): The directory to save the file to. Defaults to "downloaded_files".
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(file_url) as response:
                if response.status == 200:
                    async with aiofiles.open(os.path.join(download_dir, file_name), mode="wb") as file:
                        await file.write(await response.read())
                    print(f"Скачан: {file_name}")
                    return f"{download_dir}/{file_name}"
                else:
                    print(f"Ошибка скачивания {file_url}, {response.status}")
                    return None
    except aiohttp.ClientError as e:
        print(f"Ошибка скачивания: {e}")


