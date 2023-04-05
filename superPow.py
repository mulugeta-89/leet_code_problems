
def superp(a,b):
    new_b = ""
    for item in b:
        new_b += str(item)
    return pow(a, int(new_b), 1337)
print(superp(2147483647, [2,0,0]))