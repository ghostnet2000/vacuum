#!/usr/bin/env python3
"""
Usage
=====

   utube [URL]...

This script will download a youtube video for url argument given.
    

Output
======

The video downloaded post processed into mkv format with 360p video + opus audion25kb/s:
"""
# pep8 complaint 

import youtube_dl
from ffmpy import FFmpeg


def download(url):

    yts = [
        {'format': '133', 'outtmpl': 'video.mp4'},  # smallest hq video
        {'format': '249', 'outtmpl': 'audio.webm'},  # best audio quality
    ]

    for f in yts:
        with youtube_dl.YoutubeDL(f) as ydl:
            ydl.download([url])


def post_processing():
    ff = FFmpeg(
        inputs={'video.mp4': None, 'audio.webm': None},
        outputs={'video.mkv': '-c:a libopus -b:a 25k'}
    )

    print(ff.cmd)
    ff.run()


def main():
    import sys
    if "--help" in sys.argv:
        print(__doc__)
        return

    for arg in sys.argv[1:]:
        try:
            download(arg)
            post_processing()
        except:
            print("Failed to download %r, error:" % arg)
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    main()
