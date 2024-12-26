import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

# Function to decrypt the password
def decrypt_password():
    encrypted_password = encrypted_password_entry.get()
    encryption_key = encryption_key_entry.get()

    if not encrypted_password or not encryption_key:
        messagebox.showerror("Error", "Both encrypted password and key are required!")
        return

    try:
        cipher_suite = Fernet(encryption_key.encode())
        decrypted_password = cipher_suite.decrypt(encrypted_password.encode()).decode()
        decrypted_password_entry.delete(0, tk.END)
        decrypted_password_entry.insert(0, decrypted_password)
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {str(e)}")

# Create the main application window
app = tk.Tk()
app.title("Password Decryptor")
app.geometry("500x300")

# Encrypted password label and entry
encrypted_password_label = tk.Label(app, text="Encrypted Password:")
encrypted_password_label.pack(pady=5)
encrypted_password_entry = tk.Entry(app, width=50)
encrypted_password_entry.pack(pady=5)

# Encryption key label and entry
encryption_key_label = tk.Label(app, text="Encryption Key:")
encryption_key_label.pack(pady=5)
encryption_key_entry = tk.Entry(app, width=50)
encryption_key_entry.pack(pady=5)

# Decrypt button
decrypt_button = tk.Button(app, text="Decrypt Password", command=decrypt_password)
decrypt_button.pack(pady=10)

# Decrypted password label and entry
decrypted_password_label = tk.Label(app, text="Decrypted Password:")
decrypted_password_label.pack(pady=5)
decrypted_password_entry = tk.Entry(app, width=50)
decrypted_password_entry.pack(pady=5)

# Run the application
app.mainloop()
