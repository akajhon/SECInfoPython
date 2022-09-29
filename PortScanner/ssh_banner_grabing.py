import socket

target = input("[+] Entre com o alvo: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.connect_ex((target, 22))
banner = sock.recv(2048).decode('utf-8')
banner.strip('b').strip('\n')
print("\n" + banner)
sock.close()
