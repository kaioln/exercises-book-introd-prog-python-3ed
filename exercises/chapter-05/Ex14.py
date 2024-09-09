count = 0
result = 0

while True:
    num1 = int(input("Enter the First number: "))
    num2 = int(input("Enter the Second number: "))
    
    if num1 == 0 or num2 == 0:
        break
    else:
        result += num1 + num2
        count += 2
        arithmeticMean = result / count
        break

print(f"Sum: {result}")
print(f"Arithmetic Mean: {arithmeticMean}")