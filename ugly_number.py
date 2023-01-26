def ugly_number(num):
    if num == 0:
        return False
    factors =[2,3,5]
    for item in factors:
        while num %item == 0:
            num //= item
    return num == 1

print(ugly_number(1))