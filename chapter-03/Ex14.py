salary = int(input("Enter salary to calculate tax: "))
base = salary
tax = 0

if base > 3000:
    tax = tax + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    tax = tax + ((base - 1000) * 0.20)
print(f"Salary: ${salary:6.2f} tax to pay: ${tax:6.2f}")