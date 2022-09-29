import nmap

nmap_scan = nmap.PortScanner()
nmap_scan.scan("8.8.8.8", "21-80")

for host in nmap_scan.all_hosts():
    print(f"[!] Host: {host}\t{nmap_scan[host].hostname()}")
    print(f"[*] State: {nmap_scan[host].state()}")
    for protocol in nmap_scan[host].all_protocols():
        print("+-----------+")
        print(f"[+] Protocol: {protocol}")

        ports = nmap_scan[host][protocol].keys()

        for port in ports:
            print(f"[+] Port: {port}\tState: {nmap_scan[host][protocol][port]['state']}")
