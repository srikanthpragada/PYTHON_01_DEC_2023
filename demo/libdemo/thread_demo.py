import threading
from threading import Thread


class NumbersThread(Thread):
    def run(self):
        for n in range(1, 10):
            print('Numbers', n)


print(threading.main_thread())

nt = NumbersThread()
nt.start()

for n in range(1, 10):
    print('Main', n)
