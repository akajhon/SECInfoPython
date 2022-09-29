import socket
import requests

https = "https://"
target = input("[+] Entre com o alvo: ")
https_target = https + target

def check_http():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target, 80))
    sock.sendall((f"HEAD / HTTP/1.1\r\nHost:{target}\r\n\r\n").encode())
    while True:
        data = sock.recv(512).decode()
        if (len(data) < 1):
            print("[!] ERROR RETRIEVING HTTP HEADERS [!]")
            break
        else:
            print("\n[!] HTTP HEADERS [!]")
            print(data)
            break
    sock.close()

def check_https():
    try:
        https_request = requests.head(https_target)
        https_headers = https_request.headers
        print("[!] HTTPS HEADERS [!]")
        for x, y in https_headers.items():
            print(f"{x} : {y}")
    except:
        print("[!] ERROR RETRIEVING HTTPS HEADERS [!]")
        pass


check_http()
check_https()