merchandise_value = int(input("Enter the Merchandise value: "))
discount_percentage = int(input("Enter the Discount Percentage: "))

discount_value = merchandise_value * discount_percentage / 100
total_discounted_value = merchandise_value - discount_value

print(f"Discount Value: {discount_value}")
print(f"Total Discounted Value: ${total_discounted_value:1.2f}")