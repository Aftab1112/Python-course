num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
operator = input("Enter an operator : ")

if operator == "+":
    print("Addition is ", num1 + num2)
elif operator == "-":
    print("Substraction is ", num1 - num2)
elif operator == "*":
    print("Multiplication is ", num1 * num2)
elif operator == "/":
    print("Division is ", num1 / num2)
else:
    print("Invalid operator")
