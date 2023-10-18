import math

ans = str(input("input 1 for squere or 2 for a rectangle. ans 3 for a circle,\n4 for a triangle. 5 for a volume of a prisum:"))

if ans == "1":
    h = int(input("Please input the hight number? "))
    #l = int(input("Please input the length number? "))
    print(f"The aria is {h*h}")
elif ans == "2":
    h = int(input("Please input the hight number? "))
    l = int(input("Please input the length number? "))
    print(f"The aria is {h*l}")    
elif ans == "3":
    r = float(input("Please enter the radius: "))
    pi = math.pi
    z = (r ** 2) * pi
    print(f"The area is {z:.3f}")
elif ans == "4":
    h = int(input("Please input the hight number? "))
    b = int(input("Please input the bace number? "))
    a = 0.5 * b * h
    print(f"The area is {a:.3f}")
elif ans == "5":
    h = int(input("Please input the hight number? "))
    b = int(input("Please input the bace number? "))
    V = b * h
    print(f"The Volume is {a:.3f}")
