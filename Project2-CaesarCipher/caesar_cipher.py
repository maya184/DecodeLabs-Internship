"""
DecodeLabs Cyber Security - Project 2
Basic Encryption & Decryption (Caesar Cipher)

Goal: Implement a simple, reversible encryption technique.
This program encrypts user text using a Caesar Cipher (shift-based
substitution) and can decrypt it back to the original message.

Key Skills demonstrated: encryption concepts, logic building,
data protection basics.
"""

ALPHABET_SIZE = 26


def encrypt(text: str, shift: int) -> str:
    """
    Encrypt text using a Caesar Cipher.
    Formula: E(x) = (x + shift) % 26

    Only letters are shifted. Spaces, numbers, and punctuation
    are left unchanged (as noted in the training material's
    'edge case handling' requirement).
    """
    result = []

    for char in text:
        if char.isupper():
            # Convert to 0-25 range, shift, wrap with %26, convert back
            shifted = (ord(char) - ord('A') + shift) % ALPHABET_SIZE
            result.append(chr(shifted + ord('A')))
        elif char.islower():
            shifted = (ord(char) - ord('a') + shift) % ALPHABET_SIZE
            result.append(chr(shifted + ord('a')))
        else:
            # Non-letters (spaces, digits, punctuation) stay the same
            result.append(char)

    return "".join(result)


def decrypt(ciphertext: str, shift: int) -> str:
    """
    Decrypt Caesar Cipher text.
    Formula: D(x) = (x - shift) % 26

    Decryption is simply encryption with the negative shift,
    since Caesar Cipher is symmetric (same key locks and unlocks).
    """
    return encrypt(ciphertext, -shift)


def main():
    print("=== DecodeLabs Caesar Cipher: Encryption & Decryption ===\n")

    while True:
        message = input("Enter text to encrypt (or 'exit' to quit): ")
        if message.lower() == "exit":
            print("Goodbye!")
            break
        if message == "":
            print("Please enter some text.\n")
            continue

        # Get and validate the shift key
        while True:
            shift_input = input("Enter shift key (an integer, e.g. 3): ")
            try:
                shift = int(shift_input)
                break
            except ValueError:
                print("Please enter a valid whole number for the shift key.")

        encrypted_text = encrypt(message, shift)
        decrypted_text = decrypt(encrypted_text, shift)

        print("\n--- Result ---")
        print(f"Original Text : {message}")
        print(f"Shift Key     : {shift}")
        print(f"Encrypted     : {encrypted_text}")
        print(f"Decrypted     : {decrypted_text}")
        print(f"Match Check   : {'PASS' if decrypted_text == message else 'FAIL'}")
        print("--------------\n")


if __name__ == "__main__":
    main()
