import hashlib

stored_username = "admin"

stored_password_hash = hashlib.sha256(
    "admin123".encode()
).hexdigest()

username = input("Enter Username: ")
password = input("Enter Password: ")

entered_hash = hashlib.sha256(
    password.encode()
).hexdigest()

if username == stored_username and entered_hash == stored_password_hash:
    print("Login Successful")
else:
    print("Access Denied")