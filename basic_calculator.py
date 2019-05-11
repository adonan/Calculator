def add(x,y):
    return x+y
def subtract(x,y):
    return  x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

x = int(input("Enter First Number: "))
oper = input("Enter the Operator: ")
y = int(input("Enter Second Number: "))

if(oper == '*'):
    multiply(x,y)
    print("The Result is = ",int(multiply(x,y)))
elif(oper == '-'):
    subtract(x,y)
    print("The Result is = ",int(subtract(x,y)))
elif(oper == '+'):
    add(x,y)
    print("The Result is = ",int(add(x,y)))
elif(oper == '/'):
    divide(x,y)
    print("The Result is = ",int(divide(x,y)))
else:
    print("wrong operator")

