def reverse(x):
    if x==0:
        return 0
    if x < 0:
        x = -1*x
        x = str(x)
        x = list(x)
        x.reverse()
        x.insert(0, "-")
        x = "".join(x)
        return int(x) if x >= -(2**31) else 0
    x = str(x)
    x = list(x)
    x.reverse()
    x = "".join(x)
    return int(x) if int(x)<= 2**31-1 else 0
print(reverse(2100000000))