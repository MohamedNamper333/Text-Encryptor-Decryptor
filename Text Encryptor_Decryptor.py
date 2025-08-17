import base64

def encrypt(text):
    encoded = base64.b64encode(text.encode())
    return encoded.decode()

def decrypt(encoded_text):
    decoded = base64.b64decode(encoded_text.encode())
    return decoded.decode()

choice = input("Encrypt or Decrypt? (e/d): ").lower()
if choice == "e":
    text = input("Enter text to encrypt: ")
    print(f"Encrypted: {encrypt(text)}")
elif choice == "d":
    encoded_text = input("Enter text to decrypt: ")
    print(f"Decrypted: {decrypt(encoded_text)}")
else:
    print("Invalid choice.")