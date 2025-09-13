# Bitwise operators demonstration

# Define two integers
a = 25  # Binary:  011001
b = 45  # Binary:  101101

# Bitwise AND (&)
result_and = a & b  # 001001 (Decimal: 9)
print("a & b:", result_and)

# Bitwise OR (|)
result_or = a | b  # 111101 (Decimal: 61)
print("a | b:", result_or)

# Bitwise XOR (^)
result_xor = a ^ b  # 110100 (Decimal: 52)
print("a ^ b:", result_xor)

# Bitwise NOT (~) - Two's complement representation
result_not_a = ~a  # - (a + 1) = -26
print("~a:", result_not_a)

# Left shift (<<) - Shifts bits left by 2 places (multiplies by 2^2)
result_left_shift = a << 2  # 1100100 (Decimal: 100)
print("a << 2:", result_left_shift)

# Right shift (>>) - Shifts bits right by 2 places (divides by 2^2)
result_right_shift = a >> 2  # 000110 (Decimal: 6)
print("a >> 2:", result_right_shift)

#Here's a small Python project that demonstrates the use of bitwise operators
#in a simple Encryption/Decryption program. This project uses bitwise operators
#to manipulate the data during the encryption and decryption process.

#Project: Simple XOR Encryption/Decryption
# Simple XOR encryption and decryption using bitwise operators

def encrypt_decrypt(data, key):
    """
    Encrypts or decrypts the given data using XOR bitwise operator.

    :param data: The data (string) to be encrypted or decrypted
    :param key: The key (integer) to be used for XOR operation
    :return: The encrypted or decrypted data (string)
    """
    encrypted_decrypted = ""
    for char in data:
        encrypted_decrypted += chr(ord(char) ^ key)  # XOR each character with the key
    return encrypted_decrypted


def main():
    # User input for data to encrypt and the key for encryption
    data = input("Enter the text to encrypt/decrypt: ")
    key = int(input("Enter the key (integer for XOR operation): "))

    # Encrypt the data
    encrypted_data = encrypt_decrypt(data, key)
    print(f"Encrypted data: {encrypted_data}")

    # Decrypt the data (same process as encryption because XOR is reversible)
    decrypted_data = encrypt_decrypt(encrypted_data, key)
    print(f"Decrypted data: {decrypted_data}")


if __name__ == "__main__":
    main()

#How it works:
#1.Encrypt/Decrypt Function:
#The encrypt_decrypt function takes the data (string) and a key (integer) as inputs.
#It loops over each character in the data and applies the XOR (^)
#bitwise operator to the ASCII value of the character and the key. This manipulates the bits of the data.
#The result is then converted back to a character and added to the output string.

#2.Encryption and Decryption:
#The same XOR operation is used for both encryption and decryption.
#This is because XOR is a reversible operation: applying the same XOR operation twice restores the original value.

#3.User Input:
#The program asks the user for a string of text and a key. It then encrypts the text and immediately decrypts it back to the original.
