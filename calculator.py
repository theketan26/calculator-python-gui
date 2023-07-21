import tkinter
import customtkinter as ctk


root = ctk.CTk()


master_label = ctk.CTkLabel(master=root, text="CALCULATOR")
master_label.grid(row=0, column=0, columnspan=2)


equation, result, operation = tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar()


def set_equation(x):
    pre_eq = equation.get()
    if x == '.':
        if '.' in pre_eq:
            return
        if pre_eq == '':
            equation.set('0' + x)
            return
    elif x == '0' and (pre_eq == ''):
        return
    equation.set(pre_eq + x)


def remove_equation(clear=False):
    pre_eq = equation.get()
    if clear:
        equation.set('')
    elif pre_eq != '':
        equation.set(pre_eq[:-1])


def add_operator(x):
    pre_eq = equation.get()
    if pre_eq != '':
        if result.get() != '':
            equate()
        operation.set(x)
        result.set(pre_eq)
        equation.set('')


def equate():
    if operation == '+':
        result.set(str(float(equation.get()) + float(result.get())))


equation_entry = ctk.CTkEntry(master=root, textvariable=equation)
result_label = ctk.CTkLabel(master=root, textvariable=result)
operation_label = ctk.CTkLabel(master=root, textvariable=operation)
equation_entry.grid(row=1, column=0, columnspan=2, padx=2)
operation_label.grid(row=2, column=0, padx=2)
result_label.grid(row=2, column=1, padx=2)


number_frame = ctk.CTkFrame(master=root)
number_buttons = {
    "1": ctk.CTkButton(master=number_frame, command=lambda: set_equation("1"), text="1", height=25, width=50),
    "2": ctk.CTkButton(master=number_frame, command=lambda: set_equation("2"), text="2", height=25, width=50),
    "3": ctk.CTkButton(master=number_frame, command=lambda: set_equation("3"), text="3", height=25, width=50),
    "4": ctk.CTkButton(master=number_frame, command=lambda: set_equation("4"), text="4", height=25, width=50),
    "5": ctk.CTkButton(master=number_frame, command=lambda: set_equation("5"), text="5", height=25, width=50),
    "6": ctk.CTkButton(master=number_frame, command=lambda: set_equation("6"), text="6", height=25, width=50),
    "7": ctk.CTkButton(master=number_frame, command=lambda: set_equation("7"), text="7", height=25, width=50),
    "8": ctk.CTkButton(master=number_frame, command=lambda: set_equation("8"), text="8", height=25, width=50),
    "9": ctk.CTkButton(master=number_frame, command=lambda: set_equation("9"), text="9", height=25, width=50),
    "0": ctk.CTkButton(master=number_frame, command=lambda: set_equation("0"), text="0", height=25, width=104),
    ".": ctk.CTkButton(master=number_frame, command=lambda: set_equation("."), text=".", height=25, width=50),
}

number_frame.grid(row=3, column=0)
number_buttons["1"].grid(row=0, column=0, padx=2, pady=1)
number_buttons["2"].grid(row=0, column=1, padx=2, pady=1)
number_buttons["3"].grid(row=0, column=2, padx=2, pady=1)
number_buttons["4"].grid(row=1, column=0, padx=2, pady=1)
number_buttons["5"].grid(row=1, column=1, padx=2, pady=1)
number_buttons["6"].grid(row=1, column=2, padx=2, pady=1)
number_buttons["7"].grid(row=2, column=0, padx=2, pady=1)
number_buttons["8"].grid(row=2, column=1, padx=2, pady=1)
number_buttons["9"].grid(row=2, column=2, padx=2, pady=1)
number_buttons["."].grid(row=3, column=0, padx=2, pady=1)
number_buttons["0"].grid(row=3, column=1, columnspan=2, padx=2, pady=1)


operator_frame = ctk.CTkFrame(master=root)
operator_buttons = {
    "+": ctk.CTkButton(master=operator_frame, command=lambda: add_operator("+"), text="+", width=50, height=25),
    "-": ctk.CTkButton(master=operator_frame, command=lambda: add_operator("_"), text="-", width=50, height=25),
    "^": ctk.CTkButton(master=operator_frame, command=lambda: add_operator("^"), text="^", width=50, height=25),
    "*": ctk.CTkButton(master=operator_frame, command=lambda: add_operator("*"), text="*", width=50, height=25),
    "/": ctk.CTkButton(master=operator_frame, command=lambda: add_operator("/"), text="/", width=50, height=25),
    "eq": ctk.CTkButton(master=operator_frame, text="eq", width=50, height=25),
    "%": ctk.CTkButton(master=operator_frame, command=lambda: add_operator("%"), text="%", width=50, height=25),
    "√": ctk.CTkButton(master=operator_frame, command=lambda: add_operator("√"), text="√", width=50, height=25),
    "=": ctk.CTkButton(master=operator_frame, text="=", width=104, height=25),
    "↼": ctk.CTkButton(master=operator_frame, command=lambda: remove_equation(), text="↼", width=50, height=25),
    "c": ctk.CTkButton(master=operator_frame, text="c", width=50, height=25),
}

operator_frame.grid(row=3, column=1)
operator_buttons["+"].grid(row=0, column=0, padx=2, pady=1)
operator_buttons["-"].grid(row=0, column=1, padx=2, pady=1)
operator_buttons["^"].grid(row=0, column=2, padx=2, pady=1)
operator_buttons["*"].grid(row=1, column=0, padx=2, pady=1)
operator_buttons["/"].grid(row=1, column=1, padx=2, pady=1)
operator_buttons["eq"].grid(row=1, column=2, padx=2, pady=1)
operator_buttons["%"].grid(row=2, column=0, padx=2, pady=1)
operator_buttons["√"].grid(row=2, column=1, padx=2, pady=1)
operator_buttons["="].grid(row=3, column=0, columnspan=2, padx=2, pady=1)
operator_buttons["↼"].grid(row=2 , column=2, padx=2, pady=1)
operator_buttons["c"].grid(row=3, column=2, padx=2, pady=1)

root.mainloop()