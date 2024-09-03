houseValue = int(input("Enter the House value: "))
salary = int(input("Enter your salary: "))
yearsQuantity = int(input("Enter the years quantity: "))

monthsToPay = yearsQuantity * 12
installmentCalculation = houseValue / monthsToPay
salaryLimit = salary * 0.3

if installmentCalculation <= salaryLimit:
    print("loan has been approved")
    print(f"The loan will last for {monthsToPay} months")
else:
    print("Your bank loan was not approved!")