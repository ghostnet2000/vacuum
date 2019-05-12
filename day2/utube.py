#!/usr/bin/env python3
"""
Usage
=====

   utube [URL]...

This script will download a youtube video for url argument given.


Output
======

The video downloaded, post processed into mkv format with 360p video + opus audio 25kb/s:
"""
# <pep8 complaint>

import youtube_dl
from ffmpy import FFmpeg

# TODO download video starting at time x

def cleanup():
    search = {'video.mp4', 'video.mkv', 'audio.webm', 'audio.opus'}

    import os
    for d in search:
        if os.path.exists(d):
            os.remove(os.path.abspath(d))
    del os


def download(url):
    cleanup()

    yts = [
        {'format': '160', 'outtmpl': 'video.mp4'},  # smallest hq video
        {'format': '249', 'outtmpl': 'audio.webm'},  # best audio quality
    ]

    for f in yts:
        with youtube_dl.YoutubeDL(f) as ydl:
            ydl.download([url])


def extract_audio(media, bitrate):
    extract_cmd = '-c:a libopus -b:a %r' % bitrate
    ff = FFmpeg(
        inputs={media: None},
        outputs={'audio.opus': extract_cmd}
    )
    ff.run()


def post_processing():
    extract_audio('audio.webm', '15k')   # convert audio to opus 25kb/s
    ff = FFmpeg(
        inputs={'video.mp4': None},
        outputs={'video.mkv': '-i audio.opus -c copy'}
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
        except BaseException:
            print("Failed to download %r, error:" % arg)
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
