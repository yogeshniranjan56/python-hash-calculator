import hashlib

file_path = input("Enter file path: ")

try:
    with open(file_path, "rb") as file:
        data = file.read()

    print("\nFile Hashes")
    print("--------------------------------")

    print("MD5    :", hashlib.md5(data).hexdigest())
    print("SHA1   :", hashlib.sha1(data).hexdigest())
    print("SHA256 :", hashlib.sha256(data).hexdigest())

except FileNotFoundError:
    print("File Not Found")
    input("\nPress Enter to Exit...")