# Project X: Advanced Deniable Encryption Interface 🛡️

### **Overview**
Project X is a specialized security tool designed for **Plausible Deniability**. In high-stakes environments, standard encryption can be a liability if a user is forced to reveal a password. This system solves that by allowing two different messages (Real vs. Decoy) to be stored in a single encrypted payload, protected by separate keys.

### **Key Technical Features**
- **Deniable Cryptography:** Supports **Master Access** (Real Secret) and **Decoy Access** (Fake Message).
- **Hardened Key Derivation:** Utilizes **PBKDF2HMAC** with SHA-256 and 480,000 iterations for brute-force resistance.
- **Payload Structure:** Uses **Fernet (AES-128)** encryption for data integrity and confidentiality.
- **Stealth PDF Generation:** Encrypted data is exported into a standard PDF format to avoid suspicion during transit.
- **Intrusion Detection:** Includes an automated alarm system for unauthorized authentication attempts.

### **How To Use**
1. **Selection 1 (Deployment):** Enter your Real Secret and a Decoy message. Set two different passwords.
2. **PDF Creation:** The tool generates a PDF containing the encrypted string.
3. **Selection 2 (Retrieval):** Paste the encrypted string from the PDF. 
   - Enter **Master Password** -> Reveals Real Secret.
   - Enter **Decoy Password** -> Reveals Fake Message.
   - Enter **Wrong Password** -> Triggers [ALARM].

### **Tech Stack**
- **Language:** Python 3.x
- **Encryption:** Cryptography (Fernet)
- **Document Generation:** FPDF
