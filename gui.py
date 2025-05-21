import tkinter as tk
from logic import evaluate_expression

def create_gui():
    window = tk.Tk()
    window.title("Calculator")
    window.geometry("300x400")

    expression = ""

    def update_display(value):
        nonlocal expression
        expression += value
        result_var.set(expression)

    def clear():
        nonlocal expression
        expression = ""
        result_var.set("")

    def calculate():
        nonlocal expression
        result = evaluate_expression(expression)
        result_var.set(result)
        expression = result if result.isnumeric() else ""

    result_var = tk.StringVar()

    entry = tk.Entry(window, textvariable=result_var, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
    entry.pack(fill="both", ipadx=8, ipady=15, pady=10)

    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
    ]

    for row in buttons:
        row_frame = tk.Frame(window)
        row_frame.pack(expand=True, fill="both")
        for btn_text in row:
            btn = tk.Button(
                row_frame, text=btn_text, font=("Arial", 18), bd=5,
                command=lambda b=btn_text: calculate() if b == "=" else update_display(b)
            )
            btn.pack(side="left", expand=True, fill="both")

    clear_btn = tk.Button(window, text="C", font=("Arial", 18), bd=5, command=clear)
    clear_btn.pack(fill="both", expand=True)

    window.mainloop()
