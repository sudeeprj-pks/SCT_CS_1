# Caesar Cipher Encryption and Decryption

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Check if it's a letter
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# --- Main Program ---
print("=== Caesar Cipher Program ===")
message = input("Enter your message: ")
shift = int(input("Enter shift value (e.g., 3): "))

print("\n--- Results ---")
encrypted = encrypt(message, shift)
print(f"Encrypted Message: {encrypted}")

decrypted = decrypt(encrypted, shift)
print(f"Decrypted Message: {decrypted}")
