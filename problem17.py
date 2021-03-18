# 17. Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.

def calc(num, num1, operator):
    if (operator== "+"):
        print (num+num1)
    
    if (operator=="-"):
        print(num-num1)
    
    if (operator=="*"):
        print(num*num1)
    
    if (operator=="/"):
        if (num1!=0):
            print(num/num1)
        else:
            print("Division by zero not applicable")

num=float( input("Enter the first number:"))
num1=float(input (" Enter the second number:"))
operator=input(" Enter the operator  ")


if operator=="/" or operator=="*" or operator=="+" or operator=="-":
    calc(num, num1, operator)

else:
    print(" Invalid operator")
