def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine the appropriate case (uppercase or lowercase)
            start = ord('A') if char.isupper() else ord('a')
            # Apply the shift and wrap around if necessary
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

def main():
    message = input("Enter the message to encrypt or decrypt: ")
    shift = int(input("Enter the shift value (positive integer): "))
    choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()

    if choice == 'E':
        result = encrypt(message, shift)
        print("Encrypted message:", result)
    elif choice == 'D':
        result = decrypt(message, shift)
        print("Decrypted message:", result)
    else:
        print("Invalid choice. Please enter 'E' or 'D'.")

if __name__ == "__main__":
    main()
