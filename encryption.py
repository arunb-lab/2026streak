def encrypt(text, shift):
    """Encrypt text using Caesar cipher"""
    result = ""
    
    for char in text:
        if char.isalpha():
            # Get the ASCII value
            ascii_offset = 65 if char.isupper() else 97
            # Shift the character and wrap around using modulo
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += encrypted_char
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result

def decrypt(text, shift):
    """Decrypt text using Caesar cipher"""
    # Decryption is just encryption with negative shift
    return encrypt(text, -shift)

# Main program
if __name__ == "__main__":
    print("=== Caesar Cipher Encryption ===\n")
    
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (1-25): "))
    
    if choice == 'E':
        encrypted = encrypt(message, shift)
        print(f"\nEncrypted message: {encrypted}")
    elif choice == 'D':
        decrypted = decrypt(message, shift)
        print(f"\nDecrypted message: {decrypted}")
    else:
        print("Invalid choice!")
        
    # Example usage
    print("\n--- Example ---")
    original = "Hello World!"
    shift_value = 3
    enc = encrypt(original, shift_value)
    dec = decrypt(enc, shift_value)
    print(f"Original: {original}")
    print(f"Encrypted (shift {shift_value}): {enc}")
    print(f"Decrypted: {dec}")