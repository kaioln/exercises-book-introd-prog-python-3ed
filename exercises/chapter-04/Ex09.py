minutes = int(input("How many minutes you already used this month: "))

if minutes < 200:
    price = 0.20
elif minutes < 400:
    price = 0.18
else:
    price = 0.15
print(f"You will pay this month: R${minutes * price:6.2f}")