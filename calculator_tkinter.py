# the calculation 
from tkinter import *
import numbers

number1 = number2 = command = answer = ''
first_second = 1

# binding the key 1 to this function (same for all other numbers)
def rb1(self):
    button1()

# the calculation that go when you press 1 (same for all other numbers)
def button1():
    global number1, number2, command, answer
    if len(number1)+len(number2)<13: #to make sure that the number doesn't go out of bounds
        if first_second == 1: 
            if answer != '':
                number1 = ''
            number1 += '1' 
            answer = ''
            numbers.screen.config(text = number1, font=20, width=15, height=2 ) #changing the text on the screen
        else:
            number2 += '1'
            numbers.screen.config(text = number1 + command + number2, font=20, width=15, height=2 )
    else:
        numbers.screen.config(text = 'OVERLOAD', font=20, width=15, height=2 )

def rb2(self):
    button2()
def button2():
    global number1, number2, command,answer
    if len(number1)+len(number2)<13:    
        if first_second == 1: 
            if answer != '':
                number1 = ''
            number1 += '2'
            answer = ''
            numbers.screen.config(text = number1, font=20, width=15, height=2 )
        else:
            number2 += '2'
            numbers.screen.config(text = number1 + command + number2, font=20, width=15, height=2 )
    else:
        numbers.screen.config(text = 'OVERLOAD', font=20, width=15, height=2 )

def rb3(self):
    button3()
def button3():
    global number1, number2, command,answer
    if len(number1)+len(number2)<13:
        if first_second == 1: 
            if answer != '':
                number1 = ''
            number1 += '3'
            answer = ''
            numbers.screen.config(text = number1, font=20, width=15, height=2 )
        else:
            number2 += '3'
            numbers.screen.config(text = number1 + command + number2, font=20, width=15, height=2 )
    else:
        numbers.screen.config(text = 'OVERLOAD', font=20, width=15, height=2 )
    
def rb4(self):
    button4()
def button4():
    global number1, number2, command,answer
    if len(number1)+len(number2)<13:
        if first_second == 1: 
            if answer != '':
                number1 = ''
            number1 += '4'
            answer = ''
            numbers.screen.config(text = number1, font=20, width=15, height=2 )
        else:
            number2 += '4'
            numbers.screen.config(text = number1 + command + number2, font=20, width=15, height=2 )
    else:
        numbers.screen.config(text = 'OVERLOAD', font=20, width=15, height=2 )
    
def rb5(self):
    button5()
def button5():
    global number1, number2, command,answer
    if len(number1)+len(number2)<13:
        if first_second == 1: 
            if answer != '':
                number1 = ''
            number1 += '5'
            answer = ''
            numbers.screen.config(text = number1, font=20, width=15, height=2 )
        else:
            number2 += '5'
            numbers.screen.config(text = number1 + command + number2, font=20, width=15, height=2 )
    else:
        numbers.screen.config(text = 'OVERLOAD', font=20, width=15, height=2 )
    
def rb6(self):
    button6()
def button6():
    global number1, number2, command,answer
    if len(number1)+len(number2)<13:
        if first_second == 1: 
            if answer != '':
                number1 = ''
            number1 += '6'
            answer = ''
            numbers.screen.config(text = number1, font=20, width=15, height=2 )
        else:
            number2 += '6'
            numbers.screen.config(text = number1 + command + number2 , font=20, width=15, height=2 )
    else:
        numbers.screen.config(text = 'OVERLOAD', font=20, width=15, height=2 )
    
def rb7(self):
    button7()
def button7():
    global number1, number2, command, answer
    if len(number1)+len(number2)<13:
        if first_second == 1: 
            if answer != '':
                number1 = ''
            number1 += '7'
            answer = ''
            numbers.screen.config(text = number1, font=20, width=15, height=2 )
        else:
            number2 += '7'
            numbers.screen.config(text = number1 + command + number2 , font=20, width=15, height=2 )
    else:
        numbers.screen.config(text = 'OVERLOAD', font=20, width=15, height=2 )
    
def rb8(self):
    button8()
def button8():
    global number1, number2, command, answer
    if len(number1)+len(number2)<13:
        if first_second == 1: 
            if answer != '':
                number1 = ''
            number1 += '8'
            answer = ''
            numbers.screen.config(text = number1, font=20, width=15, height=2 )
        else:
            number2 += '8'
            numbers.screen.config(text = number1 + command + number2, font=20, width=15, height=2 )
    else:
        numbers.screen.config(text = 'OVERLOAD', font=20, width=15, height=2 )
    
