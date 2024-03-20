from tkinter import *
import math

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "Error: Division by zero"
            else:
                result = num1 / num2
        elif operation == "√":
            if num1 < 0:
                result = "Error: Cannot take square root of a negative number"
            else:
                result = math.sqrt(num1)
        elif operation == "!":
            if num1 < 0:
                result = "Error: Cannot calculate factorial of a negative number"
            else:
                result = math.factorial(int(num1))
        else:
            result = "Invalid operation"

        label_result.config(text="Result: " + str(result))
    except ValueError:
        label_result.config(text="Error: Invalid input")
    except OverflowError:
        label_result.config(text="Error: Result is too large")

root = Tk()
root.title("Scientific Calculator")

# Changing Background Color
root.configure(bg="light blue")

# Labels
Label(root, text="Number 1:").grid(row=0, column=0, padx=5, pady=5)
Label(root, text="Number 2:").grid(row=1, column=0, padx=5, pady=5)
Label(root, text="Operation:").grid(row=2, column=0, padx=5, pady=5)
Label(root, text="Result:").grid(row=3, column=0, padx=5, pady=5)

# Entry Widgets
entry_num1 = Entry(root)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

entry_num2 = Entry(root)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

operation_var = StringVar(root)
operation_var.set("+")  # Default operation is addition
option_menu = OptionMenu(root, operation_var, "+", "-", "*", "/", "√", "!")
option_menu.grid(row=2, column=1, padx=5, pady=5)

# Result Label
label_result = Label(root, text="Result: ")
label_result.grid(row=3, column=1, padx=5, pady=5)

# Calculate Button
Button(root, text="Calculate", command=calculate).grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()