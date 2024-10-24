import random

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime_number(lower, upper):
    """Generate a prime number between lower and upper bounds."""
    while True:
        num = random.randint(lower, upper)
        if is_prime(num):
            return num

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """Calculate the modular inverse of e mod phi using the Extended Euclidean Algorithm."""
    m0, x0, x1 = phi, 0, 1
    if phi == 1:
        return 0
    while e > 1:
        # q is quotient
        q = e // phi
        m, phi = phi, e % phi
        e = m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def generate_keypair():
    """Generate a pair of RSA keys (public and private)."""
    p = generate_prime_number(100, 200)  # Generate a random prime p
    q = generate_prime_number(100, 200)  # Generate a random prime q
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Calculate d
    d = mod_inverse(e, phi)

    return (e, n), (d, n)  # Public key and private key

def encrypt(public_key, plaintext):
    """Encrypt the plaintext using the public key."""
    e, n = public_key
    # Convert each character to its ASCII value, encrypt, and convert back to characters
    encrypted = [(pow(ord(char), e, n)) for char in plaintext]
    return encrypted

def decrypt(private_key, ciphertext):
    """Decrypt the ciphertext using the private key."""
    d, n = private_key
    # Decrypt each number back to characters
    decrypted = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted

def main():
    while True:
        print("\nRSA Cipher Menu:")
        print("1. Generate RSA Keypair")
        print("2. Encrypt a message")
        print("3. Decrypt a message")
        print("4. Exit")

        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            public_key, private_key = generate_keypair()
            print("Public Key:", public_key)
            print("Private Key:", private_key)

        elif choice == '2':
            plaintext = input("Enter the plaintext: ")
            ciphertext = encrypt(public_key, plaintext)
            print("Ciphertext:", ciphertext)

        elif choice == '3':
            ciphertext = input("Enter the ciphertext (comma-separated numbers): ")
            ciphertext = list(map(int, ciphertext.split(',')))
            decrypted_text = decrypt(private_key, ciphertext)
            print("Decrypted Text:", decrypted_text)

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
