carSpeed = int(input("Enter the Car Speed: "))
maxPermittedSpeed = 80
fine = 5

if carSpeed > maxPermittedSpeed:
    fineIncrement = carSpeed - maxPermittedSpeed

    finalValue = fineIncrement * fine

    print(f"You're fined! your fine is: {finalValue}")
else:
    print("Normal speed!")