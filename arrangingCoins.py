def arrangingCoins(num):
    sum = 0
    counter = 0
    for i in range(1,num+1):
        sum += i
        if sum > num:
            break
        counter = counter + 1
    return counter
print(arrangingCoins(1))