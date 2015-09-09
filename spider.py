import threading
import time
import os


def dochore():
    time.sleep(0.5)


def booth(tid):
    global i
    global lock
    while True:
        lock.acquire()
        if i != 0:
            i -= 1
            print(tid, ':now left :', i)
            dochore()
        else:
            print("Thread_id", tid, "no more tickets")
            os._exit()
        lock.release()
        dochore()


i = 10
lock = threading.Lock()

for k in xrange(1, 10):
    new_thread = threading.Thread(target=booth, args=(k,))
    new_thread.start()
