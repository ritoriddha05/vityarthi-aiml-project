import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- LOGIC ---------------- #
def generate_schedule():
    try:
        subjects = subject_entry.get().split(",")
        difficulty = list(map(int, difficulty_entry.get().split(",")))
        hours = float(hours_entry.get())
        days = int(days_entry.get())

        if len(subjects) != len(difficulty):
            messagebox.showerror("Error", "Subjects & difficulty must match!")
            return

        total = sum(difficulty)
        weights = [d / total for d in difficulty]

        output_text.delete("1.0", tk.END)

        for day in range(1, days + 1):
            output_text.insert(tk.END, f"📅 Day {day}\n", "day")

            for i in range(len(subjects)):
                if day % 3 == 0:
                    name = subjects[i] + " (Revision)"
                else:
                    name = subjects[i]

                hrs = round(weights[i] * hours, 2)
                output_text.insert(tk.END, f"  • {name}: {hrs} hrs\n")

            output_text.insert(tk.END, "\n")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def save_to_file():
    data = output_text.get("1.0", tk.END)
    with open("schedule.txt", "w") as f:
        f.write(data)
    messagebox.showinfo("Saved", "Schedule saved as schedule.txt")


# ---------------- UI ---------------- #
root = tk.Tk()
root.title("Smart Study Planner")
root.geometry("650x700")
root.configure(bg="#0f172a")  # dark background

# Style
style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel", background="#0f172a", foreground="white", font=("Segoe UI", 11))
style.configure("TEntry", padding=5)
style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)

# ---------------- HEADER ---------------- #
title = tk.Label(root, text="🧠 Smart Study Planner",
                 font=("Segoe UI", 20, "bold"),
                 bg="#0f172a", fg="#38bdf8")
title.pack(pady=20)

# ---------------- INPUT FRAME ---------------- #
frame = tk.Frame(root, bg="#1e293b", bd=0)
frame.pack(padx=20, pady=10, fill="x")

def create_input(label_text):
    label = tk.Label(frame, text=label_text, bg="#1e293b", fg="white", anchor="w")
    label.pack(fill="x", padx=10, pady=(10, 2))
    entry = ttk.Entry(frame)
    entry.pack(fill="x", padx=10, pady=5)
    return entry

subject_entry = create_input("Subjects (comma separated)")
difficulty_entry = create_input("Difficulty (1,2,3...)")
hours_entry = create_input("Hours per day")
days_entry = create_input("Days left")

# ---------------- BUTTONS ---------------- #
btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(pady=15)

generate_btn = tk.Button(btn_frame, text="Generate Plan",
                         command=generate_schedule,
                         bg="#38bdf8", fg="black",
                         font=("Segoe UI", 11, "bold"),
                         padx=20, pady=8, bd=0)
generate_btn.grid(row=0, column=0, padx=10)

save_btn = tk.Button(btn_frame, text="Save Plan",
                     command=save_to_file,
                     bg="#22c55e", fg="black",
                     font=("Segoe UI", 11, "bold"),
                     padx=20, pady=8, bd=0)
save_btn.grid(row=0, column=1, padx=10)

# ---------------- OUTPUT ---------------- #
output_frame = tk.Frame(root, bg="#1e293b")
output_frame.pack(padx=20, pady=10, fill="both", expand=True)

scrollbar = tk.Scrollbar(output_frame)
scrollbar.pack(side="right", fill="y")

output_text = tk.Text(output_frame,
                      bg="#020617",
                      fg="white",
                      font=("Consolas", 10),
                      yscrollcommand=scrollbar.set,
                      wrap="word")

output_text.pack(fill="both", expand=True)
scrollbar.config(command=output_text.yview)

# Styling text
output_text.tag_config("day", foreground="#38bdf8", font=("Segoe UI", 12, "bold"))

root.mainloop()