
# Lesson 5: Assignments | Python Functions
# 1. The Calculator App


#num1 = int(input()), operation, int(input())
num1 = int(input('Enter first number '))
operation = input('What opperation?') 
num2 =  int(input('Enter second number'))

def adds(num1, num2):
    number_add = num1 + num2
    if operation == 'add':
        return number_add   


 

def subtractions (num1, num2):
    number_sub = num1 - num2
    if operation == 'subtraction':
        return number_sub




def multiplications (num1, num2):
    number_multiply = num1 * num2
    if operation == 'multiply':
        return number_multiply

    


def divisions (num1, num2):
    number_divide = num1 / num2
    if operation == 'divide':
        return number_divide
    
   

if operation == 'add':
    print (adds(num1, num2))
elif operation == 'subtraction':
    print (subtractions(num1, num2))
elif operation == 'multiply':
    print (multiplications(num1, num2))
elif operation == 'divide':
    print (divisions(num1, num2))
else:
    print ('Invalid Input')


