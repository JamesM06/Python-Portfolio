totalCost = 0.00

print("-Pizza Calculator-")
crust = str(input("Thick or Thin crust: "))
size = str(input("What is the size 8, 10, 12, 14, and 18 inch: "))
cheese = str(input("Is there cheese on that: "))
type_ = str(input("do you want;\nMargherita\nVegetable\nVegan\nHawaiian\nMeat\nfeast\n:"))
voucher = str(input("If you have a voucher input the code: "))

if crust == "thick":
    totalCost += 8.00
else:
    totalCost += 10.00

if size != "8 inch" or "10 inch":
    
if cheese == "yes":
    totalCost += 0.50

if type_ == "vegan" or "vegetable":
    totalCost += 1.00
elif type_ == "hawaiian" or "meat feast":
     += 2.00

if voucher == "FunFriday" and size == "18 inch":
    
    totalCost -= 2.00

print(f"your cost is: {totalCost}")
