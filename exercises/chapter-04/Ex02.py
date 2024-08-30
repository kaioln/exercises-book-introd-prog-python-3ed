cigarettesPerDay = int(input("Enter the quantity of Cigarettes: "))
yearsOfSmoking = int(input("Enther the quantity of Years Smoking: "))

totalCigarettes = cigarettesPerDay * yearsOfSmoking * 365

lostMinutes = totalCigarettes * 10

lostDays = lostMinutes / 1440

print(lostDays)