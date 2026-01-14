import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        self.root.config(bg="#f0f0f0")

        # Title
        tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=10)

        # Length Selection
        tk.Label(root, text="Password Length:", bg="#f0f0f0").pack(pady=5)
        self.length_var = tk.IntVar(value=12)
        tk.Spinbox(root, from_=4, to=32, textvariable=self.length_var, width=5, font=("Arial", 12)).pack(pady=5)

        # Complexity Options
        self.use_upper = tk.BooleanVar(value=True)
        self.use_numbers = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)

        options_frame = tk.Frame(root, bg="#f0f0f0")
        options_frame.pack(pady=5)
        tk.Checkbutton(options_frame, text="A-Z", variable=self.use_upper, bg="#f0f0f0").pack(side=tk.LEFT, padx=5)
        tk.Checkbutton(options_frame, text="0-9", variable=self.use_numbers, bg="#f0f0f0").pack(side=tk.LEFT, padx=5)
        tk.Checkbutton(options_frame, text="@#$", variable=self.use_symbols, bg="#f0f0f0").pack(side=tk.LEFT, padx=5)

        # Generate Button
        tk.Button(root, text="Generate Password", command=self.generate_password, bg="#007bff", fg="white", font=("Arial", 10, "bold")).pack(pady=15)

        # Result Display
        self.password_entry = tk.Entry(root, font=("Courier", 14), width=24, justify="center")
        self.password_entry.pack(pady=5)

        # Copy Button
        tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard, bg="#28a745", fg="white").pack(pady=5)

    def generate_password(self):
        length = self.length_var.get()
        chars = string.ascii_lowercase
        if self.use_upper.get(): chars += string.ascii_uppercase
        if self.use_numbers.get(): chars += string.digits
        if self.use_symbols.get(): chars += string.punctuation

        if not chars:
            messagebox.showwarning("Error", "Select at least one character type.")
            return

        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()