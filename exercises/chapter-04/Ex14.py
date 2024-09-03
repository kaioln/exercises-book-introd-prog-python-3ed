kwhQuantity = float(input("Enter the kWh consumed number: "))
print("R for Residences, C for Commerce, and I for Industries")
installationType = str(input("Enter the Installation Type: "))

if installationType == "R" and kwhQuantity <= 500:
    price = 0.40
    print(f"The price of kWh is: ${price:3.2f}")
elif installationType == "R" and kwhQuantity > 500:
    price = 0.65
    print(f"The price of kWh is: ${price:3.2f}")
elif installationType == "C" and kwhQuantity >= 1000:
    price = 0.55
    print(f"The price of kWh is: ${price:3.2f}")
elif installationType == "I" and kwhQuantity > 1000:
    price = 0.60
    print(f"The price of kWh is: ${price:3.2f}")
elif installationType == "R" and kwhQuantity <= 5000:
    price = 0.55
    print(f"The price of kWh is: ${price:3.2f}")