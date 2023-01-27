def powerOfThree(num):
    x = 0
    while x < 32:
        num /= 3
        if num == 1:
            return True
        x+=1
    return False
print((powerOfThree(-1)))