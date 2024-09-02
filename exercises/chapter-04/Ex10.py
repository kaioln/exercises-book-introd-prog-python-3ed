category = int(input("Enter the product category: "))

if category == 1:
    price = 10
else:
    if category == 2:
        price = 18
    else:
        if category == 3:
            price = 23
        else:
            if category == 4:
                price = 26
            else:
                if category == 5:
                    price == 31
                else:
                    print("Invalid category, enter a digit from 1 to 5!")
                    price = 0
print(f"The product price is: R${price:6.2f}")