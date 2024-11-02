

def calculator():
    try:
        num1 = float(input("Enter first number : "))
    except:
        print("Invalid number")
        return None

    try:
        num2 = float(input("Enter second number : "))
    except:
        print("Invalid number")
        return None

    print("Select operator ")

    print("1. Addition (+) : ")
    print("2. Substraction (-) : ")
    print("3. Multiplication (*) : ")
    print("4. Division (/) : ")

    try:
        operator = int(input("Select the operator (1-4) : "))
        if operator not in [1,2,3,4]:
            print("Invalid Operator")
            return None
    except:
        print("Invalid operator")
        return  None
    if operator == 1:
        print(f" {num1} + {num2} = {num1+num2}")
    if operator == 2:
        print(f" {num1} - {num2} = {num1-num2}")
    if operator == 3:
        print(f" {num1} * {num2} = {num1*num2}")
    if operator == 4:
        if num2==0:
            print(f"{ num1 } Can't divide by Zero ")
        else : 
            print(f" {num1} / {num2} = {num1/num2}")

while True:
    calculator()