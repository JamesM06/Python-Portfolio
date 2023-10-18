

"""def swap(a, b):
    index = [a, b]
    if index[0] > index[1]:
        index = [a,b]
    else:
        index = [b,a]
    return index
"""

def swap(a, b):
    if(a<=b):
        temp = a
        a = b
        b = temp
        list_ = [b, a]
        return(list_)
    else:
        print("error")