import customtkinter as ctk
from tkinter import messagebox
import re

# ---------------- Theme ----------------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

PRIMARY = "#6C63FF"
SECONDARY = "#4D96FF"
ACCENT = "#00C9A7"
DANGER = "#FF5C5C"
BG = "#F4F6FB"
CARD = "#FFFFFF"
TEXT_DARK = "#2B2E4A"

class ContactManager(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Window ---
        self.title("Contact Book • Pooja Pawar")
        self.geometry("1000x700")
        self.minsize(750, 600)
        self.configure(fg_color=BG)

        # --- Data ---
        self.contacts = [
            {"name": "Kaif", "code": "+91", "phone": "9876543210", "email": "kaif@gmail.com", "address": "Nagpur"},
            {"name": "JK", "code": "+1", "phone": "1234567890", "email": "jk@example.com", "address": "New York"}
        ]

        self.setup_ui()
        self.render_contacts()

    # ---------------- UI ----------------
    def setup_ui(self):
        # Header
        self.header = ctk.CTkFrame(self, fg_color=PRIMARY, corner_radius=18)
        self.header.pack(fill="x", padx=20, pady=(20, 15))

        ctk.CTkLabel(
            self.header,
            text="📒 Contact Manager",
            font=("Segoe UI", 28, "bold"),
            text_color="white"
        ).pack(side="left", padx=25, pady=18)

        ctk.CTkButton(
            self.header,
            text="+ Add Contact",
            fg_color=ACCENT,
            hover_color="#00B39F",
            text_color="black",
            font=("Segoe UI", 14, "bold"),
            width=140,
            height=42,
            corner_radius=12,
            command=self.open_add_dialog
        ).pack(side="right", padx=25)

        # Search
        self.search_var = ctk.StringVar()
        self.search_var.trace_add("write", self.search_contacts)

        self.search_entry = ctk.CTkEntry(
            self,
            placeholder_text="🔍 Search by name or number",
            textvariable=self.search_var,
            width=380,
            height=42,
            corner_radius=14,
            border_color=PRIMARY
        )
        self.search_entry.pack(anchor="w", padx=30, pady=(0, 10))

        # Cards Area
        self.scroll_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scroll_frame.pack(fill="both", expand=True, padx=20, pady=10)
        self.scroll_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Footer
        self.footer = ctk.CTkFrame(self, fg_color=CARD, height=40)
        self.footer.pack(fill="x", side="bottom")

        ctk.CTkLabel(
            self.footer,
            text="Made by Pooja Pawar",
            font=("Segoe UI", 11, "italic"),
            text_color="#7A7A7A"
        ).pack(pady=8)

    # ---------------- Cards ----------------
    def render_contacts(self, data=None):
        for w in self.scroll_frame.winfo_children():
            w.destroy()

        data = data if data else self.contacts

        for i, c in enumerate(data):
            self.create_card(c).grid(row=i // 3, column=i % 3, padx=12, pady=12, sticky="nsew")

    def create_card(self, c):
        card = ctk.CTkFrame(
            self.scroll_frame,
            fg_color=CARD,
            corner_radius=18,
            border_width=1,
            border_color="#E5E7EB"
        )

        ctk.CTkLabel(
            card,
            text=c["name"],
            font=("Segoe UI", 18, "bold"),
            text_color=TEXT_DARK
        ).pack(anchor="w", padx=18, pady=(15, 5))

        info = f"📞 {c['code']} {c['phone']}\n✉ {c['email']}\n📍 {c['address']}"
        ctk.CTkLabel(
            card,
            text=info,
            justify="left",
            font=("Segoe UI", 12),
            text_color="#555"
        ).pack(anchor="w", padx=18)

        btns = ctk.CTkFrame(card, fg_color="transparent")
        btns.pack(fill="x", padx=15, pady=15)

        ctk.CTkButton(
            btns,
            text="Edit",
            fg_color="#EEF2FF",
            text_color=PRIMARY,
            hover_color="#E0E7FF",
            height=32,
            command=lambda x=c: self.open_edit_dialog(x)
        ).pack(side="left", expand=True, padx=4)

        ctk.CTkButton(
            btns,
            text="Delete",
            fg_color="#FFE4E6",
            text_color=DANGER,
            hover_color="#FECDD3",
            height=32,
            command=lambda x=c: self.delete_contact(x)
        ).pack(side="left", expand=True, padx=4)

        return card

    # ---------------- Logic ----------------
    def validate(self, name, email, phone):
        if not name or not email or not phone:
            messagebox.showerror("Error", "All fields are required")
            return False
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            messagebox.showerror("Error", "Invalid email")
            return False
        if not phone.isdigit() or len(phone) != 10:
            messagebox.showerror("Error", "Phone must be 10 digits")
            return False
        return True

    def contact_window(self, title, edit=None):
        win = ctk.CTkToplevel(self)
        win.title(title)
        win.geometry("420x540")
        win.configure(fg_color=CARD)

        ctk.CTkLabel(win, text=title, font=("Segoe UI", 22, "bold"), text_color=PRIMARY).pack(pady=20)

        name = ctk.CTkEntry(win, placeholder_text="Full Name", width=320)
        phone = ctk.CTkEntry(win, placeholder_text="10-digit Phone", width=320)
        email = ctk.CTkEntry(win, placeholder_text="Email Address", width=320)
        addr = ctk.CTkEntry(win, placeholder_text="Address", width=320)

        for w in (name, phone, email, addr):
            w.pack(pady=8)

        if edit:
            name.insert(0, edit["name"])
            phone.insert(0, edit["phone"])
            email.insert(0, edit["email"])
            addr.insert(0, edit["address"])

        def save():
            if self.validate(name.get(), email.get(), phone.get()):
                new = {"name": name.get(), "code": "+91", "phone": phone.get(),
                       "email": email.get(), "address": addr.get()}
                if edit:
                    self.contacts[self.contacts.index(edit)] = new
                else:
                    self.contacts.append(new)
                self.render_contacts()
                win.destroy()

        ctk.CTkButton(
            win,
            text="Save Contact",
            fg_color=PRIMARY,
            hover_color="#584CFF",
            width=200,
            height=42,
            command=save
        ).pack(pady=25)

    def search_contacts(self, *a):
        q = self.search_var.get().lower()
        self.render_contacts([c for c in self.contacts if q in c["name"].lower() or q in c["phone"]])

    def delete_contact(self, c):
        if messagebox.askyesno("Confirm", f"Delete {c['name']}?"):
            self.contacts.remove(c)
            self.render_contacts()

    def open_add_dialog(self): self.contact_window("Add Contact")
    def open_edit_dialog(self, c): self.contact_window("Edit Contact", c)

# ---------------- Run ----------------
if __name__ == "__main__":
    app = ContactManager()
    app.mainloop()
