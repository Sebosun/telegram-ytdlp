from __future__ import unicode_literals
import yt_dlp as youtube_dl
import os

max_filesize = 1.8 * 1024 * 1024 * 1024  # 1800 MB in bytes, just under 2gb mark to be sure

ydl_opts = {
    'outtmpl': './downloads/%(title)s.%(ext)s',
    'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
    'playlistend': 1,
}

def downloadVideo(url: str):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            filename = ydl.prepare_filename(ydl.extract_info(url))
            return filename
        except:
            return False

def deleteCreatedVideo(path:str):
    if os.path.exists(path):
        os.remove(path)
        return True
    return False
