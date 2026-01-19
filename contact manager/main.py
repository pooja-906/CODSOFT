import customtkinter as ctk
from tkinter import messagebox
import re

# Set the theme to Light and Blue
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class ContactManager(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Window Configuration ---
        self.title("Aesthetic Contact Manager")
        self.geometry("1000x700")
        self.minsize(700, 600)  # Ensures UI doesn't break when small
        self.configure(fg_color="#F0F2F9") # Soft aesthetic background

        # --- Data Storage ---
        self.contacts = [
            {"name": "Kaif", "code": "+91", "phone": "9876543210", "email": "kaif@gmail.com", "address": "Nagpur"},
            {"name": "JK", "code": "+1", "phone": "1234567890", "email": "jk@example.com", "address": "New York"}
        ]

        self.setup_ui()
        self.render_contacts()

    def setup_ui(self):
        # 1. Header Section
        self.header = ctk.CTkFrame(self, fg_color="#6200EA", corner_radius=15)
        self.header.pack(fill="x", padx=20, pady=(20, 10))

        self.title_lbl = ctk.CTkLabel(self.header, text="Contact Manager", font=("Arial Bold", 28), text_color="white")
        self.title_lbl.pack(side="left", padx=20, pady=15)

        self.add_btn = ctk.CTkButton(self.header, text="+ Add New", fg_color="#03DAC6", hover_color="#018786", 
                                     text_color="#000", font=("Arial Bold", 13), width=100,
                                     command=self.open_add_dialog, height=38, corner_radius=8)
        self.add_btn.pack(side="right", padx=20)

        # 2. Search Section
        self.search_var = ctk.StringVar()
        self.search_var.trace_add("write", self.search_contacts)
        self.search_entry = ctk.CTkEntry(self, placeholder_text="🔍 Search name or number...", 
                                         textvariable=self.search_var, width=350, height=40, 
                                         corner_radius=10, border_color="#6200EA")
        self.search_entry.pack(anchor="w", padx=20, pady=(0, 10))

        # 3. Main Content (Scrollable) - Using expand=True to push footer down
        self.scroll_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scroll_frame.pack(fill="both", expand=True, padx=15, pady=5)
        
        # Configure grid columns for responsiveness
        self.scroll_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # 4. Fixed Footer Section
        self.footer = ctk.CTkFrame(self, fg_color="white", height=35, corner_radius=0)
        self.footer.pack(fill="x", side="bottom")
        
        self.footer_label = ctk.CTkLabel(
            self.footer, 
            text="Made by Pooja Pawar", 
            font=("Arial", 11, "italic"), 
            text_color="#777777"
        )
        self.footer_label.pack(pady=5)

    def render_contacts(self, data_list=None):
        # Clear current view
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        display_data = data_list if data_list is not None else self.contacts
        
        for i, contact in enumerate(display_data):
            card = self.create_card(contact)
            card.grid(row=i // 3, column=i % 3, padx=10, pady=10, sticky="nsew")

    def create_card(self, contact):
        card = ctk.CTkFrame(self.scroll_frame, fg_color="white", corner_radius=15, 
                            border_width=1, border_color="#E0E0E0")
        
        ctk.CTkLabel(card, text=contact['name'], font=("Arial Bold", 18), text_color="#311B92").pack(anchor="w", padx=15, pady=(12, 5))
        
        details = f"📞 {contact['code']} {contact['phone']}\n✉ {contact['email']}\n📍 {contact['address']}"
        ctk.CTkLabel(card, text=details, font=("Arial", 12), justify="left", text_color="#555").pack(anchor="w", padx=15, pady=5)

        # Action Buttons
        btn_f = ctk.CTkFrame(card, fg_color="transparent")
        btn_f.pack(fill="x", padx=10, pady=12)
        
        ctk.CTkButton(btn_f, text="Edit", fg_color="#F3E5F5", text_color="#6200EA", hover_color="#E1BEE7",
                      height=30, command=lambda c=contact: self.open_edit_dialog(c)).pack(side="left", expand=True, padx=4)
        
        ctk.CTkButton(btn_f, text="Delete", fg_color="#FFEBEE", text_color="#D32F2F", hover_color="#FFCDD2",
                      height=30, command=lambda c=contact: self.delete_contact(c)).pack(side="left", expand=True, padx=4)
        return card

    # --- Validation & Dialog Logic ---
    
    def validate(self, name, email, phone):
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not name or not email or not phone:
            messagebox.showerror("Validation Error", "Name, Email, and Phone are required!")
            return False
        if not re.match(email_regex, email):
            messagebox.showerror("Validation Error", "Please enter a valid email address!")
            return False
        if not (phone.isdigit() and len(phone) == 10):
            messagebox.showerror("Validation Error", "Phone number must be exactly 10 digits!")
            return False
        return True

    def contact_window(self, title, edit_data=None):
        win = ctk.CTkToplevel(self)
        win.title(title)
        win.geometry("400x550")
        win.attributes("-topmost", True)
        win.configure(fg_color="white")

        ctk.CTkLabel(win, text=title, font=("Arial Bold", 20), text_color="#6200EA").pack(pady=20)

        # Fields
        name_ent = ctk.CTkEntry(win, placeholder_text="Full Name", width=300)
        name_ent.pack(pady=8)

        p_frame = ctk.CTkFrame(win, fg_color="transparent")
        p_frame.pack(pady=8)
        codes = ["+91", "+1", "+44", "+971"]
        code_var = ctk.StringVar(value=edit_data['code'] if edit_data else "+91")
        ctk.CTkOptionMenu(p_frame, values=codes, variable=code_var, width=75).pack(side="left", padx=2)
        phone_ent = ctk.CTkEntry(p_frame, placeholder_text="10 Digit Number", width=220)
        phone_ent.pack(side="left", padx=2)

        email_ent = ctk.CTkEntry(win, placeholder_text="Email Address", width=300)
        email_ent.pack(pady=8)

        addr_ent = ctk.CTkEntry(win, placeholder_text="Address", width=300)
        addr_ent.pack(pady=8)

        if edit_data:
            name_ent.insert(0, edit_data['name'])
            phone_ent.insert(0, edit_data['phone'])
            email_ent.insert(0, edit_data['email'])
            addr_ent.insert(0, edit_data['address'])

        def save():
            if self.validate(name_ent.get(), email_ent.get(), phone_ent.get()):
                new_c = {
                    "name": name_ent.get(), "code": code_var.get(), 
                    "phone": phone_ent.get(), "email": email_ent.get(), "address": addr_ent.get()
                }
                if edit_data:
                    idx = self.contacts.index(edit_data)
                    self.contacts[idx] = new_c
                else:
                    self.contacts.append(new_c)
                self.render_contacts()
                win.destroy()

        ctk.CTkButton(win, text="Save Contact", fg_color="#6200EA", width=200, height=40, command=save).pack(pady=25)

    def search_contacts(self, *args):
        q = self.search_var.get().lower()
        filtered = [c for c in self.contacts if q in c['name'].lower() or q in c['phone']]
        self.render_contacts(filtered)

    def delete_contact(self, contact):
        if messagebox.askyesno("Confirm", f"Delete {contact['name']}?"):
            self.contacts.remove(contact)
            self.render_contacts()

    def open_add_dialog(self): self.contact_window("Add Contact")
    def open_edit_dialog(self, c): self.contact_window("Edit Contact", c)

if __name__ == "__main__":
    app = ContactManager()
    app.mainloop()