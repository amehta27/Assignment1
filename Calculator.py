first_number = input("Input the first number:")
second_number = input("input the second number:")
operand = input("input the operand:")

def addfunction():
    return int(first_number) + int(second_number)

def subtractfunction():
     return int(first_number)  - int(second_number)

def multiply():
    return int(first_number)  * int(second_number)

def divide():
    return int(first_number)  / int(second_number)





def calculator():
 if  (operand == "+"):
    print(addfunction())
           #int(first_number) + int(second_number)
 elif (operand == "-"):
    print(subtractfunction())
 elif (operand == "*"):
    print(multiply())
 else:
    print(divide())

calculator()
