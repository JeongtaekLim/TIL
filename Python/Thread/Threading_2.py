# -*- coding: utf-8 -*-
import threading

g_count = 0

def thread_main():
    global g_count
    lock.acquire()
    for i in range(100000):
        g_count += 1
    lock.release()

# thread 에 할당
threads = []
lock = threading.Lock()

for i in range(100):
    th = threading.Thread(target=thread_main)
    threads.append(th)

# thread 실행
for th in threads:
    th.start()

# thread 종료
for th in threads:
    th.join()

print(g_count)
