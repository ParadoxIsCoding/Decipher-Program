import string
from collections import Counter
import itertools

ENGLISH_FREQ = {
    'E': 12.70,
    'T': 9.06,
    'A': 8.17,
    'O': 7.51,
    'I': 6.97,
    'N': 6.75,
    'S': 6.33,
    'H': 6.09,
    'R': 5.99,
    'D': 4.25,
    'L': 4.03,
    'C': 2.78,
    'U': 2.76,
    'M': 2.41,
    'W': 2.36,
    'F': 2.23,
    'G': 2.02,
    'Y': 1.97,
    'P': 1.93,
    'B': 1.49,
    'V': 0.98,
    'K': 0.77,
    'X': 0.15,
    'J': 0.15,
    'Q': 0.10,
    'Z': 0.07,
}

def caesar_decrypt(ciphertext):
    """Decrypts a Caesar cipher by trying all possible shifts."""
    ciphertext = ciphertext.upper()
    best_shift = 0
    max_score = float('-inf')
    decrypted_text = ''
    for shift in range(26):
        shifted_text = ''
        for char in ciphertext:
            if char in string.ascii_uppercase:
                shifted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                shifted_text += shifted_char
            else:
                shifted_text += char
        score = score_text(shifted_text)
        if score > max_score:
            max_score = score
            best_shift = shift
            decrypted_text = shifted_text
    return decrypted_text

def substitution_decrypt(ciphertext):

    ciphertext = ciphertext.upper()
    cipher_freq = Counter(c for c in ciphertext if c in string.ascii_uppercase)
    cipher_letters = [item[0] for item in cipher_freq.most_common()]
    english_letters = [item[0] for item in sorted(ENGLISH_FREQ.items(), key=lambda x: x[1], reverse=True)]
    mapping = dict(zip(cipher_letters, english_letters))

    decrypted_text = ''
    for char in ciphertext:
        if char in string.ascii_uppercase:
            decrypted_text += mapping.get(char, char)
        else:
            decrypted_text += char
    return decrypted_text

def vigenere_decrypt(ciphertext, key):
    
    ciphertext = ciphertext.upper()
    key = key.upper()
    key_length = len(key)
    decrypted_text = ''
    for i, char in enumerate(ciphertext):
        if char in string.ascii_uppercase:
            shift = ord(key[i % key_length]) - ord('A')
            shifted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

def score_text(text):
   
    text = text.upper()
    total_letters = sum(c.isalpha() for c in text)
    if total_letters == 0:
        return float('-inf')
    letter_counts = Counter(c for c in text if c.isalpha())
    score = 0
    for letter in string.ascii_uppercase:
        observed_freq = (letter_counts.get(letter, 0) / total_letters) * 100
        expected_freq = ENGLISH_FREQ.get(letter, 0)
        score += (observed_freq - expected_freq) ** 2
    return -score  

def main():
    print("Advanced Decipher Program")
    print("1. Decrypt Caesar Cipher")
    print("2. Decrypt Substitution Cipher (Frequency Analysis)")
    print("3. Decrypt Vigenère Cipher")
    choice = input("Select an option (1-3): ")
    if choice not in {'1', '2', '3'}:
        print("Invalid choice.")
        return

    ciphertext = input("Enter the ciphertext: ")

    if choice == '1':
        plaintext = caesar_decrypt(ciphertext)
        print("\nDecrypted Text (Caesar Cipher):")
        print(plaintext)
    elif choice == '2':
        plaintext = substitution_decrypt(ciphertext)
        print("\nDecrypted Text (Substitution Cipher):")
        print(plaintext)
    elif choice == '3':
        key = input("Enter the key: ")
        plaintext = vigenere_decrypt(ciphertext, key)
        print("\nDecrypted Text (Vigenère Cipher):")
        print(plaintext)

if __name__ == "__main__":
    main()
