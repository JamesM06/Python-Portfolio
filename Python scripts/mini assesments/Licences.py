amount = 0



while True:
    amount = int(input("Lisences needed: "))
    if amount > 0:
        break
    print("error\n")
cost = amount * 35
print(f"cost of {amount}: £{cost}")
if amount > 20:
    #cost = cost - cost / 10
    #cost /= 10
    print("10% discont applied")
print(f"final cost: £{cost}")