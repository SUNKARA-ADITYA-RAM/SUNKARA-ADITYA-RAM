import tkinter as tk
from tkinter import messagebox

def update_expression(num):
    expression_field.insert(tk.END, str(num))

def clear():
    expression_field.delete(0, tk.END)
def evaluate():
    try:
        result = eval(expression_field.get())
        expression_field.delete(0, tk.END)
        expression_field.insert(tk.END, str(result))
    except:
        messagebox.showerror("Error", "Invalid input")

root = tk.Tk()
root.title("Calculator")
root.geometry("900x500")

expression_field = tk.Entry(root, font=('Arial', 20), justify='right', bd=10, bg='#eaeaea', width=15)
expression_field.grid(row=0, column=0, columnspan=4)

buttons = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', 'C', '=', '+']

for i, button in enumerate(buttons):
    action = evaluate if button == '=' else clear if button == 'C' else lambda b=button: update_expression(b)
    tk.Button(root, text=button, height=2, width=5, font=('Arial', 18), command=action).grid(row=1 + i//4, column=i%4)
root.mainloop()
