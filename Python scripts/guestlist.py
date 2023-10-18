guestlist = ["robin", "gorge", "mo", "Rue Pall"]
for i in guestlist:
    print(f"{i} is invited.")
print("\nMo cant make it. :(")
guestlist[3] = "Kyle"
print("new guest list\n")
for i in guestlist:
    print(f"{i} is invited.")
inv1 = guestlist.pop(0)
inv2 = guestlist.pop(2)
guestlist.clear()
print(f"The only people coming are {inv1} & {inv2}")