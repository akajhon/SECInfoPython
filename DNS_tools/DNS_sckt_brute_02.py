import socket

domain = input("[+] Entre com o Alvo: ")
with open("subdomain_list", "r") as f:
    subdomain = f.readlines()
    f.close()

for name in subdomain:
    dns = name.strip("\n") + "." + domain
    try:
        print(f"[+] {dns} : {socket.gethostbyname(dns)}") #Esta funcao do socket retorna o IP do domínio
    except socket.gaierror:
        pass