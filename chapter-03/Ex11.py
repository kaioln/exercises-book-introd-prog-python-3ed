kilometersDriven = int(input("Enter the Kilometers Driven: "))
daysRented = int(input("Enter the quantity of days rented: "))

rentalCoustPerDay = 60
perKm = 0.15

totalCoust = (kiloMetersDriven * perKm) + (daysRented * rentalCoustPerDay)
print(f"Total Value: {totalCoust}")