def powerOfThree(num):
    if num == 1:
        return True
    x = 0
    while x < 32:
        num /= 4
        if num == 1:
            return True
        x+=1
    return False
print((powerOfThree(-1)))