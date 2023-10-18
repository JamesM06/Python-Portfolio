import string
import random, time
file = open("file.txt", "r")
ans = int(input("pick 1 for brown 2 for blond 3 for back. DNA sequence. "))
x = file.readlines()
print(x[ans-1])