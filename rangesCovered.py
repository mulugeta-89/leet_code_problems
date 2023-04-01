def rangesCovered(ranges, left, right):
    flag = False
    counter = 0
    for i in range(left, right+1):
        for item in ranges:
            if i in range(item[0], item[1]+1):
                flag = True
                break
        if flag:
            counter += 1
        flag = False
    return counter == (right-left)+1
print(rangesCovered([[1,1]], 1,50))