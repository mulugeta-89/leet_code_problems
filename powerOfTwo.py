def powerOfTwo(num):
    x = 0
    while x < 32:
        num /= 2
        if num == 1:
            return True
        x+=1
    return False
print(powerOfTwo(1))