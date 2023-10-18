def is10():
    ans = int(input("Enter number: "))
    if ans >= 10:
        if ans == 10:
            return "number is 10"
        else:
            return "number is grater than 10"
    else:
        return "numbr is less than 10."
print(is10())