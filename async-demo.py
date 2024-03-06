"""
Demo for sequential way to download images
"""
import asyncio
import aiohttp
import os
from pathlib import Path
import time
from typing import List, Optional

async def download_file(session:aiohttp.ClientSession, photo_id: str, dirname: str) -> None:
    try:
        url = f"https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=640&h=480"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
        filepath = Path(f"{dirname}/{photo_id}.jpeg")

        async with session.get(url, headers=headers) as response:
            with open(filepath, "wb") as img_file:
                async for chunk in response.content.iter_chunked(1024):
                    img_file.write(chunk)
        print(f"Download: {photo_id}.jpeg")

    except Exception as e:
        print(e)

async def download_files(photo_ids: List[str], dirname: Optional[str]="images_02") -> None:
    tasks = []
    
    os.makedirs(dirname, exist_ok=True)
    async with aiohttp.ClientSession() as session:    
        tasks = [download_file(session, photo_id, dirname) for photo_id in photo_ids]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    with open("list_photo_ids.txt", "r") as f:
        photo_ids =  [line.strip() for line in f.readlines()]

        start_time = time.time()
        asyncio.run(download_files(photo_ids))
        end_time = time.time()

        print("Time: ", end_time - start_time)
