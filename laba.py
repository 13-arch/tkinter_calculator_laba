from tkinter import *
import math

def addition(a,b): 
    return a+b

def subtract(a,b): 
    return a-b

def multiply(a,b): 
    return a*b

def divide(a,b): 
    return a/b

def factorial(a):
    f=1
    for i in range(2,a+1):
        f*=i
    return f

def degree(a,b): 
    return a**b

def sine(a): 
    return math.sin(math.radians(a))

def cosine(a): 
    return math.cos(math.radians(a))

def tangent(a): 
    return math.tan(math.radians(a))

def cotangent(a): 
    return 1/math.tan(math.radians(a))

expression = ""

def btn_click(item):
    global expression
    input_field['state'] = "normal"
    if item == '=':
        try:
            result = calculate(expression)
            input_field.insert(END, '=' + str(result))
            expression = str(result)
        except Exception:
            input_field.delete(0, END)
            input_field.insert(0, 'Ошибка')
            expression = ""
    elif item == 'π': 
        expression += str(math.pi)
        input_field.insert(END, str(math.pi))
    else:
        expression += item
        input_field.insert(END, item)
    input_field['state'] = "readonly"

def bt_clear():
    global expression
    expression = ""
    input_field['state'] = "normal"
    input_field.delete(0, END)
    input_field['state'] = "readonly"

def calculate(vir):
    if "+" in vir:
        v = vir.split('+')
        result = float(v[0])
        for i in range(1,len(v)):
            result = addition(result,float(v[i]))
        return result
    elif "-" in vir:
        v = vir.split('-')
        result = float(v[0])
        for i in range(1,len(v)):
            result = subtract(result,float(v[i]))
        return result
    elif "*" in vir:
        v = vir.split('*')
        result = float(v[0])
        for i in range(1,len(v)):
            result = multiply(result,float(v[i]))
        return result
    elif "/" in vir:
        v = vir.split('/')
        result = float(v[0])
        for i in range(1,len(v)):
            result = divide(result,float(v[i]))
        return result
    elif "!" in vir:
        v = vir.replace("!","").strip()
        return factorial(int(v))
    elif "^" in vir:
        v = vir.split('^')
        result = float(v[0])
        for i in range(1,len(v)):
            result = degree(result,float(v[i]))
        return result
    elif "sin" in vir:
        v = vir.replace("sin","").strip("() ")
        return sine(float(v))
    elif "cos" in vir:
        v = vir.replace("cos","").strip("() ")
        return cosine(float(v))
    elif "tan" in vir:
        v = vir.replace("tan","").strip("() ")
        return tangent(float(v))
    elif "ctg" in vir:
        v = vir.replace("ctg","").strip("() ")
        return cotangent(float(v))
    else:
        return vir


root = Tk()
root.geometry("380x420")
root.title("Калькулятор")
root.resizable(0,0)

frame_input = Frame(root)
frame_input.grid(row=0,column=0,columnspan=5,sticky="nsew")

input_field = Entry(frame_input,font='Arial 15 bold',width=30,state="readonly")
input_field.pack(fill=BOTH)

buttons = [
    ('C'),
    ('7','8','9','/','('),
    ('4','5','6','*',')'),
    ('1','2','3','-','sin'),
    ('0','.','=','+','cos'),
    ('tan','ctg','^','!','π')]

for row in range(len(buttons)):
    for col in range(len(buttons[row])):
        text = buttons[row][col]
        if text == 'C':
            cmd = bt_clear
        else:
            cmd = lambda t=text: btn_click(t)
        Button(root,width=5,height=2,text=text,command=cmd).grid(row=row+2,column=col,sticky="nsew",padx=1,pady=1)

root.mainloop()
