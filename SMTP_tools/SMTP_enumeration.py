from colorama import Fore, Style
import socket, sys

target_server = input("[+] Defina o Alvo: ")
with open("smtp_usernames", "r") as f:
    usernames = f.readlines()
    f.close()
print("+-------------------+\n")

for user in usernames:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        user = user.strip('\n')
        sock.connect((target_server, 25))
        sock.recv(1024)
        sock.send(("VRFY "+ user + "\n").encode('utf-8'))
        smtp_answer = sock.recv(1024).decode('utf-8')
        sock.close()
        if '252' in smtp_answer:
            print(Fore.GREEN + f"[+] User {user} Valido! [+]\n" + Style.RESET_ALL)
        elif '550' in smtp_answer:
            print(Fore.RED + f"[!] User {user} Invalido! [!]\n" + Style.RESET_ALL)
        elif '503' in smtp_answer:
            print(Fore.BLUE + "[!] Servidor requer autenticacao [!]\n" + Style.RESET_ALL)
            break
        elif '500' in smtp_answer:
            print(Fore.BLUE + "[!] Comando VRFY nao suportado [!]\n" + Style.RESET_ALL)
            break
        else:
            print(Fore.BLUE + f"[!] {smtp_answer} [!]\n" + Style.RESET_ALL)
    except socket.error as err:
        print(f"[!] {err} [!]")
        sys.exit()