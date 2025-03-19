def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift  # Reverse the shift for decryption
    
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - ord('a') + shift_amount) % 26) + ord('a'))
            if char.isupper():
                new_char = new_char.upper()
            result += new_char
        else:
            result += char  # Keep spaces and punctuation unchanged
    
    return result

if __name__ == "__main__":
    choice = input("Do you want to encrypt or decrypt? (e/d): ").strip().lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    
    if choice == 'e':
        encrypted_message = caesar_cipher(message, shift, mode='encrypt')
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == 'd':
        decrypted_message = caesar_cipher(message, shift, mode='decrypt')
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice! Please enter 'e' for encryption or 'd' for decryption.")
