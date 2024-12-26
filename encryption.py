import tkinter as tk
from tkinter import messagebox
import random
import string
from cryptography.fernet import Fernet

# Function to generate a random password
def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to encrypt the password
def encrypt_password():
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "No password to encrypt!")
        return

    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())

    encryption_key_entry.delete(0, tk.END)
    encryption_key_entry.insert(0, key.decode())

    encrypted_password_entry.delete(0, tk.END)
    encrypted_password_entry.insert(0, encrypted_password.decode())

# Create the main application window
app = tk.Tk()
app.title("Password Generator & Encryptor")
app.geometry("500x400")

# Length label and entry
length_label = tk.Label(app, text="Password Length:")
length_label.pack(pady=5)
length_entry = tk.Entry(app)
length_entry.pack(pady=5)

# Generate button
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Password label and entry
password_label = tk.Label(app, text="Generated Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(app, width=50)
password_entry.pack(pady=5)

# Encrypt button
encrypt_button = tk.Button(app, text="Encrypt Password", command=encrypt_password)
encrypt_button.pack(pady=10)

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

# Run the application
app.mainloop()
