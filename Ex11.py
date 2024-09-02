category = int(input("Enter the product category: "))

if category == 1:
    price = 10
elif category == 2:
    price = 18
elif category == 3:
    price = 23
elif category == 4:
    price = 26
elif category == 5:
    price == 31
else:
    print("Invalid category, enter a digit from 1 to 5!")
    price = 0
print(f"The product price is: R${price:6.2f}")