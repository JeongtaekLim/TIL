# li = [ i for i in range(1000)]
# for idx in range(1000):
#     li[idx] += 2
# print(li)
import threading


def thread_main(li, i):
    for i in range(offset * i, offset * (i + 1)):
        li[i] *= 2


if __name__ == "__main__":
    num_elem = 1000
    num_thread = 4

    offset = num_elem // num_thread
    li = [i + 1 for i in range(num_elem)]
    threads = []

    for i in range(num_thread):
        th = threading.Thread(target=thread_main, args=(li, i))
        threads.append(th)

    for th in threads:
        th.start()

    for th in threads:
        th.join()

    print(li)
