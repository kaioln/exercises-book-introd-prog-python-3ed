salary = int(input("Salary: "))
increase = int(input(f"Salary Increase in percentage: "))
total_increase = salary * increase / 100
total_salary = salary + total_increase


print(f"Total increased Salary: ${total_salary:1.2f}")