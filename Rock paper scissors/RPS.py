import tkinter as tk
import random

# ---------------- Window ----------------
root = tk.Tk()
root.title("Rock Paper Scissors - Pooja Pawar")
root.geometry("440x560")
root.configure(bg="#1e1b4b")  # Deep indigo
root.resizable(False, False)

# ---------------- Variables ----------------
choices = ["✊", "✋", "✌️"]
win_map = {"✊": "✌️", "✋": "✊", "✌️": "✋"}
player_score = 0
cpu_score = 0

# ---------------- Functions ----------------
def play(player_choice):
    global player_score, cpu_score

    player_label.config(text=player_choice)
    cpu_label.config(text="🎲")
    message.config(text="Thinking...", fg="#facc15")

    root.after(900, lambda: result(player_choice))


def result(player_choice):
    global player_score, cpu_score

    cpu_choice = random.choice(choices)
    cpu_label.config(text=cpu_choice)

    if player_choice == cpu_choice:
        message.config(text="It's a Draw 🤝", fg="#38bdf8")
    elif win_map[player_choice] == cpu_choice:
        message.config(text="You Won! 🔥", fg="#22c55e")
        player_score += 1
    else:
        message.config(text="CPU Won! 🤖", fg="#ef4444")
        cpu_score += 1

    score.config(text=f"{player_score}  —  {cpu_score}")

# ---------------- Main Card ----------------
card = tk.Frame(root, bg="#ffffff", bd=0)
card.place(relx=0.5, rely=0.48, anchor="center", width=380, height=460)

# Title
title = tk.Label(
    card,
    text="🎮 Battle Arena",
    font=("Segoe UI", 22, "bold"),
    bg="white",
    fg="#4338ca"
)
title.pack(pady=15)

# Display Section
display = tk.Frame(card, bg="white")
display.pack(pady=10)

tk.Label(display, text="PLAYER", font=("Segoe UI", 10, "bold"), bg="white", fg="#64748b")\
    .grid(row=0, column=0, padx=45)
tk.Label(display, text="COMPUTER", font=("Segoe UI", 10, "bold"), bg="white", fg="#64748b")\
    .grid(row=0, column=1, padx=45)

player_label = tk.Label(
    display,
    text="?",
    font=("Segoe UI", 48),
    bg="#eef2ff",
    width=3
)
player_label.grid(row=1, column=0, padx=20, pady=15)

cpu_label = tk.Label(
    display,
    text="?",
    font=("Segoe UI", 48),
    bg="#fee2e2",
    width=3
)
cpu_label.grid(row=1, column=1, padx=20, pady=15)

# Message
message = tk.Label(
    card,
    text="Ready to play?",
    font=("Segoe UI", 14, "bold"),
    bg="white",
    fg="#4338ca"
)
message.pack(pady=15)

# Buttons
btn_frame = tk.Frame(card, bg="white")
btn_frame.pack(pady=10)

btn_colors = {
    "✊": "#fde68a",
    "✋": "#bbf7d0",
    "✌️": "#bae6fd"
}

for c in choices:
    tk.Button(
        btn_frame,
        text=c,
        font=("Segoe UI", 26),
        width=3,
        bg=btn_colors[c],
        bd=0,
        cursor="hand2",
        activebackground="#e5e7eb",
        command=lambda ch=c: play(ch)
    ).pack(side="left", padx=12)

# Score Board
score = tk.Label(
    card,
    text="0  —  0",
    font=("Segoe UI", 14, "bold"),
    bg="#4338ca",
    fg="white",
    padx=30,
    pady=10
)
score.pack(pady=25)

# Footer
footer = tk.Label(
    root,
    text="Made by Pooja Pawar",
    bg="#1e1b4b",
    fg="#e0e7ff",
    font=("Segoe UI", 10, "italic")
)
footer.pack(side="bottom", pady=12)

root.mainloop()
