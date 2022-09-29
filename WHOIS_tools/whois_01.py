import whois
domain = input("[+] Entre com o Alvo: ")
print("\n+-------------------+")
whois_query = whois.whois(domain)
print(whois_query.text)
