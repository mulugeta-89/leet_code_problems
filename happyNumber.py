def happyNumber(num):
    # if num == 1 or num == 7:
    #     return True
    running = 0
    while running < 9:
        num = str(num)
        sum = 0
        for item in num:
            sum += (pow(int(item),2))
        if sum == 1:
            return True
        num = sum
        running += 1
    return False
    
print(happyNumber(7))