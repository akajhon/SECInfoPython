import requests

session = requests.Session()
https = "https://"
target = input("[+] Entre com o alvo: ")
full_target = https + target
response = session.get(full_target)
cookies_dict = session.cookies.get_dict()
print(f"*** {full_target} ***")
for cookie_name, cookie_valor in cookies_dict.items():
    print(f"[+] {cookie_name} => {cookie_valor}")
print("----------------------")