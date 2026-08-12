# Phishing Triage Toolkit

## Description
A Python-based tool that analyzes an email or message and classifies it as
**Safe**, **Suspicious**, or **Malicious** by detecting common phishing red
flags — urgency language, authority impersonation, sensitive info requests,
lookalike/spoofed domains, sender-domain mismatches, and dangerous
attachments. Built as part of the DecodeLabs Cyber Security Internship —
Project 3 (Phishing Awareness Analysis).

## Red Flag Checklist
Use this checklist manually on any email/message that feels suspicious:
- [ ] Sender-domain mismatch — display name looks trusted, but the actual
  email address doesn't match the real company domain
- [ ] Urgency or fear language — "act now", "account will be locked",
  "immediate action required"
- [ ] Authority impersonation — claims to be from IT, HR, the CEO, or law
  enforcement, demanding compliance
- [ ] Requests for sensitive info — passwords, OTP/MFA codes, bank details,
  or payment information
- [ ] Suspicious or lookalike links — misspelled domains (amaz0n.com), extra
  words (yourcompany-secure-login.com), or long nested subdomains
- [ ] Unexpected attachments — especially .exe, .scr, .js, .iso, or .zip
  files you weren't expecting
- [ ] Generic or awkward greetings — "Dear Customer" instead of your actual
  name, poor grammar, or odd phrasing
- [ ] Unsolicited QR codes — asking you to scan a code "to secure your
  account"
- [ ] MFA fatigue — multiple unexpected login-approval prompts in a row
- [ ] Requests to bypass normal procedure — "keep this confidential",
  "don't verify with anyone else"
- [ ] Too-good-to-be-true offers — prize winnings, unexpected refunds,
  surprise bonuses

## Decision Tree
| Verdict | Criteria | Action |
|---|---|---|
| **Safe** | No red flags found. Sender is verified, no unusual requests or links. | Close — no further action needed. |
| **Suspicious** | One or more soft red flags: urgency language, odd greeting, unexpected sender — but nothing overtly malicious. | Warn User — advise caution, do not click links or reply. Verify via a separate channel. |
| **Malicious** | Critical red flags: sender-domain mismatch, dangerous attachment, lookalike domain, or direct request for credentials/payment. | Block & Escalate — report to IT/Security immediately. Do not interact further. |

## The Golden Rule
1. **Pause** — Recognize the emotional trigger (urgency, fear, authority) and stop interacting with the message.
2. **Verify** — Confirm the request through a separate, trusted channel (e.g. a phone call to a known number).
3. **Report** — Use your organization's reporting process. Don't just delete it — reporting helps protect others too.

## How to Run
1. Make sure Python 3 is installed on your system.
2. Download `phishing_triage_tool.py` to your computer.
3. Open a terminal/command prompt in the folder containing the file.
4. Run:
   ```
   python3 phishing_triage_tool.py
   ```
5. When prompted:
   - Paste or type the message text you want to analyze
   - Optionally enter the sender's email address
   - Optionally enter an attachment filename (e.g. `invoice.exe`)
6. The tool will print a **Verdict** (Safe / Suspicious / Malicious), a
   **Recommended Action**, and a list of the specific **Red Flags** it found.
7. Type `exit` at any prompt to quit the program.

## Example
```
Enter message text (or 'exit' to quit): URGENT: Your account will be suspended in 24 hours. Click here to verify immediately.
Enter sender email (optional, press Enter to skip): support@paypa1-secure.com
Enter attachment filename (optional, press Enter to skip):

--- Triage Report ---
Verdict        : Malicious
Recommended Action: Block & Escalate to IT/Security team
Red Flags Found:
  - Urgency/fear language detected: urgent, 24 hours, verify immediately, suspended
  - Sender domain mismatch: message references 'paypal' but sender is 'support@paypa1-secure.com'
----------------------
```

## Tech Stack
- Python 3 (standard library only — uses `re` for pattern matching, no
  external dependencies)

## Author
Built as part of the DecodeLabs Cyber Security Internship — Project 3.
