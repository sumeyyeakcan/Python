# import
#
# url=input("url:")
# path=" "
#
# pytube.Youtube(url).streams.get_highest_resolution.download(path)
# youtubeObject = youtubeObject.streams.get_highest_resolution()
import yt_dlp

url = "https://www.youtube.com/watch?v=GILi_0RamtY"

ydl_opts = {"outtmpl": "%(title)s.%(ext)s"}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
