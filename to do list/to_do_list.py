import tkinter as tk
from tkinter import messagebox

# ---------------- Window ----------------
root = tk.Tk()
root.title("To-Do List • Pooja Pawar")
root.geometry("420x560")
root.configure(bg="#0f172a")
root.resizable(False, False)

tasks = []

# ---------------- Functions ----------------
def add_task(event=None):
    task = entry.get().strip()
    priority = priority_var.get()

    if task == "":
        return

    task_text = f"[{priority}] {task}"
    listbox.insert(tk.END, task_text)
    tasks.append(task_text)
    entry.delete(0, tk.END)

def delete_task():
    try:
        idx = listbox.curselection()[0]
        listbox.delete(idx)
        tasks.pop(idx)
    except:
        messagebox.showwarning("Warning", "Select a task to delete")

def edit_task():
    try:
        idx = listbox.curselection()[0]
        new_task = entry.get().strip()
        priority = priority_var.get()

        if new_task == "":
            return

        updated = f"[{priority}] {new_task}"
        listbox.delete(idx)
        listbox.insert(idx, updated)
        tasks[idx] = updated
        entry.delete(0, tk.END)
    except:
        messagebox.showwarning("Warning", "Select a task to edit")

def mark_done(event):
    try:
        idx = listbox.curselection()[0]
        task = listbox.get(idx)

        if not task.startswith("✔"):
            listbox.delete(idx)
            listbox.insert(idx, "✔ " + task)
    except:
        pass

def clear_all():
    if messagebox.askyesno("Confirm", "Clear all tasks?"):
        listbox.delete(0, tk.END)
        tasks.clear()

# ---------------- UI ----------------
# Header
header = tk.Label(
    root,
    text="📝 My To-Do List",
    font=("Segoe UI", 22, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)
header.pack(pady=20)

# Input Card
card = tk.Frame(root, bg="#1e293b", bd=0)
card.pack(padx=20, pady=10, fill="x")

entry = tk.Entry(
    card,
    font=("Segoe UI", 13),
    bg="#020617",
    fg="white",
    insertbackground="white",
    bd=0
)
entry.pack(fill="x", padx=15, pady=(15, 8))
entry.bind("<Return>", add_task)

# Priority
priority_var = tk.StringVar(value="Medium")

priority_frame = tk.Frame(card, bg="#1e293b")
priority_frame.pack(pady=5)

tk.Label(priority_frame, text="Priority:", bg="#1e293b", fg="#94a3b8")\
    .pack(side="left", padx=5)

for p, c in [("High", "#ef4444"), ("Medium", "#facc15"), ("Low", "#22c55e")]:
    tk.Radiobutton(
        priority_frame,
        text=p,
        value=p,
        variable=priority_var,
        bg="#1e293b",
        fg=c,
        selectcolor="#020617",
        activebackground="#1e293b"
    ).pack(side="left", padx=6)

# Buttons
btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(pady=15)

def action_btn(text, color, cmd):
    return tk.Button(
        btn_frame,
        text=text,
        width=10,
        bg=color,
        fg="black",
        font=("Segoe UI", 11, "bold"),
        bd=0,
        cursor="hand2",
        command=cmd
    )

action_btn("Add", "#38bdf8", add_task).grid(row=0, column=0, padx=6)
action_btn("Edit", "#22c55e", edit_task).grid(row=0, column=1, padx=6)
action_btn("Delete", "#ef4444", delete_task).grid(row=0, column=2, padx=6)
action_btn("Clear All", "#f59e0b", clear_all).grid(row=0, column=3, padx=6)

# Task List
listbox = tk.Listbox(
    root,
    font=("Segoe UI", 12),
    bg="#020617",
    fg="white",
    selectbackground="#38bdf8",
    bd=0,
    height=14
)
listbox.pack(fill="both", expand=True, padx=20, pady=10)
listbox.bind("<Double-Button-1>", mark_done)

# Footer
footer = tk.Label(
    root,
    text="Double-click task to mark completed • Made by Pooja Pawar",
    bg="#0f172a",
    fg="#94a3b8",
    font=("Segoe UI", 9, "italic")
)
footer.pack(pady=10)

root.mainloop()
