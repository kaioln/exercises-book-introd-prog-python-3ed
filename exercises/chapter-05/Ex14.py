initialDebtValue = int(input("Enter the initial debt amount: "))
interestRate = int(input("Enter the debt interest rate (annual): "))
monthQuantity = int(input("Enter the number of debt months: "))
monthlyPaid = int(input("Enter the monthly paid amount: "))

value = initialDebtValue
totalPaid = 0
totalInterestPaid = 0
actualMonth = 1

while actualMonth <= monthQuantity and value > 0:
    interestForMonth = value * (interestRate / 100 / 12)
    value = value + interestForMonth - monthlyPaid
    
    if value < 0:
        totalPaid += (monthlyPaid + value)
        value = 0
    else:
        totalPaid += monthlyPaid
        totalInterestPaid += interestForMonth
    
    print(f"At the end of month {actualMonth}, the debt value will be: ${value:.2f}")
    
    actualMonth += 1

print(f"\nTotal months for the debt: {actualMonth - 1}")
print(f"Total value paid: ${totalPaid:.2f}")
print(f"Total interest paid: ${totalInterestPaid:.2f}")

if value > 0:
    print(f"Remaining debt after the specified months: ${value:.2f}")
else:
    print("The debt is fully paid within the given months.")