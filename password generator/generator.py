import tkinter as tk
import random
import string
from tkinter import messagebox

# ---------------- Window ----------------
root = tk.Tk()
root.title("Password Generator - Pooja Pawar")
root.geometry("440x560")
root.configure(bg="#0f172a")
root.resizable(False, False)

# ---------------- Variables ----------------
password_var = tk.StringVar()
length_var = tk.IntVar(value=16)
strength_var = tk.StringVar(value="Strong")

use_upper = tk.BooleanVar(value=True)
use_lower = tk.BooleanVar(value=True)
use_numbers = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=True)

# ---------------- Functions ----------------
def generate_password():
    chars = ""

    if use_upper.get(): chars += string.ascii_uppercase
    if use_lower.get(): chars += string.ascii_lowercase
    if use_numbers.get(): chars += string.digits
    if use_symbols.get(): chars += "!@#$%^&*()_+~`|}{[]:;?><,./-="

    if chars == "":
        password_var.set("Select options")
        strength_var.set("---")
        return

    length = length_var.get()
    password = "".join(random.choice(chars) for _ in range(length))
    password_var.set(password)
    update_strength(length, len(chars))


def update_strength(length, pool_size):
    if length < 8 or pool_size < 30:
        strength_var.set("Weak")
        strength_label.config(fg="#ef4444")
    elif length < 14:
        strength_var.set("Medium")
        strength_label.config(fg="#f59e0b")
    else:
        strength_var.set("Strong")
        strength_label.config(fg="#22c55e")


def copy_password():
    pwd = password_var.get()
    if pwd in ["", "Select options"]:
        return
    root.clipboard_clear()
    root.clipboard_append(pwd)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# ---------------- Header ----------------
header = tk.Label(
    root,
    text="🔐 Password Generator",
    font=("Segoe UI", 20, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)
header.pack(pady=(15, 5))

subtitle = tk.Label(
    root,
    text="Create strong and secure passwords",
    bg="#0f172a",
    fg="#94a3b8"
)
subtitle.pack()

# ---------------- Card ----------------
card = tk.Frame(
    root,
    bg="#1e293b",
    highlightthickness=1,
    highlightbackground="#334155"
)
card.pack(padx=20, pady=20, fill="both", expand=True)

# Password Box
tk.Label(
    card, text="Your Password",
    bg="#1e293b",
    fg="#e5e7eb",
    font=("Segoe UI", 10, "bold")
).pack(pady=(20, 5))

pwd_entry = tk.Entry(
    card,
    textvariable=password_var,
    font=("Consolas", 15, "bold"),
    justify="center",
    bg="#020617",
    fg="#38bdf8",
    bd=0,
    insertbackground="white"
)
pwd_entry.pack(fill="x", padx=20, pady=10, ipady=10)

# Strength
strength_frame = tk.Frame(card, bg="#1e293b")
strength_frame.pack(fill="x", padx=20, pady=10)

tk.Label(
    strength_frame,
    text="Strength:",
    bg="#1e293b",
    fg="#94a3b8"
).pack(side="left")

strength_label = tk.Label(
    strength_frame,
    textvariable=strength_var,
    bg="#1e293b",
    fg="#22c55e",
    font=("Segoe UI", 10, "bold")
)
strength_label.pack(side="right")

# Length Slider
tk.Label(
    card,
    text="Password Length",
    bg="#1e293b",
    fg="#e5e7eb",
    font=("Segoe UI", 10, "bold")
).pack(pady=(15, 5))

length_scale = tk.Scale(
    card,
    from_=4,
    to=128,
    orient="horizontal",
    variable=length_var,
    command=lambda x: generate_password(),
    bg="#1e293b",
    fg="#38bdf8",
    troughcolor="#020617",
    highlightthickness=0
)
length_scale.pack(fill="x", padx=20)

# Options
options = tk.Frame(card, bg="#1e293b")
options.pack(padx=20, pady=15, fill="x")

def styled_check(text, var):
    return tk.Checkbutton(
        options,
        text=text,
        variable=var,
        bg="#1e293b",
        fg="#e5e7eb",
        activebackground="#1e293b",
        activeforeground="#38bdf8",
        selectcolor="#020617",
        command=generate_password
    )

styled_check("Uppercase (A-Z)", use_upper).pack(anchor="w")
styled_check("Lowercase (a-z)", use_lower).pack(anchor="w")
styled_check("Numbers (0-9)", use_numbers).pack(anchor="w")
styled_check("Symbols (!@#$)", use_symbols).pack(anchor="w")

# Buttons
btn_frame = tk.Frame(card, bg="#1e293b")
btn_frame.pack(pady=20)

tk.Button(
    btn_frame,
    text="🔄 Regenerate",
    bg="#38bdf8",
    fg="#020617",
    font=("Segoe UI", 11, "bold"),
    width=18,
    bd=0,
    cursor="hand2",
    command=generate_password
).grid(row=0, column=0, padx=6)

tk.Button(
    btn_frame,
    text="📋 Copy",
    bg="#22c55e",
    fg="#020617",
    font=("Segoe UI", 11, "bold"),
    width=10,
    bd=0,
    cursor="hand2",
    command=copy_password
).grid(row=0, column=1, padx=6)

# Footer
footer = tk.Label(
    root,
    text="Made by Pooja Pawar",
    bg="#0f172a",
    fg="#94a3b8",
    font=("Segoe UI", 9, "italic")
)
footer.pack(pady=12)

# Default password
generate_password()

root.mainloop()
