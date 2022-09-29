from scapy.all import *
from scapy.layers.l2 import Ether, ARP

IPs=[]
for ip in range (100, 200):
    IPs.append("10.210.23." + str(ip))
arp_packet = Ether()/ARP(pdst=IPs, hwdst="5c:cd:5b:4d:47:f7")
ans, unans = sr(arp_packet, inter=0.1, timeout=1)
print("IP\t\tMAC")
for received_packet in ans:
    print(received_packet[1].psrc, "\t", received_packet[1].hwsrc)
