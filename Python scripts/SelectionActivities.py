ans = str(input("Day of the week (In 3 letter form (mon-fri)):"))
if ans == "sat" or ans == "sun":
    print("weekend")
elif ans in ["mon", "tue", "wed", "thu", "fri"]:
    print("weekday")
