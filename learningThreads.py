'''
use of threads is like running multiple programs at once
threads actually take turns executing
A thread is a block of code that executes
'''
import random
import time
import threading


def executeThread(i):
    print("Threat {} sleeps at {}".format(i, time.strftime("%H: %M: %S", time.gmtime())))
    randSleepTime = random.randint(1, 5)
    # make thread pause
    time.sleep(randSleepTime)

    print("Thread {} stops sleeping at{}".format(i, time.strftime("%H: %M: %S", time.gmtime())))


for i in range(10):
    thread = threading.Thread(target=executeThread, args=(i,))
    thread.start()

    # print num of threads currently executing
    print("Active Threads: ", threading.active_count())
    print("Thread Objects: ", threading.enumerate())
