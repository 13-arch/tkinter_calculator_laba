from tkinter import *
from tkinter import ttk
import math
import re 

def factorial(n):
    return math.factorial(int(n))

def sine(a): 
    return math.sin(math.radians(a))

def cosine(a): 
    return math.cos(math.radians(a))

def tangent(a): 
    return math.tan(math.radians(a))

def cotangent(a): 
    tan_val = math.tan(math.radians(a))
    if abs(tan_val) < 1e-10:
        return float('inf')
    return 1 / tan_val

expression = ""

def btn_click(item):
    global expression
    input_var.set(input_var.get().replace('Ошибка', ''))
    
    if item == '=':
        try:
            current_expression = input_var.get()
            current_expression = current_expression.replace('π', str(math.pi))
            
            result = calculate(current_expression)
            
            if result == int(result):
                result = int(result)
            
            input_var.set(str(result))
            expression = str(result)
            
        except Exception as e:
            input_var.set('Ошибка')
            expression = ""
            
    elif item == 'C':
        expression = ""
        input_var.set("")
        
    elif item == 'π': 
        expression += str(math.pi)
        input_var.set(input_var.get() + "π")
        
    else:
        if item in ['sin', 'cos', 'tan', 'ctg']:
            expression += item + "("
            input_var.set(input_var.get() + item + "(")
        else:
            expression += item
            input_var.set(input_var.get() + item)

def calculate(vir):
    root_pattern = r'(\d+\.?\d*)\s*√\s*(\d+\.?\d*)'

    vir = re.sub(root_pattern, r'(\2**(1/\1))', vir)

    vir = vir.replace('^', '**')
    vir = re.sub(r'(\d+\.?\d*)!', r'factorial(\1)', vir)

    functions = {
        "sin": sine,
        "cos": cosine,
        "tan": tangent,
        "ctg": cotangent,
        "factorial": factorial,
        "math": math
    }
    
    return eval(vir, {"__builtins__": None}, functions)


root_win = Tk()
root_win.geometry("340x320")
root_win.title("Калькулятор")
root_win.resizable(0,0)

style = ttk.Style()
style.theme_use('clam') 

style.configure('TButton', font=('Arial', 10, 'bold'), padding=5)
style.map('TButton', background=[('active', '#e0e0e0')])

frame_input = Frame(root_win, bd=5) 
frame_input.grid(row=0,column=0,columnspan=5,sticky="nsew", padx=5, pady=5)

input_var = StringVar()
input_field = ttk.Entry(frame_input, textvariable=input_var, font=('Arial', 16, 'bold'), 
                        justify=RIGHT, state="readonly")
input_field.pack(fill=BOTH, ipady=10)

buttons_layout = [
    ('C', '(', ')', '^', '√'),
    ('7','8','9','/','sin'),
    ('4','5','6','*','cos'),
    ('1','2','3','-','tan'),
    ('0','.','=','+','ctg'),
    ('!', 'π', '', '', '') 
]

row_val = 1
for row in buttons_layout:
    col_val = 0
    for text in row:
        if not text:
            col_val += 1
            continue
            
        cmd = lambda t=text: btn_click(t)
        
        btn = ttk.Button(root_win, text=text, command=cmd)
        
        btn.grid(row=row_val, column=col_val, sticky="nsew", padx=2, pady=2)
        
        col_val += 1
    row_val += 1

for i in range(5):
    root_win.grid_columnconfigure(i, weight=1)
for i in range(7):
    root_win.grid_rowconfigure(i, weight=1)

root_win.mainloop()