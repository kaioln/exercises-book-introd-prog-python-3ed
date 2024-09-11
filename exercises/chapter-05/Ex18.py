value = float(input("Enter the amount to pay: "))
banknotes = 0
coins = 0
currentBanknotes = 100
currentCoins = 50
remove = value
removeCents = int(value * 100 + 0.5)


print("Banknotes:")
while currentBanknotes > 0:
    count = 0
    while removeCents >= currentBanknotes * 100:
        removeCents -= currentBanknotes * 100
        count += 1
    if count > 0:
        print(f"{count} banknotes of ${currentBanknotes}")
    if remove == 0:
        print("Your money is gone")
        break
    if count > 0:
        print(f"{count} banknote(s) of ${banknotes}")
    elif currentBanknotes == 100:
        currentBanknotes = 50
    elif currentBanknotes == 50:
        currentBanknotes = 20
    elif currentBanknotes == 20:
        currentBanknotes = 10
    elif currentBanknotes == 10:
        currentBanknotes = 5
    elif currentBanknotes == 5:
        currentBanknotes = 1
        break
    banknotes = 0

print("Coins:")
while currentCoins > 0:
    count = 0
    while removeCents >= currentCoins:
        removeCents -= currentCoins
        count += 1
    if count > 0:
        print(f"{count} coin(s) of ${currentCoins / 100:.2f}")
    elif currentCoins == 100:
        currentCoins = 50
    elif currentCoins == 50:
        currentCoins = 20
    elif currentCoins == 20:
        currentCoins = 10
    elif currentCoins == 10:
        currentCoins = 5
    elif currentCoins == 5:
        currentCoins = 1
        break
    coins = 0
    