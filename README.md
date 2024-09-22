A Python program that decrypts messages encrypted with classical ciphers like Caesar cipher, substitution cipher, and Vigenère cipher. This tool uses techniques such as frequency analysis to attempt decryption, making it a valuable resource for educational purposes and cryptography enthusiasts.

## Features
Caesar Cipher Decryption:

Automatically tries all possible shifts.
Selects the best shift based on English letter frequency analysis.
Substitution Cipher Decryption:

Utilizes frequency analysis to guess the mapping between cipher letters and plain letters.
Provides a basic decryption which may require further refinement for complex texts.
Vigenère Cipher Decryption:

Decrypts the text using a user-provided key.
Handles texts with mixed cases and non-alphabetic characters.

## Usage
Run the Program:
Choose a decryption method by entering the corresponding number:

1. Decrypt Caesar Cipher
2. Decrypt Substitution Cipher (Frequency Analysis)
3. Decrypt Vigenère Cipher

4. 
Enter the Ciphertext:

Paste or type the encrypted message you wish to decrypt.

For Vigenère Cipher:
If you selected option 3, you'll be prompted to enter the key used for encryption.

View the Decrypted Text:
The program will display the decrypted message based on the selected method.
