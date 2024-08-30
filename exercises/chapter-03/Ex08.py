merchandiseValue = int(input("Enter the Merchandise value: "))
discountPercentage = int(input("Enter the Discount Percentage: "))

discountValue = merchandiseValue * discountPercentage / 100
totalDiscountedValue = merchandiseValue - discountValue

print(f"Discount Value: {discountValue}")
print(f"Total Discounted Value: ${totalDiscountedValue:1.2f}")