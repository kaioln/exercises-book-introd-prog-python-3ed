total = 0.0

while True:
    code = int(input("Enter the product code: "))

    if code == 0:     
        print(f"Total Purchased: ${total:6.2f}")
        break
    
    quantity = int(input("Enter the quantity purchased: "))

    if code == 1:
        price = 0.50
    elif code == 2:
        price = 1.00
    elif code == 3:
        price = 4.00
    elif code == 5:
        price = 7.00
    elif code == 9:
        price = 8.00
    else:
        print("Invalid Code!")
        
    total += price * quantity
