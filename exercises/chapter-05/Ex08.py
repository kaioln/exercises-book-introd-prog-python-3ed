num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = 0
count = 0

while count < num2:
    result += num1
    count += 1

print(f"Result: {result}")