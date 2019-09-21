import requests
from multiprocessing import Process, Queue
import time


def work(q):
    r = requests.get("https://httpbin.org/uuid")
    if r.status_code != 200:
        print("error!")
        return
    data = r.json()
    print(data)
    q.put(data)


def process_example():
    q = Queue()
    plist = list()
    for i in range(5):
        plist.append(Process(target=work, args=(q,)))
    for p in plist:
        p.start()
    for p in plist:
        p.join()


def normal_example():
    q = Queue()
    for i in range(5):
        work(q)


if __name__ == "__main__":
    start = time.time()
    process_example()
    print("time:: ", time.time() - start)
    start = time.time()
    normal_example()
    print("time:: ", time.time() - start)
