import socket
import threading
from colorama import Fore, Style

target = input("Entre com o alvo: ")
# ports = [22, 80, 443, 53, 21, 23, 25, 8080, 465, 993, 995]
#closed_ports = 0

def portscan():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        banner = sock.recv(1024).decode('utf-8')
        sock.close()
    except:
        return
    if result == 0:
        print(Fore.GREEN + f"[+] Porta {port} Aberta! -> {banner}" + Style.RESET_ALL)
    if banner:
        checkVulns(banner)
    else:
        pass

def checkVulns(banner):
    with open("vulnerabilities", "r") as f:
        vulns = f.readlines()
        f.close()
    for line in vulns:
        if line.strip('\n') in banner:
            print(Fore.RED + f"[!] Vulnerability found on {banner}" + Style.RESET_ALL)
            return

for port in range(1000):
    threading.Thread(target=portscan()).start()
