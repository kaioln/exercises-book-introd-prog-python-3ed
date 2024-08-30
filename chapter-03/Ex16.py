salary = int(input("Enter your salary: "))
salaryIncrease = 0

if salary > 1250:
    salaryIncrease = salary + (salary * 0.10)
    print(f"Your new Salary: ${salaryIncrease:6.2f}")
if salary <= 1250:
    salaryIncrease = salary + (salary * 0.15)
    print(f"Your new Salary: ${salaryIncrease:6.2f}")