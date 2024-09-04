num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

quotient = 0
rest = num1

while rest >= num2:
    rest -= num2
    quotient += 1

print(f"Quotient: {quotient}")
print(f"Rest: {rest}")