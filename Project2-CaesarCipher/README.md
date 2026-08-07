# Caesar Cipher — Encryption & Decryption Tool

## Description
A Python program that encrypts and decrypts text using the **Caesar Cipher**
technique — a classic shift-based substitution cipher. The user provides a
message and a shift key; the program encrypts the message, then decrypts it
back to verify correctness.

Key features:
- Encrypts alphabetic characters using a shift-based formula (`(x + shift) % 26`)
- Decrypts ciphertext back to the original message
- Preserves spaces, numbers, and punctuation (only letters are shifted)
- Supports any integer shift value, including large numbers and negative shifts
- Includes a built-in match check to confirm decryption returns the original text

## How to Run
1. Make sure Python 3 is installed on your system.
2. Download `caesar_cipher.py` to your computer.
3. Open a terminal/command prompt in the folder containing the file.
4. Run:
   ```
   python3 caesar_cipher.py
   ```
5. When prompted, enter the text you want to encrypt and an integer shift key.
6. The program will display the original text, the encrypted text, the
   decrypted text, and confirm whether they match.
7. Type `exit` at any prompt to quit the program.

## Example
```
Enter text to encrypt (or 'exit' to quit): Hello World
Enter shift key (an integer, e.g. 3): 3

--- Result ---
Original Text : Hello World
Shift Key     : 3
Encrypted     : Khoor Zruog
Decrypted     : Hello World
Match Check   : PASS
```

## Tech Stack
- Python 3 (standard library only, no external dependencies)

## Author
Built as part of the DecodeLabs Cyber Security Internship — Project 2.
