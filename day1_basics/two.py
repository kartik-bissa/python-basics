'python program to perfrom mathematical operations'

def sum(x, y):
    return x + y

def difference(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if(y == 0):
        return "Cannot be divided by zero"
    return x / y

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

Sum = print("Sum is: ",sum(a,b))
Divison = print("Quotient is: ", divide(a,b))