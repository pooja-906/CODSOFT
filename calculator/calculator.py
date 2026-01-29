import tkinter as tk

# ---------- Main Window ----------
root = tk.Tk()
root.title("Glass Calculator")
root.geometry("360x520")
root.configure(bg="#0f172a")
root.resizable(False, False)

expression = ""

# ---------- Logic ----------
def update_display():
    display_var.set(expression)

def press(key):
    global expression
    expression += str(key)
    update_display()

def clear():
    global expression
    expression = ""
    update_display()

def delete():
    global expression
    expression = expression[:-1]
    update_display()

def calculate(event=None):
    global expression
    try:
        expression = str(eval(expression))
    except:
        expression = ""
        display_var.set("Error")
        return
    update_display()

# ---------- Keyboard Handler (REAL FIX) ----------
def key_input(event):
    global expression

    if event.keysym in ("Return", "KP_Enter"):
        calculate()
        return "break"

    if event.keysym == "BackSpace":
        delete()
        return "break"

    if event.keysym == "Escape":
        clear()
        return "break"

    if event.char.isdigit() or event.char in "+-*/.":
        press(event.char)
        return "break"

    return "break"  # Block default Entry typing

# ---------- Display ----------
display_var = tk.StringVar()

display_frame = tk.Frame(
    root,
    bg="#1e293b",
    highlightthickness=1,
    highlightbackground="#334155"
)
display_frame.pack(padx=20, pady=25, fill="x")

display = tk.Entry(
    display_frame,
    textvariable=display_var,
    font=("Segoe UI", 26, "bold"),
    bg="#1e293b",
    fg="#38bdf8",
    bd=0,
    justify="right"
)
display.pack(fill="x", padx=15, pady=18)

# ⭐ CRITICAL LINES ⭐
display.focus_set()
display.bind("<Key>", key_input)

# ---------- Buttons ----------
btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(padx=15)

def create_button(text, command, bg, fg):
    return tk.Button(
        btn_frame,
        text=text,
        command=command,
        font=("Segoe UI", 14, "bold"),
        bg=bg,
        fg=fg,
        width=6,
        height=2,
        bd=0,
        cursor="hand2",
        activebackground="#475569",
        activeforeground="white"
    )

buttons = [
    ("AC", clear, "#ef4444", "white"),
    ("DEL", delete, "#f59e0b", "black"),
    ("/", lambda: press("/"), "#334155", "#38bdf8"),
    ("*", lambda: press("*"), "#334155", "#38bdf8"),

    ("7", lambda: press("7"), "#1e293b", "white"),
    ("8", lambda: press("8"), "#1e293b", "white"),
    ("9", lambda: press("9"), "#1e293b", "white"),
    ("-", lambda: press("-"), "#334155", "#38bdf8"),

    ("4", lambda: press("4"), "#1e293b", "white"),
    ("5", lambda: press("5"), "#1e293b", "white"),
    ("6", lambda: press("6"), "#1e293b", "white"),
    ("+", lambda: press("+"), "#334155", "#38bdf8"),

    ("1", lambda: press("1"), "#1e293b", "white"),
    ("2", lambda: press("2"), "#1e293b", "white"),
    ("3", lambda: press("3"), "#1e293b", "white"),
    ("=", calculate, "#22c55e", "black"),

    ("0", lambda: press("0"), "#1e293b", "white"),
    (".", lambda: press("."), "#1e293b", "white"),
]

row = col = 0
for text, cmd, bg, fg in buttons:
    create_button(text, cmd, bg, fg).grid(row=row, column=col, padx=8, pady=8)
    col += 1
    if col == 4:
        col = 0
        row += 1

# ---------- Footer ----------
footer = tk.Label(
    root,
    text="Made by Pooja Pawar",
    fg="#94a3b8",
    bg="#0f172a",
    font=("Segoe UI", 9, "italic")
)
footer.pack(side="bottom", pady=15)

root.mainloop()
