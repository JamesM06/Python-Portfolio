#FORMULAR = (miles * 1.609)/3.785

miles = float(input("input the miles(m/g): "))

kpl = (miles * 1.609)/3.785
kpl = "{:.3f}".format(kpl)# to 3 decimal place

print(f"Klomiters/L: {kpl}")
