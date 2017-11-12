import time
from playsound import playsound
from threading import Thread

TOTAL_TIME = float(1.0)
THREAD_NUM = 3
MULTI_PLAY_INTERVAL = TOTAL_TIME / THREAD_NUM
ENTRY_WAITING_TIME = 0


def music_thread():
    # mp3_local_file = './Music/dujiajiyi.flac'
    # mp3_local_file = './Music/xiangyiweiming.mp3'
    mp3_local_file = './Music/Alan_Walker_Fade.flac'
    playsound(mp3_local_file)


music_threads = [Thread(target=music_thread) for _ in range(THREAD_NUM)]

time.sleep(ENTRY_WAITING_TIME)
for i in range(THREAD_NUM):
    music_threads[i].start()
    time.sleep(MULTI_PLAY_INTERVAL)