from moviepy import editor
from threading import Thread
from time import time

clips = ["./videos/c1.mp4", "./videos/c2.mp4", "./videos/c3.mp4", "./videos/c4.mp4", "./videos/c5.mp4"]

def convert_without_threading():
    start_time = time()
    for i, clip in enumerate(clips):
        video = editor.VideoFileClip(clip)
        video.audio.write_audiofile(f'audio {i+1}.mp3')
    return time() - start_time

def convert_with_threading():
    threads = []
    for i, clip in enumerate(clips):
        new_thread = Thread(target=conversion, args=[clip, i])
        threads.append(new_thread)

    start_time = time()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return time() - start_time

def conversion(clip, i):
    video = editor.VideoFileClip(clip)
    video.audio.write_audiofile(f'audio {i+1}.mp3')

time_without_threading = convert_without_threading()
time_with_threading = convert_with_threading()
print("Time without threading:", time_without_threading)
print("Time with threading:", time_with_threading)