def converter(type, ans):
    if type in ["km", "kilometre", "kilometres"]:
        miles = ans/1.609344
        return miles
    else:
        miles = ans * 1.609344
        return miles




def checker():
    while True:
        km_or_m = str(input("Is this in kilometres or miles?: "))
        if km_or_m in ["km", "kilometre", "kilometres", "miles", "m", "miles"]:
            break
        else:
            print("Error\n")

    while True:
        ans = int(input("How far have you travled?: "))
        if ans is int():
            break
        else:
            print("Error\n")

    return(converter(km_or_m, ans))

print(checker())
