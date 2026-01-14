import tkinter as tk
from tkinter import ttk, messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("700x450")
        self.root.config(bg="#f4f4f4")
        self.root.resizable(False, False)

        # Contact Storage (In-memory list of dictionaries)
        self.contacts = []

        # --- UI Layout ---
        
        # Title
        title_label = tk.Label(root, text="Contact Management System", font=("Arial", 18, "bold"), bg="#f4f4f4", fg="#333")
        title_label.pack(side=tk.TOP, fill=tk.X, pady=10)

        # Main Frame
        main_frame = tk.Frame(root, bg="#f4f4f4")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # --- Left Side: Input Form ---
        form_frame = tk.LabelFrame(main_frame, text="Contact Details", font=("Arial", 12), bg="#f4f4f4", bd=2)
        form_frame.place(x=10, y=10, width=300, height=350)

        tk.Label(form_frame, text="Name:", bg="#f4f4f4", font=("Arial", 10)).pack(anchor="w", padx=10, pady=2)
        self.entry_name = ttk.Entry(form_frame, width=30)
        self.entry_name.pack(padx=10, pady=2)

        tk.Label(form_frame, text="Phone:", bg="#f4f4f4", font=("Arial", 10)).pack(anchor="w", padx=10, pady=2)
        self.entry_phone = ttk.Entry(form_frame, width=30)
        self.entry_phone.pack(padx=10, pady=2)

        tk.Label(form_frame, text="Email:", bg="#f4f4f4", font=("Arial", 10)).pack(anchor="w", padx=10, pady=2)
        self.entry_email = ttk.Entry(form_frame, width=30)
        self.entry_email.pack(padx=10, pady=2)

        tk.Label(form_frame, text="Address:", bg="#f4f4f4", font=("Arial", 10)).pack(anchor="w", padx=10, pady=2)
        self.entry_address = ttk.Entry(form_frame, width=30)
        self.entry_address.pack(padx=10, pady=2)

        # Buttons Frame
        btn_frame = tk.Frame(form_frame, bg="#f4f4f4")
        btn_frame.pack(pady=20)

        self.btn_add = tk.Button(btn_frame, text="Add", command=self.add_contact, bg="#4CAF50", fg="white", width=10)
        self.btn_add.grid(row=0, column=0, padx=5, pady=5)

        self.btn_update = tk.Button(btn_frame, text="Update", command=self.update_contact, bg="#FF9800", fg="white", width=10)
        self.btn_update.grid(row=0, column=1, padx=5, pady=5)

        self.btn_delete = tk.Button(btn_frame, text="Delete", command=self.delete_contact, bg="#F44336", fg="white", width=10)
        self.btn_delete.grid(row=1, column=0, padx=5, pady=5)

        self.btn_clear = tk.Button(btn_frame, text="Clear", command=self.clear_fields, bg="#607D8B", fg="white", width=10)
        self.btn_clear.grid(row=1, column=1, padx=5, pady=5)

        # --- Right Side: List Display & Search ---
        list_frame = tk.Frame(main_frame, bg="#f4f4f4")
        list_frame.place(x=320, y=10, width=360, height=350)

        # Search Bar
        search_frame = tk.Frame(list_frame, bg="#f4f4f4")
        search_frame.pack(fill=tk.X)
        self.entry_search = ttk.Entry(search_frame)
        self.entry_search.pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Button(search_frame, text="Search", command=self.search_contact, bg="#2196F3", fg="white").pack(side=tk.LEFT, padx=5)

        # Treeview (Table)
        self.tree = ttk.Treeview(list_frame, columns=("Name", "Phone"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone Number")
        self.tree.column("Name", width=150)
        self.tree.column("Phone", width=150)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)

        # Bind click event
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if name and phone:
            self.contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
            self.update_list()
            self.clear_fields()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Input Error", "Name and Phone are required.")

    def update_list(self, data=None):
        # Clear current list
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        # Use provided data or all contacts
        dataset = data if data else self.contacts

        for contact in dataset:
            self.tree.insert("", tk.END, values=(contact["Name"], contact["Phone"]))

    def on_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            name = item['values'][0]
            phone = str(item['values'][1])

            # Find full details
            for contact in self.contacts:
                if contact["Name"] == name and contact["Phone"] == phone:
                    self.entry_name.delete(0, tk.END)
                    self.entry_name.insert(0, contact["Name"])
                    self.entry_phone.delete(0, tk.END)
                    self.entry_phone.insert(0, contact["Phone"])
                    self.entry_email.delete(0, tk.END)
                    self.entry_email.insert(0, contact["Email"])
                    self.entry_address.delete(0, tk.END)
                    self.entry_address.insert(0, contact["Address"])
                    break

    def update_contact(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a contact to update.")
            return
        
        # Get original data to find the index
        item = self.tree.item(selected_item)
        original_name = item['values'][0]
        
        for i, contact in enumerate(self.contacts):
            if contact["Name"] == original_name:
                self.contacts[i] = {
                    "Name": self.entry_name.get(),
                    "Phone": self.entry_phone.get(),
                    "Email": self.entry_email.get(),
                    "Address": self.entry_address.get()
                }
                self.update_list()
                self.clear_fields()
                messagebox.showinfo("Success", "Contact updated.")
                return

    def delete_contact(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a contact to delete.")
            return

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?")
        if confirm:
            item = self.tree.item(selected_item)
            original_name = item['values'][0]

            self.contacts = [c for c in self.contacts if c["Name"] != original_name]
            self.update_list()
            self.clear_fields()

    def search_contact(self):
        query = self.entry_search.get().lower()
        if query:
            filtered_data = [c for c in self.contacts if query in c["Name"].lower() or query in c["Phone"]]
            self.update_list(filtered_data)
        else:
            self.update_list()

    def clear_fields(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()