import math
import tkinter
import customtkinter as ctk


root = ctk.CTk()


master_label = ctk.CTkLabel(master=root, text="CALCULATOR")
master_label.grid(row=0, column=0, columnspan=2)


equation, result = tkinter.StringVar(), tkinter.StringVar()


def set_val(val, fun='eq'):
    if fun == 'res':
        result.set(val)
    else:
        equation.set(val)
        equate()


def set_equation(x):
    pre_eq = equation.get()
    if x == '.':
        if '.' in pre_eq:
            return
        if pre_eq == '':
            set_val('0' + x)
            return
    elif x == '0' and (pre_eq == ''):
        return
    set_val(pre_eq + x)


def remove_equation(clear=False):
    pre_eq = equation.get()
    if clear:
        set_val('')
    elif pre_eq != '':
        set_val(pre_eq[:-1])


def add_operator(x):
    pre_eq = equation.get()
    if pre_eq != '':
        if not pre_eq[-1].isdigit():
            if pre_eq[-1] == '=':
                equate()
            return
        set_val(pre_eq + x)
    elif x == '√':
        set_val(pre_eq + '√')


def equate_lst(lst):
    leng = len(lst)
    ops = ['√', '^', '/', '*', '+', '-', '%']
    for op in ops:
        i = 0
        while i < leng - 1:
            j = i
            if lst[i] == '(':
                while j < len(lst):
                    if i == ')':
                        break
                    j += 1
                equate_lst(lst[i + 1:j - 1])
            elif lst[i] in ops:
                if lst[i] == op == '√':
                    lst[i] = math.sqrt(lst[i + 1])
                    lst.pop(i + 1)
                    continue
                elif lst[i] == op == '^':
                    lst[i] = lst[i - 1] ** lst[i + 1]
                    i -= 1
                elif lst[i] == op == '/':
                    lst[i] = lst[i - 1] / lst[i + 1]
                    i -= 1
                elif lst[i] == op == '*':
                    lst[i] = lst[i - 1] * lst[i + 1]
                    i -= 1
                elif lst[i] == op == '+':
                    lst[i] = lst[i - 1] + lst[i + 1]
                    i -= 1
                elif lst[i] == op == '-':
                    lst[i] = lst[i - 1] - lst[i + 1]
                    i -= 1
                elif lst[i] == op == '%':
                    lst[i] = lst[i - 1] % lst[i + 1]
                    i -= 1
                else:
                    i += 1
                    continue
                lst.pop(i + 2)
                lst.pop(i)
                leng -= 2
            i += 1
    if lst[0] == 0:
        lst.pop(0)
    if len(lst) == 1:
        return lst[0]
    else:
        return equate_lst(lst)


def equate():
    print('start equating')
    pre_eq = equation.get()
    lsts = [0]
    i = 0
    while i < len(pre_eq):
        if pre_eq[i].isdigit():
            lst_num = lsts[-1]
            if type(lst_num) == (int or float):
                if lst_num != 0:
                    lst_num *= 10
                lst_num += int(pre_eq[i])
                lsts[-1] = lst_num
        else:
            lsts.append(pre_eq[i])
            lsts.append(0)
        i += 1
    res = ''
    try:
        res = equate_lst(lsts)
    except:
        res = 'ND'
    if res:
        set_val(res, 'res')


equation_entry = ctk.CTkLabel(master=root, textvariable=equation)
result_label = ctk.CTkLabel(master=root, textvariable=result)
operation_label = ctk.CTkLabel(master=root, text='=')
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
    "0": ctk.CTkButton(master=number_frame, command=lambda: set_equation("0"), text="0", height=25, width=158),
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
number_buttons["0"].grid(row=3, column=0, columnspan=3, padx=2, pady=1)


operator_frame = ctk.CTkFrame(master=root)
operator_buttons = {
    "+": ctk.CTkButton(master=operator_frame, command=lambda: add_operator("+"), text="+", width=50, height=25),
    "-": ctk.CTkButton(master=operator_frame, command=lambda: add_operator("-"), text="-", width=50, height=25),
    "^": ctk.CTkButton(master=operator_frame, command=lambda: add_operator("^"), text="^", width=50, height=25),
    "*": ctk.CTkButton(master=operator_frame, command=lambda: add_operator("*"), text="*", width=50, height=25),
    "/": ctk.CTkButton(master=operator_frame, command=lambda: add_operator("/"), text="/", width=50, height=25),
    "%": ctk.CTkButton(master=operator_frame, command=lambda: add_operator("%"), text="%", width=50, height=25),
    "√": ctk.CTkButton(master=operator_frame, command=lambda: add_operator("√"), text="√", width=50, height=25),
    "=": ctk.CTkButton(master=operator_frame, command=lambda: equate(), text="=", width=104, height=25),
    "↼": ctk.CTkButton(master=operator_frame, command=lambda: remove_equation(), text="↼", width=50, height=50),
    "c": ctk.CTkButton(master=operator_frame, command=lambda: remove_equation(clear=True), text="c", width=50, height=25),
}

operator_frame.grid(row=3, column=1)
operator_buttons["+"].grid(row=0, column=0, padx=2, pady=1)
operator_buttons["-"].grid(row=0, column=1, padx=2, pady=1)
operator_buttons["^"].grid(row=0, column=2, padx=2, pady=1)
operator_buttons["*"].grid(row=1, column=0, padx=2, pady=1)
operator_buttons["/"].grid(row=1, column=1, padx=2, pady=1)
operator_buttons["%"].grid(row=2, column=0, padx=2, pady=1)
operator_buttons["√"].grid(row=2, column=1, padx=2, pady=1)
operator_buttons["="].grid(row=3, column=0, columnspan=2, padx=2, pady=1)
operator_buttons["↼"].grid(row=2, rowspan=2, column=2, padx=2, pady=1)
operator_buttons["c"].grid(row=1, column=2, padx=2, pady=1)

root.mainloop()