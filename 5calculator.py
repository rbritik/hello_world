from tkinter import *
root = Tk()

root.title("Simple Calculator")
# Output Screen
e = Entry(root, width = 40, borderwidth = 10)
e.grid(row = 0, columnspan = 3)

# Putting clicked numbers on Screen
def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current)+str(number))

# clearing the Screen
def button_clear():
    e.delete(0,END)
    
#Button for Addition operation
def button_addition():
    first_num = e.get()
    global f_num, operator
    operator = '+'
    f_num = float(first_num)
    e.delete(0,END)

# Button for Subtraction operation
def button_subtraction():
    first_num = e.get()
    global f_num, operator
    operator = '-'
    f_num = float(first_num)
    e.delete(0,END)

# Button for Multiplication operation
def button_multiplication():
    first_num = e.get()
    global f_num, operator
    operator = '*'
    f_num = float(first_num)
    e.delete(0,END)

# Button for Division operation
def button_division():
    first_num = e.get()
    global f_num,  operator
    operator = '/' 
    f_num = float(first_num)
    e.delete(0,END)

# Button for Remainder operation
def button_remainder():
    first_num = e.get()
    global f_num,  operator
    operator = '%'
    f_num = float(first_num)
    e.delete(0,END)

# Final Output
def button_equal():
    second_num = float(e.get())
    e.delete(0,END)
    if operator == '+':
         e.insert(0, f_num + second_num)
    elif operator == '-':
         e.insert(0, f_num - second_num)
    elif operator == '*':
         e.insert(0, f_num * second_num)
    elif operator == '/':
         e.insert(0, f_num / second_num)
    elif operator == '%':
         e.insert(0, f_num % second_num)

# Adding Buttons
button_1 = Button(root, text = '1', padx = 39, pady = 25, fg = 'blue', command = lambda: button_click(1))
button_2 = Button(root, text = '2', padx = 39, pady = 25, fg = 'blue',command = lambda: button_click(2))
button_3 = Button(root, text = '3', padx = 39, pady = 25, fg = 'blue',command = lambda: button_click(3))
button_4 = Button(root, text = '4', padx = 39, pady = 25, fg = 'blue',command = lambda: button_click(4))
button_5 = Button(root, text = '5', padx = 39, pady = 25, fg = 'blue',command = lambda: button_click(5))
button_6 = Button(root, text = '6', padx = 39, pady = 25, fg = 'blue',command = lambda: button_click(6))
button_7 = Button(root, text = '7', padx = 39, pady = 25, fg = 'blue',command = lambda: button_click(7))
button_8 = Button(root, text = '8', padx = 39, pady = 25, fg = 'blue',command = lambda: button_click(8))
button_9 = Button(root, text = '9', padx = 39, pady = 25, fg = 'blue',command = lambda: button_click(9))
button_0 = Button(root, text = '0', padx = 39, pady = 25, fg = 'blue',command = lambda: button_click(0))
button_decimal = Button(root, text = '.', padx = 40, pady = 25, fg = 'blue',command = lambda: button_click('.'))
button_equal = Button(root, text ='=', padx = 89, pady=25, fg = 'blue', command = button_equal)
button_remainder = Button(root, text = '%', padx = 40, pady = 25, fg = 'blue',command = button_remainder)
button_addition = Button(root, text = '+', padx = 40, pady = 25, fg = 'blue',command = button_addition)
button_subtraction = Button(root, text = '-', padx = 40, pady = 25, fg = 'blue',command = button_subtraction)
button_multiplication = Button(root, text = '*', padx = 40, pady = 25, fg = 'blue',command = button_multiplication)
button_division = Button(root, text = '/',padx = 39, pady = 25, fg = 'blue', command = button_division)
button_clear = Button(root, text = 'Clear',padx = 75, pady = 25, fg = 'blue',command = button_clear)

# Putting Buttons on the Screen
button_7.grid(row = 1, column =0)
button_8.grid(row = 1, column =1)
button_9.grid(row = 1, column =2)
button_4.grid(row = 2, column =0)
button_5.grid(row = 2, column =1)
button_6.grid(row = 2, column =2)
button_1.grid(row = 3, column =0)
button_2.grid(row = 3, column =1)
button_3.grid(row = 3, column =2)
button_0.grid(row = 4, column =1)
button_decimal.grid(row = 4, column =0)
button_remainder.grid(row = 4, column =2)
button_addition.grid(row = 1, column = 3)
button_subtraction.grid(row = 2, column = 3)
button_multiplication.grid(row = 3, column = 3)
button_division.grid(row = 4, column = 3)
button_equal.grid(row = 5, column =0, columnspan = 2)
button_clear.grid(row = 5, column =2, columnspan = 2)

root.mainloop()