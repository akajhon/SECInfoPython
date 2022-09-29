import requests
import re

def grabEmailfromSite(site):
    site_content = requests.get(site)
    regex = re.findall("[\w\.-]+@[\w\.-]+\.\w+", site_content.text)
    if regex:
        return(list(set(regex)))
    else:
        return None

temp = 0

try:
    with open("urllist.txt", "r") as f:
        urls = f.readlines()
        f.close()
    for sites in urls:
        sites = sites.strip('\n')
        emails = (grabEmailfromSite(sites))
        if emails != "None" or emails != None:
            print(f"[!] {sites} [!]")
            print(f"[+] {emails}")
            print("*"*30+"\n")
        temp += 1
except Exception as err:
    print(err)
    pass