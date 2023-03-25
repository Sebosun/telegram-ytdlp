from __future__ import unicode_literals
from typing import Tuple
import yt_dlp as youtube_dl
import os

max_filesize = 1.8 * 1024 * 1024 * 1024  # 1800 MB in bytes, just under 2gb mark to be sure

ydl_opts = {
    'outtmpl': './downloads/%(title)s.%(ext)s',
    'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
    'playlistend': 1,
}

def download_video(url: str) -> Tuple[str, None] | Tuple[None, Exception]:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            filename = ydl.prepare_filename(ydl.extract_info(url))
            return filename, None
        except Exception as e:
            return None, e

def delete_created_video(path:str):
    if os.path.exists(path):
        os.remove(path)
        return True
    return False
