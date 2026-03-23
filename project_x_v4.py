import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from fpdf import FPDF

# --- CORE: Secure Key Generation ---
def generate_secure_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# --- MODULE: Deceptive Encryption ---
def create_stealth_pdf(filename, payload):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Courier", 'B', 14)
    pdf.cell(200, 10, txt="CLASSIFIED DATA: EYES ONLY", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Courier", size=8)
    pdf.multi_cell(190, 5, txt=payload)
    pdf.output(filename)

def main_system():
    print("\n" + "="*50)
    print("      SYSTEM-X: NATIONAL SECURITY INTERFACE      ")
    print("="*50)
    print("1. DEPLOY: Encrypt with Deniable Decoy")
    print("2. RETRIEVE: Decrypt with Master/Fake Key")
    
    cmd = input("\nEnter Command (1/2): ")
    
    if cmd == '1':
        real_msg = input("REAL SECRET: ")
        fake_msg = input("DECOY MESSAGE: ")
        real_pass = input("MASTER PASSWORD: ")
        fake_pass = input("DECOY PASSWORD: ")
        
        salt = os.urandom(16)
        s_b64 = base64.b64encode(salt).decode()
        
        t_real = Fernet(generate_secure_key(real_pass, salt)).encrypt(real_msg.encode()).decode()
        t_fake = Fernet(generate_secure_key(fake_pass, salt)).encrypt(fake_msg.encode()).decode()
        
        payload = f"{s_b64}:{t_real}:{t_fake}"
        fname = input("Target PDF Name (e.g., intel.pdf): ")
        create_stealth_pdf(fname, payload)
        print(f"\n[SUCCESS] Stealth PDF '{fname}' generated.")

    elif cmd == '2':
        payload_in = input("PASTE ENCRYPTED STRING: ")
        pwd = input("ENTER AUTHENTICATION KEY: ")
        
        try:
            s_b64, tr, tf = payload_in.split(":")
            salt = base64.b64decode(s_b64)
            f = Fernet(generate_secure_key(pwd, salt))
            
            try:
                # Attempt Master Decryption
                print(f"\n[MASTER ACCESS] Message: {f.decrypt(tr.encode()).decode()}")
            except:
                # Attempt Decoy Decryption
                print(f"\n[DECOY ACCESS] Message: {f.decrypt(tf.encode()).decode()}")
        except:
            print("\n[ALARM] Authentication Failure! Trace initiated.")

if __name__ == "__main__":
    main_system()