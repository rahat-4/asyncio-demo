"""
Demo for sequential way to download images
"""
from pathlib import Path
import requests
import time
from typing import List, Optional

def download_file(photo_id: str, dirname: str) -> None:
    try:
        url = f"https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=640&h=480"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
        filepath = Path(f"{dirname}/{photo_id}.jpeg")

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            with open(filepath, "wb") as img_file:
                img_file.write(response.content)
        print(f"Download: {photo_id}.jpeg")

    except Exception as e:
        print(e)

def download_files(photo_ids: List[str], dirname: Optional[str]="images_01") -> None:
    for photo_id in photo_ids:          
        download_file(photo_id, dirname)


if __name__ == "__main__":
    with open("list_photo_ids.txt", "r") as f:
        photo_ids =  [line.strip() for line in f.readlines()]

        start_time = time.time()
        download_files(photo_ids)
        end_time = time.time()

        print("Time: ", end_time - start_time)
