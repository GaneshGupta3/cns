def create_playfair_matrix(keyword):
    # Prepare the keyword by removing duplicates and replacing 'J' with 'I'
    keyword = keyword.upper().replace('J', 'I')
    seen = set()
    matrix = []

    for char in keyword:
        if char not in seen and char.isalpha():
            seen.add(char)
            matrix.append(char)

    # Fill the matrix with the remaining letters of the alphabet
    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':  # Note 'J' is omitted
        if char not in seen:
            matrix.append(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]  # Create a 5x5 matrix


def prepare_plaintext(plaintext):
    # Convert to uppercase and replace J with I, then prepare digraphs
    plaintext = plaintext.upper().replace('J', 'I').replace(' ', '')
    digraphs = []

    i = 0
    while i < len(plaintext):
        char1 = plaintext[i]
        char2 = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'  # Add 'X' if single letter
        if char1 == char2:
            digraphs.append(char1 + 'X')  # Insert 'X' if both characters are the same
            i += 1
        else:
            digraphs.append(char1 + char2)
            i += 2

    return digraphs


def find_position(matrix, char):
    # Find the (row, col) position of the character in the matrix
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None


def playfair_encrypt(plaintext, keyword):
    matrix = create_playfair_matrix(keyword)
    digraphs = prepare_plaintext(plaintext)
    ciphertext = []

    for digraph in digraphs:
        row1, col1 = find_position(matrix, digraph[0])
        row2, col2 = find_position(matrix, digraph[1])

        if row1 == row2:  # Same row
            ciphertext.append(matrix[row1][(col1 + 1) % 5])
            ciphertext.append(matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:  # Same column
            ciphertext.append(matrix[(row1 + 1) % 5][col1])
            ciphertext.append(matrix[(row2 + 1) % 5][col2])
        else:  # Rectangle swap
            ciphertext.append(matrix[row1][col2])
            ciphertext.append(matrix[row2][col1])

    return ''.join(ciphertext)


def playfair_decrypt(ciphertext, keyword):
    matrix = create_playfair_matrix(keyword)
    digraphs = prepare_plaintext(ciphertext)
    decrypted_text = []

    for digraph in digraphs:
        row1, col1 = find_position(matrix, digraph[0])
        row2, col2 = find_position(matrix, digraph[1])

        if row1 == row2:  # Same row
            decrypted_text.append(matrix[row1][(col1 - 1) % 5])
            decrypted_text.append(matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:  # Same column
            decrypted_text.append(matrix[(row1 - 1) % 5][col1])
            decrypted_text.append(matrix[(row2 - 1) % 5][col2])
        else:  # Rectangle swap
            decrypted_text.append(matrix[row1][col2])
            decrypted_text.append(matrix[row2][col1])

    return ''.join(decrypted_text)


def main():
    while True:
        print("\nPlayfair Cipher Menu:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            plaintext = input("Enter the plaintext: ")
            keyword = input("Enter the keyword: ")
            ciphertext = playfair_encrypt(plaintext, keyword)
            print("Ciphertext:", ciphertext)

        elif choice == '2':
            ciphertext = input("Enter the ciphertext: ")
            keyword = input("Enter the keyword: ")
            decrypted_text = playfair_decrypt(ciphertext, keyword)
            print("Decrypted Text:", decrypted_text)

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main()