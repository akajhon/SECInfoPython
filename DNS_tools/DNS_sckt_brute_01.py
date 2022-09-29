import socket

domain = input("[+] Entre com o Alvo: ")
sub_domain = ["ns1", "ns2", "ns3", "ns4", "www", "ftp", "intranet", "mail"]

for name in sub_domain:
    dns = name + "." + domain
    try:
        print(f"[+] {dns} : {socket.gethostbyname(dns)}") #Esta funcao do socket retorna o IP do domínio
    except socket.gaierror:
        pass