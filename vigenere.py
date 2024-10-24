def vigenere_encrypt(plaintext, keyword):
    encrypted_text = []
    # Repeat the keyword to match the length of the plaintext
    keyword_repeated = (keyword * (len(plaintext) // len(keyword))) + keyword[:len(plaintext) % len(keyword)]

    for p, k in zip(plaintext, keyword_repeated):
        if p.isalpha():  # Check if the character is alphabetic
            shift = ord(k.lower()) - ord('a')  # Calculate the shift based on the keyword
            if p.islower():  # Handle lowercase letters
                encrypted_text.append(chr((ord(p) - ord('a') + shift) % 26 + ord('a')))
            else:  # Handle uppercase letters
                encrypted_text.append(chr((ord(p) - ord('A') + shift) % 26 + ord('A')))
        else:
            encrypted_text.append(p)  # Non-alphabetic characters remain unchanged

    return ''.join(encrypted_text)  # Join the list into a string and return

def vigenere_decrypt(ciphertext, keyword):
    decrypted_text = []
    # Repeat the keyword to match the length of the ciphertext
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword))) + keyword[:len(ciphertext) % len(keyword)]

    for c, k in zip(ciphertext, keyword_repeated):
        if c.isalpha():  # Check if the character is alphabetic
            shift = ord(k.lower()) - ord('a')  # Calculate the shift based on the keyword
            if c.islower():  # Handle lowercase letters
                decrypted_text.append(chr((ord(c) - ord('a') - shift) % 26 + ord('a')))
            else:  # Handle uppercase letters
                decrypted_text.append(chr((ord(c) - ord('A') - shift) % 26 + ord('A')))
        else:
            decrypted_text.append(c)  # Non-alphabetic characters remain unchanged

    return ''.join(decrypted_text)  # Join the list into a string and return

def main():
    while True:
        print("\nVigenère Cipher Menu:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            plaintext = input("Enter the plaintext: ")
            keyword = input("Enter the keyword: ")
            ciphertext = vigenere_encrypt(plaintext, keyword)
            print("Ciphertext:", ciphertext)

        elif choice == '2':
            ciphertext = input("Enter the ciphertext: ")
            keyword = input("Enter the keyword: ")
            decrypted_text = vigenere_decrypt(ciphertext, keyword)
            print("Decrypted Text:", decrypted_text)

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main()