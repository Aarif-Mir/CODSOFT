import tkinter as tk
from math import sqrt, cos, exp, log

# Function Definitions
def click_button(value):
    """ Append button value to entry field """
    current = entry.get()  
    entry.delete(0, tk.END)  
    entry.insert(0, current + value) 

def clear_entry():
    """ Clear the entry field """
    entry.delete(0, tk.END)

def delete_last():
    """ Delete the last entered character """
    current = entry.get()
    entry.delete(len(current)-1, tk.END)

def calculate():
    """ Evaluate the mathematical expression entered in the entry field """
    try:
        expression = entry.get()
        expression = expression.replace("^", "**")
        expression = expression.replace("log(", "log(")

        # Evaluate the expression using eval
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="#2f3e46")

entry = tk.Entry(root, width=35, borderwidth=5, font=("Arial", 20), justify='right', bg="#333", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("^", 5, 1), ("sqrt", 5, 2), ("%", 5, 3),
    ("cos", 6, 0), ("log", 6, 1), (")", 6, 2), ("Del", 6, 3)
]

# Define button colors
button_colors = {
    "C": "#ff4c4c",  
    "Del": "#ffab4c",  
    "=": "#4caf50",  
    "+": "#2196f3", 
    "-": "#2196f3",
    "*": "#2196f3", 
    "/": "#2196f3", 
    "^": "#2196f3", 
    "sqrt": "#ff9800",  
    "cos": "#ff9800",  
    "log": "#ff9800", 
    "%": "#ff9800",  
}

# Create and place buttons with styling
for text, row, col in buttons:
    color = button_colors.get(text, "#555e63") 
    if text == "=":
        button = tk.Button(root, text=text, width=10, height=2, bg=color, fg="white", font=("Arial", 18), command=calculate)
    elif text == "C":
        button = tk.Button(root, text=text, width=10, height=2, bg=color, fg="white", font=("Arial", 18), command=clear_entry)
    elif text == "Del":
        button = tk.Button(root, text=text, width=10, height=2, bg=color, fg="white", font=("Arial", 18), command=delete_last)
    elif text == "sqrt":
        button = tk.Button(root, text=text, width=10, height=2, bg=color, fg="white", font=("Arial", 18), command=lambda: click_button("sqrt("))
    elif text == "cos":
        button = tk.Button(root, text=text, width=10, height=2, bg=color, fg="white", font=("Arial", 18), command=lambda: click_button("cos("))
    elif text == "log":
        button = tk.Button(root, text=text, width=10, height=2, bg=color, fg="white", font=("Arial", 18), command=lambda: click_button("log("))
    else:
        button = tk.Button(root, text=text, width=10, height=2, bg=color, fg="white", font=("Arial", 18), command=lambda value=text: click_button(value))

    button.grid(row=row, column=col, padx=10, pady=10)

# Run the application
root.mainloop()