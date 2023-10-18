def isdigit(s): 
    all_digits = True 
    for letter in s: 
        if not letter in "1234567890": 
            all_digits = False 

    return all_digits 

print("12345", isdigit("12345"))
print("999", isdigit("999"))
print("abc-123", isdigit("abc-123"))
print("123456", isdigit("123456"))
