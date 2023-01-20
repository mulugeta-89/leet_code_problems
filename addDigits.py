def addDigit(num):
    num = str(num)
    total = 0
    if len(num) == 1:
        total += int(num)
        return total
    else:
        for item in num:
            total += int(item)
    total = str(total)
    if len(total) == 1:
        return int(total)
    sum = 0
    if len(total) > 1:
        for item in total:
            sum += int(item)
    sum = str(sum)
    if len(sum) == 1:
        return int(sum)
    sum2 = 0
    
    if len(sum) > 1:
        for item in sum:
            sum2 += int(item)
    return int(sum2)
print(addDigit(199))

