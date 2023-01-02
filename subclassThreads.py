'''
you can subclass a thread  obj and find what happens each time a thread is executed inside run
'''
import threading
import  time
import random

class CustThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        getTime(self.name)

        print("Thread", self.name, "Execution Ends")
def getTime(name):
    print("Thread {} sleeps at {}". format(name, time.strftime("%H: %M: %S", time.gmtime())))

    randSleepTime = random.randint(1, 5)
    time.sleep(randSleepTime)
# thread obj
thread1 = CustThread("1")
thread2 = CustThread("2")
thread1.start()
thread2.start()
#check if thread is active
print("Thread is Alive: ", thread1.is_alive())
print("Thread is Alive: ", thread2.is_alive())
#get thread name
#instead of getname or __getattribute__ use .name
print("Thread 1 Name: ", thread1.name)
print("Thread 2 Name: ", thread2.name)#__getattribute__()) #TypeError: expected 1 argument, got 0
#join to wait for threads to exit
thread1.join()
thread2.join()

print("Execution ends")