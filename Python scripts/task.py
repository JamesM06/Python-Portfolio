people = int(input("How many people do you want to invite: "))
if people > 10:
    for i in range(people):
        name = input("Please enter the name: ")
        print(f"{name} has been invited.")
