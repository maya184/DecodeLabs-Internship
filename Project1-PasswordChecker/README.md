# Project 1: Password Strength Checker
**DecodeLabs Industrial Training Kit — Cyber Security Track**

## Goal
Ek Python program banaya gaya hai jo user ke diye gaye password ko
**Weak**, **Medium**, ya **Strong** ke tor par classify karta hai,
security best practices ke mutabiq.

## Requirements Fulfilled
- ✅ **Length Check** — 8 characters se kam password turant Weak count hota hai
- ✅ **Character Variety Check** — uppercase, lowercase, numbers, aur symbols
  ki maujoodgi check ki jati hai
- ✅ **Result Display** — final strength (Weak/Medium/Strong) aur detailed
  feedback screen par dikhaya jata hai
- ✅ **Bonus Feature** — common/leaked passwords ki ek list ke khilaf check
  (jaise "123456", "password", "qwerty") — agar password is list mein ho
  to turant Weak declare hota hai, chahe wo lamba kyun na ho

## How Scoring Works
1. Agar password kisi known leaked-password list mein ho → **Weak** (turant)
2. Agar length 8 se kam ho → **Weak**
3. Agar length 12+ ho AND sab 4 character types (upper/lower/digit/symbol)
   maujood hon → **Strong**
4. Agar length 8+ ho AND kam se kam 3 character types maujood hon → **Medium**
5. Baaki tamam cases → **Weak**

## Key Skills Demonstrated
- **String handling**: `.islower()`, `.isupper()`, `.isdigit()`, `.isalnum()`
  jaise built-in string methods ka istemal
- **Condition checks**: nested if/elif logic strength decide karne ke liye
- **Security basics**: common password blacklist, aur Pythonic/efficient
  code (`any()` ka istemal manual loops ki bajaye — jaisa slides mein
  recommend kiya gaya tha)

## How to Run
```
python3 password_strength_checker.py
```
Phir jo bhi password check karna ho wo type karein aur Enter dabayein.
Program exit karne ke liye `exit` type karein.

## Example Outputs
| Password | Strength | Reason |
|---|---|---|
| `123` | Weak | Bahut chota, koi variety nahi |
| `password1` | Weak | Common/leaked password list mein maujood |
| `Hello123` | Medium | 8+ length, lekin symbol missing |
| `Urwah@121202` | Strong | 12+ length, uppercase + lowercase + digit + symbol sab maujood |

## Notes on Advanced Concepts (from training material)
Slides mein do advanced security concepts bhi mention kiye gaye the jo is
project (Password *Strength* Checker) ka direct hissa nahi hain, balke
**Project 2 (Hashing & Encryption)** ke liye relevant hain:
- **Timing attacks**: password *comparison* (jaise login verification) ke
  waqt `hmac.compare_digest()` use karna chahiye, normal `==` ki bajaye,
  taake attacker response-time se password guess na kar sake.
- **RAM/memory persistence**: Python strings immutable hote hain, isliye
  password memory mein tab tak reh sakta hai jab tak garbage collection na
  ho — ye hashing/encryption phase mein zyada relevant hota hai.

Ye dono concepts is project mein implement nahi kiye gaye kyunke yahan
sirf *strength evaluation* karni thi, koi stored password se *comparison*
nahi ho raha.