def rb9(self):
    button9()
def button9():
    global number1, number2, command, answer
    if len(number1)+len(number2)<13:
        if first_second == 1: 
            if answer != '':
                number1 = ''
            number1 += '9'
            answer = ''
            numbers.screen.config(text = number1, font=20, width=15, height=2 )
        else:
            number2 += '9'
            numbers.screen.config(text = number1 + command + number2, font=20, width=15, height=2 )
    else:
        numbers.screen.config(text = 'OVERLOAD', font=20, width=15, height=2 )
    
def rb0(self):
    button0()
def button0():
    global number1, number2, command, answer
    if len(number1)+len(number2)<13:
        if first_second == 1: 
            if answer != '':
                number1 = ''
            number1 += '0'
            answer = ''
            numbers.screen.config(text = number1, font=20, width=15, height=2 )
        else:
            number2 += '0'
            numbers.screen.config(text = number1 + command + number2 , font=20, width=15, height=2 )
    else:
        numbers.screen.config(text = 'OVERLOAD', font=20, width=15, height=2 )
    
# this is in a case where you want to continue a calculation without pressing '='
def check_answer():
    global number1, number2, first_second
    if number2 != '':
        if command == '+':
            number1 = round(float(number1) + float(number2), 3)
            number1 = str(number1)
        if command == '-':
            number1 = round(float(number1) - float(number2), 3)
            number1 = str(number1)
        if command == '*':
            number1 = round(float(number1)*float(number2), 3)
            number1 = str(number1)
        if command == '/':
            intN1 = float(number1)
            intN2 = int(number2)
            number1 = round(float(intN1/intN2), 3)
            number1 = str(number1)
        number2 = ''
        first_second = 2

# what happens when you press the '+' sign (same for all other commands)
def rb_plus(self):
    button_plus()
def button_plus():
    global first_second, command, number1, number2
    if number1 != '':
        check_answer() 
        command = '+'
        first_second = 2
        numbers.screen.config(text = f'{number1} +', font=20, width=15, height=2 )
    else:
        numbers.screen.config(text = 'Enter a number', font=20, width=15, height=2)
        first_second = 1

def rb_minus(self):
    button_minus()
def button_minus():
    global first_second, command, number1, number2
    if number1 != '':
        check_answer() 
        command = '-'
        first_second = 2
        numbers.screen.config(text = f'{number1} -', font=20, width=15, height=2 )
    else:
        numbers.screen.config(text = 'Enter a number', font=20, width=15, height=2)
        first_second = 1

def rb_times(self):
    button_times()
def button_times():
    global first_second, command, number1, number2
    if number1 != '':
        check_answer() 
        command = '*'
        first_second = 2
        numbers.screen.config(text = f'{number1} *', font=20, width=15, height=2 )
    else:
        numbers.screen.config(text = 'Enter a number', font=20, width=15, height=2)
        first_second = 1

def rb_devide(self):
    button_divide()
def button_divide():
    global first_second, command, number1, number2
    if number1 != '':
        check_answer() 
        command = '/'
        first_second = 2
        numbers.screen.config(text = f'{number1} /', font=20, width=15, height=2 )
    else:
        numbers.screen.config(text = 'Enter a number', font=20, width=15, height=2)
        first_second = 1


def rb_equal(self):
    button_equal()
def button_equal():
    global first_second, answer, command
    # going through all cases
    if number1 == '':
        numbers.screen.config(text = 'Enter a number', font=20, width=15, height=2)
        first_second = 1
    if number1 != '' and number2 == '':
        numbers.screen.config(text = number1 , font=20, width=15, height=2)
        first_second = 1
    if number2 != '':
        check_answer()
        if len(number1)<13:
            numbers.screen.config(text = number1 , font=20, width=15, height=2)
            first_second = 1
            command = ''
            answer = number1
        else:
            numbers.screen.config(text = 'OVERLOAD', font=20, width=15, height=2 )

# clearing the screen and data 
def rb_clear(self):
    button_clear()
def button_clear():
    global number1, number2, first_second, command, answer
    number1 = number2 = answer = ''
    command = ''
    first_second = 1
    numbers.screen.config(text = '', font=20, width=15, height=2 )








