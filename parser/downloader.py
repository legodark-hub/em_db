from urllib import request, error
import os


def download_file(file_url, file_name, download_dir="downloaded_files"):
    """
    Downloads a file from the given URL and saves it to the given directory.

    Args:
        file_url (str): The URL of the file to download.
        file_name (str): The name of the file to save.
        download_dir (str): The directory to save the file to. Defaults to "downloaded_files".
    """
    try:
        response = request.urlopen(file_url)
        with open(os.path.join(download_dir, file_name), "wb") as file:
            file.write(response.read())
        print(f"Скачан: {file_name}")
    except error.HTTPError as e:
        if e.code == 404:
            print(f"Файл не найден: {file_url}")
        else:
            print(f"Ошибка при скачивании файла: {e}")
    except error.URLError as e:
        print(f"Ошибка: {e}")
