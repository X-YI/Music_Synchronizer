import time
from playsound import playsound
from threading import Thread

THREAD_NUM = 2
MULTI_PLAY_INTERVAL = 0.4
ENTRY_WAITING_TIME = 5


def music_thread():
    mp3_local_file = '/Users/yixin/IdeaProjects/Music_Synchronizer/Music/Alan_Walker_Fade.flac'
    playsound(mp3_local_file)


music_threads = [Thread(target=music_thread) for _ in range(THREAD_NUM)]

time.sleep(ENTRY_WAITING_TIME)
for i in range(THREAD_NUM):
    music_threads[i].start()
    time.sleep(MULTI_PLAY_INTERVAL)