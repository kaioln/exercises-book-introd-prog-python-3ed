num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number:"))

question = str(input("Enter the operation type: "))

if question == "+":
    print(f"You chose the sum operation: {num1 + num2}")
elif question == "-":
    print(f"You chose the subtraction operation: {num1 - num2}")
elif question == "*":
    print(f"You chose the multiplication operation: {num1 * num2}")
elif question == "/":
    print(f"You chose the division operation: {num1 / num2:4.2f}")
else:
    print("Error! Choose the correct operation. Example: +, -, * or /")