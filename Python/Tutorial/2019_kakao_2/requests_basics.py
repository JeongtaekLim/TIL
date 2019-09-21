import requests
import time

if __name__ == "__main__":
    start = time.time()
    r = requests.get("https://httpbin.org/status/404")
    if r.status_code != 200:
        print("error!")
    else:
        data = r.json()
        print(data)
    print("time:: ", time.time() - start)
