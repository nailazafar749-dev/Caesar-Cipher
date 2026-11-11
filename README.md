## Caesar Cipher: Basic Encryption & Decryption

## DecodeLabs | Cyber Security | Project 2 (Batch 2026)

A simple Python program that encrypts and decrypts text using the Caesar cipher. It demonstrates the basics of data confidentiality: turning readable text (plaintext) into unreadable text (ciphertext) and back again using a secret shift key.

**Features**
Encrypts user text with a shift key chosen by the user
Decrypts the encrypted text back to the original
Displays the original, encrypted and decrypted text
Handles edge cases: spaces, digits and punctuation stay unchanged
Preserves letter case (uppercase and lowercase)
Validates the result by checking that the decrypted text matches the original

**How It Works**
The program follows the IPO model:

**Stage	Description**
Input	Plaintext and a shift key entered by the user
Process	Caesar shift using ord(), chr() and % 26
Output	Ciphertext, then the decrypted text

**Encryption**: E(x) = (x + n) % 26 Decryption: D(x) = (x - n) % 26

where x is the letter position (A = 0 ... Z = 25) and n is the shift key.

The core of the logic in Python:

## python
chr((ord(char) - base + shift) % 26 + base)

base is 65 for uppercase letters and 97 for lowercase letters. The % 26 makes the alphabet wrap around, so Y shifted by 3 becomes B.

**Requirements**
Python 3.6 or higher (no external libraries needed)
Usage
python caesar_cipher.py
## Example
=== Caesar Cipher: Encryption & Decryption ===

Enter your text: FaizaKousar7
Enter shift key (e.g. 3): 9

--- Results ---
Original text  : FaizaKousar7
Encrypted text : OjrijTxdbja7
Decrypted text : FaizaKousar7

Validation: SUCCESS (decrypted text matches the original)

<img width="446" height="215" alt="image" src="https://github.com/user-attachments/assets/dea4831d-4d24-49a2-b793-585c843ea39c" />

**Security Note**

The Caesar cipher is for learning only and is not secure for real data:

Tiny key space: only 25 possible keys, so brute force is instant.
Pattern preservation: letter frequencies stay the same, so frequency analysis can break it.

Modern systems use algorithms such as AES (128-bit keys, confusion and diffusion).

Possible Improvements
Brute-force decryption that tries all 25 keys
Vigenère cipher for stronger encryption
