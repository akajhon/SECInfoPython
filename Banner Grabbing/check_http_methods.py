import requests

http = "http://"
target = input("[+] Entre com o alvo: ")
http_target = http + target

methods = ["GET", "POST", "OPTIONS", "PUT", "DELETE", "TRACE", "CONNECT", "HEAD", "PATCH"]

for method in methods:
    try:
        answer = requests.request(method, http_target)
        print(method +" |--> " + answer.reason)
    except:
        pass
