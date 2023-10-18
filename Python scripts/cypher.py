year = int(input("Input a year e.g. 2018: "))
temp = year % 4
if temp != 0:
    print(f"{year} is not a leap year")
else:
    print(f"{year} is a leap year")