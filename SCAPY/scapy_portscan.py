from scapy.all import *

target = input("[+] Entre com o alvo: ")
ports = [22, 80, 443, 53, 21, 23, 25, 8080, 465, 993, 995]
target_packet = IP(dst = target)
tcp_packet = TCP(dport=ports, flags="S")
packet = target_packet/ tcp_packet
ans, unans = sr(packet, inter=0.1, timeout=1)
print("Porta -> Estado")
for received_packet in ans:
    print(received_packet[1][IP].sport, \
    "\t", received_packet[1][TCP].sprintf("%flags%"))