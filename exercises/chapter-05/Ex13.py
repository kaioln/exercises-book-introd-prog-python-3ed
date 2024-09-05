initialDeposit = int(input("Enter the initial deposit amount: "))
interestRate = int(input("Enter the savings interest rate: "))
monthlyDeposited = int(input("Enter the monthly deposit amount: "))

x = 1
value = 0

while x <= 24:
    capitalIncrease = initialDeposit * (1 + (interestRate / 100)) ** x
    if monthlyDeposited != 0:
        capitalIncrease = capitalIncrease + (capitalIncrease + interestRate) + monthlyDeposited
    print(f"At the end of the {x}º, the rate value will be equal ${capitalIncrease:.2f}")
    x += 1
print(f"{capitalIncrease:6.2f}")