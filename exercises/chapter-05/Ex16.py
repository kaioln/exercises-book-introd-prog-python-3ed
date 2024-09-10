value = int(input("Enter the amount to pay: "))
banknotes = 0
current = 50
remove = value

if value == 0:
    print("You don't have money to pay!")
else:
    while True:
        if current <= remove:
                remove -= current
                banknotes += 1
        else:
            if banknotes > 0:
                print(f"{banknotes} banknotes of ${current}")
            if remove == 0:
                print("Your money is gone")
                break
            elif current == 50:
                current = 20
            elif current == 20:
                current = 10
            elif current == 10:
                current = 5
            elif current == 5:
                current = 1
            banknotes = 0
            