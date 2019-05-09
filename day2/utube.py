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


def download():

    yts = [
        {'format': '133', 'outtmpl': 'video.mp4'},  # smallest hq video
        {'format': '249', 'outtmpl': 'audio.webm'},  # best audio quality
    ]

    for f in yts:
        with youtube_dl.YoutubeDL(f) as u:
            u.download(['https://www.youtube.com/watch?v=_LMUWV1Tacs'])


def postprocessing():
    ff = FFmpeg(
        inputs={'video.mp4': None, 'audio.webm': None},
        outputs={'video.mkv': '-c:a libopus -b:a 25k'}
    )

    print(ff.cmd)
    ff.run()


def main():
    download()
    postprocessing()

if __name__ == "__main__":
    main()
