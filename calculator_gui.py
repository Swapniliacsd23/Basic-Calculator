import tkinter as tk
from tkinter import messagebox

def click(event):
    current = str(entry.get())
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero.")
        except:
            messagebox.showerror("Error", "Invalid Expression")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Setup window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        b = tk.Button(frame, text=btn, font=("Arial", 18), height=2, width=4)
        b.pack(side=tk.LEFT, expand=True, fill="both", padx=2, pady=2)
        b.bind("<Button-1>", click)

root.mainloop()
