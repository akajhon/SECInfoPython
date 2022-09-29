import dns.resolver
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers= ['8.8.8.8']
dns_records = ["AAAA", "A", "CNAME", "SOA", "NS", "SPF", "SRV", "MX", "TXT", "PTR"]
domain = input("[+] Entre com o Alvo: ")


for record in dns_records:
    result = dns.resolver.resolve(domain, record, raise_on_no_answer=False)
    if result.rrset is not None:
        print(f"[+] {result.rrset}")
