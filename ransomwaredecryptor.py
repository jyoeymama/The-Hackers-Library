import os
from cryptography.fernet import Fernet

# Check if the key exists
if not os.path.exists("thekey.key"):
    print("🔑 Decryption key not found! Decryption cannot proceed.")
    exit()

# Load the encryption key
with open("thekey.key", "rb") as key_file:
    key = key_file.read()

# Initialize Fernet with the key
cipher = Fernet(key)

# List all files in the current directory
files = []

for file in os.listdir():
    if file in ["decryptor.py", "thekey.key", "sigma.py"]:  # Exclude important files
        continue
    if os.path.isfile(file):
        files.append(file)

print("🔎 Found encrypted files:", files)

# Decrypt each file
for file in files:
    try:
        with open(file, "rb") as thefile:
            encrypted_contents = thefile.read()

        decrypted_contents = cipher.decrypt(encrypted_contents)

        with open(file, "wb") as thefile:
            thefile.write(decrypted_contents)

        print(f"✅ Successfully decrypted: {file}")

    except Exception as e:
        print(f"⚠️ Error decrypting {file}: {e}")

print("🎉 All files have been decrypted successfully!")
