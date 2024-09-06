initialDeposit = int(input("Enter the initial deposit amount: "))
interestRate = int(input("Enter the savings interest rate: "))
monthlyDeposited = int(input("Enter the monthly deposit amount: "))

month = 1
value = initialDeposit  

while month <= 24:
    value = value * (1 + interestRate / 100 / 12) + monthlyDeposited
    print(f"At the end of month {month}, the rate value will be: ${value:.2f}")
    month += 1  

print(f"Total value after 24 months: ${value:.2f}")