balance = 0
while balance < 50:
    if balance >= 50:
        break
    inserted_coin = int(input("Insert Coin: "))
    if inserted_coin in [25, 10, 5]:
        balance += inserted_coin
        if balance >= 50:
            print("Change Owed:", balance - 50)
            break
        amount_due = 50 - balance
        print("Amount Due:", amount_due)
    else:
        print("Amount Due: 50")
        continue


