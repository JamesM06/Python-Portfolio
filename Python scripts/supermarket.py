age = int(input("What is your age: "))
if age < 18:
    print("No discount.")
elif age >= 18:
    if age <= 24:
        print("you get 2.5% discount")
elif age >= 25:
    if age <= 31:
        print("you get 1.9% discount")
elif age >= 32:
    if age <= 39:
        print("you get 1.5% discount")
elif age >= 40:
     if age <= 54:
        print("you get 1.7% discount")
elif age >= 55:
    if age  <= 64:
        print("you get 2% discount")
elif age >= 65:
     if age <= 99:
        print("you get 23% discount")
