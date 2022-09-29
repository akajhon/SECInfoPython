import dns.resolver
dns_records = ["AAAA", "A", "CNAME", "SOA", "NS", "SRV", "MX", "TXT", "PTR"]
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
nameserver = input("[+] Defina o Servidor que resolverá o DNS: ")
dns.resolver.default_resolver.nameservers= [nameserver]

domain = input("[+] Entre com o Alvo: ")
print("\n+-------------------+")

a_record_query = dns.resolver.resolve(domain, 'A')
for ip in a_record_query:
    target_ip = ip.to_text()

for record in dns_records:
    try:
        if record == 'CNAME':
            result = dns.resolver.resolve(domain, 'CNAME')
            for cname_record in result:
                print(f"[+] CNAME: {cname_record.target}")
            print("+-------------------+")
        elif record == 'PTR':
            result = dns.resolver.resolve(target_ip + '.in-addr.arpa', 'PTR')
            for ptr_record in result:
                print(f"[+] PTR: {ptr_record.to_text()}")
            print("+-------------------+")
        else:
            record_query = dns.resolver.resolve(domain, record)
            for results in record_query:
                print(f"[+] {record}: {results.to_text()}")
            print("+-------------------+")
    except:
        pass