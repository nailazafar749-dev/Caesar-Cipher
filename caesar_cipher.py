"""
DecodeLabs - Cyber Security Project 2
Basic Encryption & Decryption (Caesar Cipher)

IPO Model:
    Input   -> Plaintext (user text) + shift key
    Process -> Caesar shift using ord(), chr(), % 26
    Output  -> Ciphertext, then decrypted text for validation
"""


def shift_char(char, shift):
    """Shift a single character. Letters are shifted, everything else is kept as is."""
    if char.isupper():
        base = ord("A")          # 65
    elif char.islower():
        base = ord("a")          # 97
    else:
        return char              # spaces, digits, punctuation stay unchanged

    # subtract base -> add shift -> wrap with % 26 -> add base back
    return chr((ord(char) - base + shift) % 26 + base)


def encrypt(plaintext, shift):
    """E(x) = (x + n) % 26"""
    return "".join(shift_char(ch, shift) for ch in plaintext)


def decrypt(ciphertext, shift):
    """D(x) = (x - n) % 26"""
    return "".join(shift_char(ch, -shift) for ch in ciphertext)


def get_shift():
    """Ask the user for a valid integer shift key."""
    while True:
        try:
            return int(input("Enter shift key (e.g. 3): "))
        except ValueError:
            print("Please enter a whole number.")


def main():
    print("=== Caesar Cipher: Encryption & Decryption ===\n")

    plaintext = input("Enter your text: ")
    shift = get_shift()

    encrypted = encrypt(plaintext, shift)
    decrypted = decrypt(encrypted, shift)

    print("\n--- Results ---")
    print(f"Original text  : {plaintext}")
    print(f"Encrypted text : {encrypted}")
    print(f"Decrypted text : {decrypted}")

    # Validation step from the deliverables checklist
    if decrypted == plaintext:
        print("\nValidation: SUCCESS (decrypted text matches the original)")
    else:
        print("\nValidation: FAILED")


if __name__ == "__main__":
    main()
