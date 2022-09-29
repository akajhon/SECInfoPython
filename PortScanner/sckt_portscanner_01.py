import socket
import threading
from colorama import Fore, Style

target = input("Entre com o alvo: ")
# ports = [22, 80, 443, 53, 21, 23, 25, 8080, 465, 993, 995]
#closed_ports = 0
def portscan():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    sock.close()
    if result == 0:
        print(Fore.GREEN + f"[+] Porta {port} Aberta! [+]\n" + Style.RESET_ALL)
    else:
        pass
        #closed_ports += 1
        #print(Fore.RED + f"[!] {closed_ports} Portas Fechadas! [+]\n" + Style.RESET_ALL)

for port in range(1000):
    threading.Thread(target=portscan()).start()

