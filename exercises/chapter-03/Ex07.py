salary = int(input("Salary: "))
increase = int(input(f"Salary Increase in percentage: "))
totalIncrease = salary * increase / 100
totalSalary = salary + totalIncrease


print(f"Total increased Salary: ${totalSalary:1.2f}")